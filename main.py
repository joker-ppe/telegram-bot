import asyncio
from datetime import datetime, timedelta
import os
import random
import sys
from typing import Final
from telegram import Bot

from parser_text import send_table_user_image
from worker import get_user
import imgkit, pdfkit


TOKEN: Final = '6694721541:AAGnKKDpDoqkQOAMOMQozKwinBpt-awUCvA'

async def send_message() -> bool:
    bot = Bot(TOKEN)
    chat_id = '-1002109063811'
    print(f'Send Scheduled notification to {chat_id}')

    yesterday = datetime.now() - timedelta(days=1)
    formatted_yesterday = yesterday.strftime('%Y-%m-%d')

    today = datetime.now()
    # Calculate the number of days to subtract to get to Monday
    # weekday() returns 0 for Monday, 1 for Tuesday, and so on
    days_to_subtract = today.weekday()
    monday = today - timedelta(days=days_to_subtract)
    formatted_monday = monday.strftime('%Y-%m-%d')
    from_date = formatted_monday
    end_date = datetime.now().strftime('%Y-%m-%d')

    user = await get_user(from_date, end_date, formatted_yesterday, 'admin')
    # user = await get_user(from_date, formatted_yesterday, (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'), info)
    response = await send_table_user_image(user)
    message_id = random.randint(1, 1000)
    
    try:
        options = {
    'format': 'jpg',
    'width': '600',
    # Adjust the quality (0-100). Lower might reduce clarity.
    'quality': '100',
    # Adjust width as per requirement
    # Other options as needed...
}
        imgkit.from_string(response, f'{message_id}{chat_id}.jpg', options=options)
        with open(f'{message_id}{chat_id}.jpg', 'rb') as image:
            await bot.send_photo(chat_id=chat_id, photo=image)
        # Delete the image after sending
        os.remove(f'{message_id}{chat_id}.jpg')
    except Exception:
        pdfkit.from_string(response, f'{message_id}{chat_id}.pdf')
        with open(f'{message_id}{chat_id}.pdf', 'rb') as file:
            await bot.send_document(chat_id=chat_id, document=file)

        # Delete the image after sending
        os.remove(f'{message_id}{chat_id}.pdf')
    return True


if __name__ == '__main__':
    result = asyncio.run(send_message())

    sys.exit(int(not result))