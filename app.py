# import everything
import asyncio
import os
import imgkit, pdfkit
from datetime import datetime, timedelta, time
from typing import Final
import pytz
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from schedule_action import send_notification, send_notification_message

from worker import *
from parser_text import *
from type_action import *
from settings import *

# Command

options = {
    'format': 'jpg',
    'width': '600',
    # Adjust the quality (0-100). Lower might reduce clarity.
    'quality': '100',
    # Adjust width as per requirement
    # Other options as needed...
}


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f'{chat_id}')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('ok okokokok')


async def wl_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await get_list_users_data()
    print('')
    # await update.message.reply_text(asyncio.run(main()))


# Responses

async def handle_response(text: str) -> str:
    text_full = text.replace(':', '').strip()

    today = datetime.now()
    # Calculate the number of days to subtract to get to Monday
    # weekday() returns 0 for Monday, 1 for Tuesday, and so on
    days_to_subtract = today.weekday()
    monday = today - timedelta(days=days_to_subtract)
    formatted_monday = monday.strftime('%Y-%m-%d')
    from_date = formatted_monday
    end_date = datetime.now().strftime('%Y-%m-%d')

    time_text = 'tuần này'
    # get time
    if detect_today(text_full):
        # do nothing
        from_date = datetime.now().strftime('%Y-%m-%d')
        end_date = from_date
        time_text = 'hôm nay'
    elif detect_yesterday(text_full):
        yesterday = datetime.now() - timedelta(days=1)
        formatted_yesterday = yesterday.strftime('%Y-%m-%d')
        from_date = formatted_yesterday
        end_date = formatted_yesterday
        time_text = 'hôm qua'
    elif detect_this_week(text_full):
        time_text = 'tuần này'

    # call api
    if detect_report_xsmb(text_full):
        report = await get_report_xsmb()
        return report
    elif detect_os_cong_ty(text_full):
        date = datetime.now().strftime('%Y-%m-%d')
        os = await get_user_os(date, date, 'admin')
        return check_response(f'Outstanding hôm nay:', os)
    elif detect_os_super(text_full):
        supers = await get_supers(from_date, end_date)
        return await send_table_os_image(supers, 'Cổ Đông')
    elif detect_os_master(text_full):
        masters = await get_masters(from_date, end_date)
        return await send_table_os_image(masters, 'Tổng Đại Lý')
    elif detect_os_agent(text_full):
        agents = await get_agents(from_date, end_date)
        return await send_table_os_image(agents, 'Đại Lý')
    elif detect_os_member(text_full):
        members = await get_members(from_date, end_date)
        return await send_table_os_image(members, 'Hội Viên')
    elif detect_doanh_thu_cong_ty(text_full):
        profit = await get_user_profit(from_date, end_date, 'admin')
        return check_response_company_profit(f'Doanh thu công ty {time_text}:', profit)
    elif detect_thau_ngoai(text_full):
        bid_outside = await get_user_outside_bid(from_date, end_date)
        return check_response(f'Thầu ngoài {time_text}:', bid_outside)
    elif detect_super(text_full):
        supers = await get_supers(from_date, end_date)
        tmp_text = text_full.split(' ')
        threshold = 0
        if len(tmp_text) > 0:
            threshold = tmp_text[len(tmp_text)-1]
        return await send_table_image(supers, time_text, 'Cổ Đông', threshold)
    elif detect_master(text_full):
        threshold = 0
        tmp_text = text_full.split(' ')
        if len(tmp_text) > 0:
            threshold = tmp_text[len(tmp_text)-1]
        masters = await get_masters(from_date, end_date)
        return await send_table_image(masters, time_text, 'Tổng Đại Lý', threshold)
    elif detect_agent(text_full):
        threshold = 0
        tmp_text = text_full.split(' ')
        if len(tmp_text) > 0:
            threshold = tmp_text[len(tmp_text)-1]
        agents = await get_agents(from_date, end_date)
        return await send_table_image(agents, time_text, 'Đại Lý', threshold)
    elif detect_member(text_full):
        threshold = 0
        tmp_text = text_full.split(' ')
        if len(tmp_text) > 0:
            threshold = tmp_text[len(tmp_text)-1]
        members = await get_members(from_date, end_date)
        return await send_table_image(members, time_text, 'Hội Viên', threshold)
    else:
        text_full = text_full.split(' ')

        if len(text_full) == 1:
            return 'Không đúng cú pháp. Chúc anh một ngày tốt lành.'

        info = text_full[0].strip().lower()
        processed: str = text.replace(info, '').lower().strip()
        if detect_member_info(processed):
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

            user = await get_user(from_date, end_date, formatted_yesterday, info)
            # user = await get_user(from_date, formatted_yesterday, (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'), info)
            return await send_table_user_image(user)
        elif detect_member_info_os_bet(processed):
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

            user = await get_user_os_bet(end_date, info)
            # user = await get_user(from_date, formatted_yesterday, (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'), info)
            return await send_table_user_os_bet_image(user)
        elif detect_member_info_os_number(processed):
            return 'Không đúng cú pháp. Chúc anh một ngày tốt lành.'
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

            user = await get_user_os_number(end_date, info)
            # user = await get_user(from_date, formatted_yesterday, (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'), info)
            return await send_table_user_os_bet_image(user)
        else:
            return 'Không đúng cú pháp. Chúc anh một ngày tốt lành.'




