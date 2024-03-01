# import everything
import asyncio
import os
import random
import imgkit, pdfkit
from datetime import datetime, timedelta, time
from typing import Final
import pytz
from bs4 import BeautifulSoup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
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
    'quality': '60',
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
def check_time_and_send_notification():
    # Đặt múi giờ nếu cần
    timezone = pytz.timezone('Asia/Bangkok')
    now = datetime.now(timezone)

    current_hour = now.hour
    current_minute = now.minute

    # Kiểm tra xem thời gian hiện tại có nằm trong khoảng từ 18:32 đến 18:37 không
    if current_hour == 18 and 32 <= current_minute <= 40:
        return True
    
    return False
      # Hàm để gửi thông báo qua Telegram Bot

async def handle_response(context: ContextTypes.DEFAULT_TYPE, chat_id: int, full_name: str, text: str) -> str:
    message_id = ''

    text_full = text.replace(':', '').strip()

    is_last_week = False

    today = datetime.now()
    # Calculate the number of days to subtract to get to Monday
    # weekday() returns 0 for Monday, 1 for Tuesday, and so on
    days_to_subtract = today.weekday()
    monday = today - timedelta(days=days_to_subtract)
    formatted_monday = monday.strftime('%Y-%m-%d')
    from_date = formatted_monday
    end_date = datetime.now().strftime('%Y-%m-%d')

    time_text = 'tuần này'
    report_date = datetime.now().strftime('%Y-%m-%d')
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
    elif detect_last_week(text_full):
        time_text = 'tuần trước'
        today = datetime.now()
        # Calculate last Monday and Sunday
        last_monday = today - timedelta(days=(today.weekday() + 7) % 7) - timedelta(days=7)
        from_date = last_monday.strftime('%Y-%m-%d')
        end_date = (last_monday + timedelta(days=6)).strftime('%Y-%m-%d')
        report_date = from_date

        is_last_week = True

    # call api
    if detect_report_xsmb(text_full):
        message_to_delete = await context.bot.send_message(chat_id, f'Đang lấy dữ liệu. Sếp {full_name} đợi em chút nhé')
        message_id = message_to_delete.message_id
        
        report = await get_report_xsmb()
        return report, message_id
    
    elif detect_guide(text_full):
        message_to_delete = await context.bot.send_message(chat_id, f'Đang lấy dữ liệu. Sếp {full_name} đợi em chút nhé')
        message_id = message_to_delete.message_id

        guide = get_guide()
        return guide, message_id
    
    elif detect_guide_report_list(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        report = await get_list_report_info(report_date)
        return await send_table_report_list(report), message_id
    
    elif detect_member_inactive(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        members = await get_members_inactive(from_date, end_date)
        return await send_member_inactive(members, time_text), message_id

    elif detect_os_cong_ty(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id
    
        date = datetime.now().strftime('%Y-%m-%d')
        os = await get_user_os(date, date, 'admin')
        return check_response(f'Outstanding hôm nay:', os), message_id
    elif detect_os_super(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id
        
        supers = await get_supers(from_date, end_date)
        return await send_table_os_image(supers, 'Cổ Đông'), message_id
    elif detect_os_master(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        masters = await get_masters(from_date, end_date)
        return await send_table_os_image(masters, 'Tổng Đại Lý'), message_id
    elif detect_os_agent(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        agents = await get_agents(from_date, end_date)
        return await send_table_os_image(agents, 'Đại Lý'), message_id
    elif detect_os_member(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        members = await get_members(from_date, end_date)
        return await send_table_os_image(members, 'Hội Viên'), message_id
    elif detect_doanh_thu_cong_ty(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        profit = await get_user_profit(from_date, end_date, 'admin')
        return check_response_company_profit(f'Doanh thu công ty {time_text}:', profit), message_id
    elif detect_thau_ngoai(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        bid_outside = await get_user_outside_bid(from_date, end_date)
        return check_response(f'Thầu ngoài {time_text}:', bid_outside), message_id
    elif detect_super(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        supers = await get_supers(from_date, end_date)
        tmp_text = text_full.split(' ')
        threshold = 0
        if len(tmp_text) > 0:
            threshold = tmp_text[len(tmp_text)-1]
        return await send_table_image(supers, time_text, 'Cổ Đông', threshold), message_id
    elif detect_master(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        threshold = 0
        tmp_text = text_full.split(' ')
        if len(tmp_text) > 0:
            threshold = tmp_text[len(tmp_text)-1]
        masters = await get_masters(from_date, end_date)
        return await send_table_image(masters, time_text, 'Tổng Đại Lý', threshold), message_id
    elif detect_agent(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        threshold = 0
        tmp_text = text_full.split(' ')
        if len(tmp_text) > 0:
            threshold = tmp_text[len(tmp_text)-1]
        agents = await get_agents(from_date, end_date)
        return await send_table_image(agents, time_text, 'Đại Lý', threshold), message_id
    elif detect_member(text_full):
        if check_time_and_send_notification():
            return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
        else:
            message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
            message_id = message_to_delete.message_id

        threshold = 0
        tmp_text = text_full.split(' ')
        if len(tmp_text) > 0:
            threshold = tmp_text[len(tmp_text)-1]
        members = await get_members(from_date, end_date)
        return await send_table_image(members, time_text, 'Hội Viên', threshold), message_id
    else:
        text_full = text_full.split(' ')

        if len(text_full) == 1:
            return 'Không đúng cú pháp. Chúc anh một ngày tốt lành.', ''

        info = text_full[0].strip().lower()
        processed: str = text.replace(info, '').lower().strip()

        if detect_member_info_last_week(processed):
            if check_time_and_send_notification():
                return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
            else:
                message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
                message_id = message_to_delete.message_id
            
            user = await get_user_last_week(info)
        
            return await send_table_user_image(user), message_id
        elif detect_member_info_tet(processed):
            if check_time_and_send_notification():
                return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
            else:
                message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
                message_id = message_to_delete.message_id

            user = await get_user_tet(info)
            # user = await get_user(from_date, formatted_yesterday, (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'), info)
            return await send_table_user_image(user), message_id
        elif detect_member_info(processed):
            if check_time_and_send_notification():
                return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
            else:
                message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
                message_id = message_to_delete.message_id

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
            return await send_table_user_image(user), message_id
        
        elif detect_report_super_tet(processed):
            if check_time_and_send_notification():
                return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
            else:
                message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
                message_id = message_to_delete.message_id
            
            report = await get_report_super_tet(datetime.now().strftime('%Y-%m-%d'), info)

            return await send_table_report_super_image(report), message_id
        
        elif detect_report_super(processed):
            if check_time_and_send_notification():
                return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
            else:
                message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
                message_id = message_to_delete.message_id
            
            report = await get_report_super(report_date, info, is_last_week)

            return await send_table_report_super_image(report), message_id


        elif detect_member_info_os_bet(processed):
            if check_time_and_send_notification():
                return 'Đang tính toán dữ liệu hôm nay. Sếp vui lòng nhắn sau 18:41 nhé ạ.', ''
            else:
                message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
                message_id = message_to_delete.message_id


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
            return await send_table_user_os_bet_image(user), message_id
        elif detect_member_info_os_number(processed):
            return 'Không đúng cú pháp. Chúc anh một ngày tốt lành.', ''
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
            return 'Không đúng cú pháp. Chúc anh một ngày tốt lành.', ''


async def on_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the callback data as a dict
    callback_data = str(update.callback_query.data)

    chat_id = update.effective_chat.id

    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name
    full_name = f'{first_name} {last_name}'
    

    if first_name is None:
        full_name = f'{last_name}'
    elif last_name is None:
        full_name = f'{first_name}'


    print('callback_data: ' + callback_data)

    if callback_data != '***':
        button = [[InlineKeyboardButton("Xem Outstanding Super tuần này", callback_data='super tuần này')]]

        if 'os super' in callback_data.lower():
            button = [[InlineKeyboardButton("Xem Outstanding Master hôm nay", callback_data='os master')]]
        elif 'os master' in callback_data.lower():
                button = [[InlineKeyboardButton("Xem Outstanding Agent hôm nay", callback_data='os agent')]]
        elif 'os agent' in callback_data.lower():
                button = [[InlineKeyboardButton("Xem Outstanding Member hôm nay", callback_data='os member')]]

        # elif 'wl' in callback_data.lower():
        #     tmp = callback_data.split('-')
        #     role = tmp[1].lower()
        #     time_text = tmp[2].lower()

        #     if role == 'cổ đông':
        #         button = [[InlineKeyboardButton(f"Xem thắng thua Master {time_text}", callback_data=f'os master {time_text}')]]
        #     elif role == 'tổng đại lý':
        #         button = [[InlineKeyboardButton(f"Xem thắng thua Agent {time_text}", callback_data=f'os agent {time_text}')]]
        #     elif role == 'đại lý':
        #         button = [[InlineKeyboardButton(f"Xem thắng thua Member {time_text}", callback_data=f'os member {time_text}')]]
        
        reply_markup = InlineKeyboardMarkup(button)
       



    response, message_id = await handle_response(context, chat_id, full_name, str(callback_data))

    if '<tr><th>STT.</th><th>Thể loại</th><th>Số</th><th>Điểm</th><th>Tiền</th><th>Trả thưởng</th><th>Lợi nhuận</th></tr>' in response:
        pdfkit.from_string(response, f'{message_id}{chat_id}.pdf')
        with open(f'{message_id}{chat_id}.pdf', 'rb') as file:
            await app.bot.send_document(chat_id=chat_id, document=file)

        # Delete the image after sending
        os.remove(f'{message_id}{chat_id}.pdf')
    elif '<html>' in response:
        try:
            imgkit.from_string(response, f'{message_id}{chat_id}.jpg', options=options)
            with open(f'{message_id}{chat_id}.jpg', 'rb') as image:
                await app.bot.send_photo(chat_id=chat_id, photo=image)

            # Delete the image after sending
            os.remove(f'{message_id}{chat_id}.jpg')
        except Exception as e:
            print(f'Error: {e}')
            pdfkit.from_string(response, f'{message_id}{chat_id}.pdf')
            with open(f'{message_id}{chat_id}.pdf', 'rb') as file:
                await app.bot.send_document(chat_id=chat_id, document=file)

            # Delete the image after sending
            os.remove(f'{message_id}{chat_id}.pdf')
                
    elif 'Không đúng cú pháp. Chúc anh một ngày tốt lành.' in response:
        # do nothing
        print('hóng')
    else:
        await app.bot.send_message(chat_id=chat_id, text=response)

    if message_id != '':
        # Delete the message
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

    
    # await app.bot.send_message(chat_id=update.callback_query.message.chat_id, text=callback_data.data)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # print('User @'+update.effective_user.username +'['+update.effective_user.first_name+' ' + update.effective_user.last_name+'] in ' + message_type + ": " + text)
    print('Input: ' + text)

    group_white_list = [
        -1002044356915, # hey
        -1002036601443, # loc phat
        -1002109063811, # hau due
        -4115120908, # Nghiện Lô Đề
    ]

    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name
    full_name = f'{first_name} {last_name}'

    if first_name is None:
        full_name = f'{last_name}'
    elif last_name is None:
        full_name = f'{first_name}'

    # message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Sếp {full_name} đợi em chút nhé')
    message_id = ''

    if message_type == 'supergroup' or message_type == 'group':
        print(chat_id)

        if chat_id in group_white_list:
            if BOT_USER_NAME in text:
                # message_to_delete = await context.bot.send_message(chat_id, 'Đang tổng hợp dữ liệu. Đợi em chút nhé')
                # message_id = message_to_delete.message_id

                text: str = text.replace(BOT_USER_NAME, '').strip()
                # response: str = await handle_response(new_text)
            else:
                print('@' + str(update.effective_user.username))
                # return

            response, message_id = await handle_response(context, chat_id, full_name, text)
        else:
            response: str = "Cút, mày không đủ tuổi nói chuyện với tao."

    else:
        # message_to_delete = await context.bot.send_message(chat_id, 'Đang tổng hợp dữ liệu. Đợi em chút nhé')
        # message_id = message_to_delete.message_id
        print('@' + str(update.effective_user.username))
        print(f'id: {chat_id}')

        # response: str = await handle_response(text)
        response: str = "Cút, mày không đủ tuổi nói chuyện với tao."

    # response: str = await handle_response(text)

    # print('Bot:', response)

    if '<tr><th>STT.</th><th>Thể loại</th><th>Số</th><th>Điểm</th><th>Tiền</th><th>Trả thưởng</th><th>Lợi nhuận</th></tr>' in response or '<title>pdf</title>' in response:
        pdfkit.from_string(response, f'{message_id}{chat_id}.pdf')
        with open(f'{message_id}{chat_id}.pdf', 'rb') as file:
            await update.message.reply_document(file)

        # Delete the image after sending
        os.remove(f'{message_id}{chat_id}.pdf')
    elif '<html>' in response:
        soup = BeautifulSoup(response, 'html.parser')
        title_text = soup.title.string if soup.title else '***'
        button = [[InlineKeyboardButton("Xem thắng thua Super tuần này", callback_data='super tuần này')]]

        if title_text != '***':
            button = [[InlineKeyboardButton("Xem thắng thua Super tuần này", callback_data='super tuần này')]]

            if 'os' in title_text.lower():
                tmp = title_text.split('-')
                role = tmp[1].lower()

                if role == 'cổ đông':
                    button = [[InlineKeyboardButton("Xem Outstanding Master hôm nay", callback_data='os master')]]
                elif role == 'tổng đại lý':
                    button = [[InlineKeyboardButton("Xem Outstanding Agent hôm nay", callback_data='os agent')]]
                elif role == 'đại lý':
                    button = [[InlineKeyboardButton("Xem Outstanding Member hôm nay", callback_data='os member')]]

            elif 'wl' in title_text.lower():
                tmp = title_text.split('-')
                role = tmp[1].lower()
                time_text = tmp[2].lower()

                if role == 'cổ đông':
                    button = [[InlineKeyboardButton(f"Xem thắng thua Master {time_text}", callback_data=f'os master {time_text}')]]
                elif role == 'tổng đại lý':
                    button = [[InlineKeyboardButton(f"Xem thắng thua Agent {time_text}", callback_data=f'os agent {time_text}')]]
                elif role == 'đại lý':
                    button = [[InlineKeyboardButton(f"Xem thắng thua Member {time_text}", callback_data=f'os member {time_text}')]]
        
        
        reply_markup = InlineKeyboardMarkup(button)
        try:
            imgkit.from_string(response, f'{message_id}{chat_id}.jpg', options=options)
            with open(f'{message_id}{chat_id}.jpg', 'rb') as image:
                await update.message.reply_photo(image)

            # Delete the image after sending
            os.remove(f'{message_id}{chat_id}.jpg')
        except Exception as e:
            print(f'Error: {e}')
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

    if message_id != '':
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

     # Set the callback handler
    app.add_handler(CallbackQueryHandler(on_callback_query))

    # app.add_error_handler(error)

    print("App setting up schedules...")

    # Set up APScheduler
    job_queue = app.job_queue

    # job_minute = job_queue.run_repeating(callback_minute, interval=60, first=10)

    local_timezone = pytz.timezone('Asia/Bangkok')
    target_time_admin_report = time(18, 38, 10, tzinfo=local_timezone)  # Set your time here
    job_daily1 = job_queue.run_daily(send_notification, time=target_time_admin_report)

    second = random.randint(1, 59)
    target_time_master_report = time(18, 39, second, tzinfo=local_timezone)  # Set your time here
    job_daily2 = job_queue.run_daily(send_notification_message, time=target_time_master_report)

    print("App for Admin running...")

     # Run the bot
    app.run_polling(poll_interval=1)
