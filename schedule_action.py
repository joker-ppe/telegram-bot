# Add all required schedules
import asyncio
from datetime import datetime, timedelta
import os
import random
from parser_text import send_table_user_image
import schedule
from worker import get_user
import imgkit, pdfkit





async def send_notification(app):
    chat_id = '-1002109063811'  # Replace with the chat ID to send notifications
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



def setup_schedules_send_report(app, hour, minute):
    # hour = 11
    # minute = 18
    time_str = f"{hour}:{minute:02}"
    # def run_async():
    #     asyncio.run(send_notification(app))

    schedule.every().day.at(time_str).do(send_notification, app)


# Scheduled action: sending a notification
async def send_notification_message(app, message):
    chat_id = '-1002109063811'  # Replace with the chat ID to send notifications
    await app.bot.send_message(chat_id=chat_id, text=f"{message}")


def setup_schedules_send_message(app, hour, minute, message):
    # hour = 11
    # minute = 18
    time_str = f"{hour}:{minute:02}"
    # def run_async():
    #     asyncio.run(send_notification_message(app, message))

    schedule.every().day.at(time_str).do(lambda: asyncio.run(send_notification_message(app, message)))



















