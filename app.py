# import everything
import asyncio
from datetime import datetime, timedelta
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from worker import get_user_data

TOKEN: Final = '6695572072:AAGxx6Rn8wyTshwhFfOnfSY6AKfhSvJIa6o'
BOT_USER_NAME: Final = '@em_than_tai_bot'

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
    text_full = text.replace(':', '')
    text_full = text_full.split(' ')

    if len(text_full) == 1:
        return 'Sai cú pháp. Cú pháp mẫu:\n\nvip111 thang thua hom nay\n\nhoặc\n\nvip111 thắng thua hôm nay'

    info = text_full[0].strip()
    processed: str = text.replace(info, '').lower().strip()
    if ('thang thua hom nay' in processed or 'thắng thua hôm nay' in processed):
        from_date = datetime.now().strftime('%Y-%m-%d')
        end_date = from_date

        profit = await get_user_data(from_date=from_date, end_date=end_date, user_code=info, user_name=info)
        if (profit == "***"):
            return "Không tìm thấy thông tin tài khoản. Vui lòng kiểm tra lại"

        formatted_number = "{:,}".format(profit)

        return f'Thắng thua hôm nay: {formatted_number}'
    if 'thang thua hom qua' in processed or 'thắng thua hôm qua' in processed:
        yesterday = datetime.now() - timedelta(days=1)
        formatted_yesterday = yesterday.strftime('%Y-%m-%d')
        from_date = formatted_yesterday
        end_date = formatted_yesterday

        profit = await get_user_data(from_date=from_date, end_date=end_date, user_code=info, user_name=info)

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

        profit = await get_user_data(from_date=from_date, end_date=end_date, user_code=info, user_name=info)

        if (profit == "***"):
            return "Không tìm thấy thông tin tài khoản. Vui lòng kiểm tra lại"

        formatted_number = "{:,}".format(profit)

        return f'Thắng thua tuần này: {formatted_number}'
    else:
        return 'Sai cú pháp. Cú pháp mẫu:\n\nvip111: thang thua hom nay\n\nhoặc\n\nvip111: thắng thua hôm nay'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User @{update.effective_user.username}[{update.effective_user.first_name} {update.effective_user.last_name}] in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USER_NAME in text:
            new_text: str = text.replace(BOT_USER_NAME, '').strip()
            response: str = await handle_response(new_text)
        else:
            return
    else:
        response: str = await handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


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

    app.run_polling(poll_interval=3)
