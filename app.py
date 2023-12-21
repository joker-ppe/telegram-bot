# import everything
import asyncio
import prettytable as pt
from datetime import datetime, timedelta
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from worker import *

TOKEN: Final = '6695572072:AAGxx6Rn8wyTshwhFfOnfSY6AKfhSvJIa6o'
BOT_USER_NAME: Final = '@em_loc_phat_bot'

# Command


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, Em là Thần Tài đây')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('ok okokokok')


async def wl_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await get_list_users_data()
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
    if 'hôm nay' in text_full.lower() or 'hom nay' in text_full.lower() or 'hnay' in text_full.lower():
        # do nothing
        from_date = datetime.now().strftime('%Y-%m-%d')
        end_date = from_date
        time_text = 'hôm nay'
    elif 'hôm qua' in text_full.lower() or 'hom qua' in text_full.lower() or 'hqa' in text_full.lower() or 'hqua' in text_full.lower():
        yesterday = datetime.now() - timedelta(days=1)
        formatted_yesterday = yesterday.strftime('%Y-%m-%d')
        from_date = formatted_yesterday
        end_date = formatted_yesterday
        time_text = 'hôm qua'
    elif 'tuần này' in text_full.lower() or 'tuan nay' in text_full.lower():
        time_text = 'tuần này'

    # call api
    if 'os công ty' in text_full.lower() or 'outstanding công ty' in text_full.lower() or 'os cong ty' in text_full.lower() or 'os cty' in text_full.lower():
        date = datetime.now().strftime('%Y-%m-%d')
        os = await get_user_os(date, date, 'admin')
        return check_response(f'Outstanding hôm nay:', os)
    elif 'os cổ đông' in text_full.lower() or 'os co dong' in text_full.lower() or 'os cd' in text_full.lower() or 'os super' in text_full.lower():
        supers = await get_supers(from_date, end_date)
        return await send_table_os(supers, 'Cổ Đông')
    elif 'os tổng đại lý' in text_full.lower() or 'os tong dai ly' in text_full.lower() or 'os tong dl' in text_full.lower() or 'os master' in text_full.lower():
        masters = await get_masters(from_date, end_date)
        return await send_table_os(masters, 'Tổng Đại Lý')
    elif 'os đại lý' in text_full.lower() or 'os dai ly' in text_full.lower() or 'os dly' in text_full.lower() or 'os agent' in text_full.lower():
        agents = await get_agents(from_date, end_date)
        return await send_table_os(agents, 'Đại Lý')
    elif 'os hội viên' in text_full.lower() or 'os hoi vien' in text_full.lower() or 'os hv' in text_full.lower() or 'os member' in text_full.lower():
        members = await get_members(from_date, end_date)
        return await send_table_os(members, 'Hội Viên')
    elif 'doanh thu công ty' in text_full.lower() or 'doanh thu cty' in text_full.lower() or 'doanh thu cong ty' in text_full.lower():
        profit = await get_user_profit(from_date, end_date, 'admin')
        return check_response_company_profit(f'Doanh thu công ty {time_text}:', profit)
    elif 'thầu ngoài' in text_full.lower() or 'thau ngoai' in text_full.lower() or 'tn' in text_full.lower():
        bid_outside = await get_user_outside_bid(from_date, end_date)
        return check_response(f'Thầu ngoài {time_text}:', bid_outside)
    elif 'cổ đông' in text_full.lower() or 'co dong' in text_full.lower() or 'cd' in text_full.lower() or 'super' in text_full.lower():
        supers = await get_supers(from_date, end_date)
        return await send_table(supers, time_text, 'Cổ Đông')
    elif 'tổng đại lý' in text_full.lower() or 'tong dai ly' in text_full.lower() or 'tong dl' in text_full.lower() or 'master' in text_full.lower():
        masters = await get_masters(from_date, end_date)
        return await send_table(masters, time_text, 'Tổng Đại Lý')
    elif 'đại lý' in text_full.lower() or 'dai ly' in text_full.lower() or 'dl' in text_full.lower() or 'dly' in text_full.lower() or 'agent' in text_full.lower():
        agents = await get_agents(from_date, end_date)
        return await send_table(agents, time_text, 'Đại Lý')
    elif 'hội viên' in text_full.lower() or 'hoi vien' in text_full.lower() or 'hv' in text_full.lower() or 'member' in text_full.lower():
        members = await get_members(from_date, end_date)
        return await send_table(members, time_text, 'Hội Viên')
    else:
        text_full = text_full.split(' ')

        if len(text_full) == 1:
            return 'Không đúng cú pháp. Chúc anh một ngày tốt lành.'

        info = text_full[0].strip()
        processed: str = text.replace(info, '').lower().strip()
        if ('thang thua hom nay' in processed or 'thắng thua hôm nay' in processed):
            from_date = datetime.now().strftime('%Y-%m-%d')
            end_date = from_date

            profit = await get_user_data(from_date=from_date, end_date=end_date, user_name=info)
            if (profit == "***"):
                return "Không tìm thấy thông tin tài khoản. Vui lòng kiểm tra lại"

            formatted_number = "{:,}".format(profit)

            return f'Thắng thua hôm nay: {formatted_number}'
        if 'thang thua hom qua' in processed or 'thắng thua hôm qua' in processed:
            yesterday = datetime.now() - timedelta(days=1)
            formatted_yesterday = yesterday.strftime('%Y-%m-%d')
            from_date = formatted_yesterday
            end_date = formatted_yesterday

            profit = await get_user_data(from_date=from_date, end_date=end_date, user_name=info)

            if (profit == "***"):
                return "Không tìm thấy thông tin tài khoản. Vui lòng kiểm tra lại"

            formatted_number = "{:,}".format(profit)

            return f'Thắng thua hôm qua: {formatted_number}'
        if 'thang thua tuan nay' in processed or 'thắng thua tuần này' in processed:
            today = datetime.now()
            # Calculate the number of days to subtract to get to Monday
            # weekday() returns 0 for Monday, 1 for Tuesday, and so on
            days_to_subtract = today.weekday()
            monday = today - timedelta(days=days_to_subtract)
            formatted_monday = monday.strftime('%Y-%m-%d')
            from_date = formatted_monday
            end_date = datetime.now().strftime('%Y-%m-%d')

            profit = await get_user_data(from_date=from_date, end_date=end_date, user_name=info)

            if (profit == "***"):
                return "Không tìm thấy thông tin tài khoản. Vui lòng kiểm tra lại"

            formatted_number = "{:,}".format(profit)

            return f'Thắng thua tuần này: {formatted_number}'
        else:
            return 'Không đúng cú pháp. Chúc anh một ngày tốt lành.'


