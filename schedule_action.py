# Add all required schedules
import asyncio
from datetime import datetime, timedelta
import os
import random
from parser_text import send_table_image, send_table_user_image
import schedule
from worker import get_masters, get_user
import imgkit, pdfkit
from telegram.ext import ContextTypes

GROUP_CHAT_ID = '-1002044356915'

options = {
    'format': 'jpg',
    'width': '600',
    # Adjust the quality (0-100). Lower might reduce clarity.
    'quality': '100',
    # Adjust width as per requirement
    # Other options as needed...
}


async def send_notification(app: ContextTypes.DEFAULT_TYPE):
    chat_id = GROUP_CHAT_ID  # Replace with the chat ID to send notifications
    print(f'Send daily report admin to {chat_id}')

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
        imgkit.from_string(response, f'{message_id}{chat_id}.jpg', options=options)
        with open(f'{message_id}{chat_id}.jpg', 'rb') as image:
            await app.bot.send_photo(chat_id=chat_id, photo=image)
        # Delete the image after sending
        os.remove(f'{message_id}{chat_id}.jpg')
    except Exception:
        pdfkit.from_string(response, f'{message_id}{chat_id}.pdf')
        with open(f'{message_id}{chat_id}.pdf', 'rb') as file:
            await app.bot.send_document(chat_id=chat_id, document=file)

        # Delete the image after sending
        os.remove(f'{message_id}{chat_id}.pdf')


    # await app.bot.send_message(chat_id=chat_id, text="Scheduled Notification")


# Scheduled action: sending a notification
async def send_notification_message(app: ContextTypes.DEFAULT_TYPE):
    chat_id = GROUP_CHAT_ID  # Replace with the chat ID to send notifications
    
    print(f'Send daily report master to {chat_id}')

    today = datetime.now()
    # Calculate the number of days to subtract to get to Monday
    # weekday() returns 0 for Monday, 1 for Tuesday, and so on
    days_to_subtract = today.weekday()
    monday = today - timedelta(days=days_to_subtract)
    formatted_monday = monday.strftime('%Y-%m-%d')
    from_date = formatted_monday
    end_date = datetime.now().strftime('%Y-%m-%d')

    masters = await get_masters(from_date, end_date)
    response = await send_table_image(masters, 'tuần này', 'Tổng Đại Lý')
    message_id = random.randint(1, 1000)

    try:
        imgkit.from_string(response, f'{message_id}{chat_id}.jpg', options=options)
        with open(f'{message_id}{chat_id}.jpg', 'rb') as image:
            await app.bot.send_photo(chat_id=chat_id, photo=image)
        # Delete the image after sending
        os.remove(f'{message_id}{chat_id}.jpg')
    except Exception:
        pdfkit.from_string(response, f'{message_id}{chat_id}.pdf')
        with open(f'{message_id}{chat_id}.pdf', 'rb') as file:
            await app.bot.send_document(chat_id=chat_id, document=file)

        # Delete the image after sending
        os.remove(f'{message_id}{chat_id}.pdf')