async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # print('User @'+update.effective_user.username +'['+update.effective_user.first_name+' ' + update.effective_user.last_name+'] in ' + message_type + ": " + text)
    print('Input: ' + text)

    group_white_list = [
        -1002044356915, # hey
        -1002036601443, # loc phat
        -1002109063811 # hau due
    ]

    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name
    full_name = f'{first_name} {last_name}'

    if first_name is None:
        full_name = f'{last_name}'
    elif last_name is None:
        full_name = f'{first_name}'

    message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Anh {full_name} đợi em chút nhé')
    message_id = message_to_delete.message_id

    if message_type == 'supergroup':
        print(chat_id)

        if chat_id in group_white_list:
            if BOT_USER_NAME in text:
                # message_to_delete = await context.bot.send_message(chat_id, 'Đang tổng hợp dữ liệu. Đợi em chút nhé')
                # message_id = message_to_delete.message_id

                text: str = text.replace(BOT_USER_NAME, '').strip()
                # response: str = await handle_response(new_text)
            else:
                print('@' + update.effective_user.username)
                # return

            response: str = await handle_response(text)
        else:
            response: str = "Cút, mày không đủ tuổi nói chuyện với tao."

    else:
        # message_to_delete = await context.bot.send_message(chat_id, 'Đang tổng hợp dữ liệu. Đợi em chút nhé')
        # message_id = message_to_delete.message_id
        print('@' + update.effective_user.username)
        print(f'id: {chat_id}')

        # response: str = await handle_response(text)
        response: str = "Cút, mày không đủ tuổi nói chuyện với tao."

    # response: str = await handle_response(text)

    # print('Bot:', response)

    if '<tr><th>STT.</th><th>Thể loại</th><th>Số</th><th>Điểm</th><th>Tổng</th></tr>' in response:
        pdfkit.from_string(response, f'{message_id}{chat_id}.pdf')
        with open(f'{message_id}{chat_id}.pdf', 'rb') as file:
            await update.message.reply_document(file)

        # Delete the image after sending
        os.remove(f'{message_id}{chat_id}.pdf')
    elif '<html>' in response:
        try:
            imgkit.from_string(response, f'{message_id}{chat_id}.jpg', options=options)
            with open(f'{message_id}{chat_id}.jpg', 'rb') as image:
                await update.message.reply_photo(image)

            # Delete the image after sending
            os.remove(f'{message_id}{chat_id}.jpg')
        except Exception:
            pdfkit.from_string(response, f'{message_id}{chat_id}.pdf')
            with open(f'{message_id}{chat_id}.pdf', 'rb') as file:
                await update.message.reply_document(file)

            # Delete the image after sending
            os.remove(f'{message_id}{chat_id}.pdf')
    elif 'Không đúng cú pháp. Chúc anh một ngày tốt lành.' in response:
        # do nothing
        print('hóng')
    else:
        await update.message.reply_html(response)

    # Delete the message
    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



# Running the scheduler in a separate thread
def schedule_async_job(func, *args):
    print("App running up schedules...")
    asyncio.create_task(func(*args))

async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id='-1002109063811', text='One message every minute')

if __name__ == '__main__':
    print("App starting...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('wl', wl_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("App setting up schedules...")

    # Set up APScheduler
    job_queue = app.job_queue

    # job_minute = job_queue.run_repeating(callback_minute, interval=60, first=10)

    local_timezone = pytz.timezone('Asia/Bangkok')
    target_time_admin_report = time(18, 37, 10, tzinfo=local_timezone)  # Set your time here
    job_daily1 = job_queue.run_daily(send_notification, time=target_time_admin_report)
    target_time_master_report = time(18, 39, 10, tzinfo=local_timezone)  # Set your time here
    job_daily2 = job_queue.run_daily(send_notification_message, time=target_time_master_report)

    print("App running...")

     # Run the bot
    app.run_polling(poll_interval=1)