async def send_table(json_data, time_text, role='Cổ Đông'):
    table = pt.PrettyTable(['STT.', role, 'Thắng thua'])
    table.title = f'Báo cáo {role} {time_text}'
    table.align['STT.'] = 'l'
    table.align[role] = 'l'
    table.align['Thắng thua'] = 'r'

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    # print(json_data)

    data = [(item["full_name"], item["profit"])
            for item in json_data]

    # print(data)

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    data = sorted(data, key=lambda x: x[1], reverse=True)

    total = sum(int(item[1]) for item in data)

    for index, (full_name, profit) in enumerate(data, start=1):
        table.add_row([index, full_name, "{:,}".format(round(profit))])

    table.add_row(['------', '-----------', '-----------'])
    table.add_row(['***', 'Tổng', "{:,}".format(round(total))])

    return f'<pre>{table}</pre>'


async def send_table_os(json_data, role='Cổ Đông'):
    table = pt.PrettyTable(['STT.', role, 'Outstanding'])
    table.title = f'Báo cáo Outstanding {role}'
    table.align['STT.'] = 'l'
    table.align[role] = 'l'
    table.align['Outstanding'] = 'r'

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    data = [(item["full_name"], item["outstanding"])
            for item in json_data]

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    data = sorted(data, key=lambda x: x[1], reverse=True)

    total = sum(int(item[1]) for item in data)

    for index, (full_name, outstanding) in enumerate(data, start=1):
        table.add_row([index, full_name, "{:,}".format(round(outstanding))])

    table.add_row(['------', '-----------', '-----------'])
    table.add_row(['***', 'Tổng', "{:,}".format(round(total))])

    return f'<pre>{table}</pre>'

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)


def check_response(message, response):
    if (response == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    formatted_number = "{:,}".format(round(response))
    return f'{message} {formatted_number}'


def check_response_company_profit(message, response):
    if (response == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    formatted_number = "{:,}".format(round(int(response) * (-1) * 20 / 100))
    return f'{message} {formatted_number}'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # print('User @'+update.effective_user.username +'['+update.effective_user.first_name+' ' + update.effective_user.last_name+'] in ' + message_type + ": " + text)
    print('Input: ' + text)

    group_white_list = [
        -1002044356915,
        -1002036601443
    ]

    message_to_delete = await context.bot.send_message(chat_id, f'Đang tổng hợp dữ liệu. Anh {update.effective_user.first_name} {update.effective_user.last_name} đợi em chút nhé')
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

        # response: str = await handle_response(text)
        response: str = "Cút, mày không đủ tuổi nói chuyện với tao."

    # response: str = await handle_response(text)

    print('Bot:', response)
    await update.message.reply_html(response)

    # Delete the message
    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print("App starting...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('wl', wl_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("App running...")

    app.run_polling(poll_interval=1)
