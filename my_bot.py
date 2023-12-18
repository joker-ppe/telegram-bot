from telegram.ext import Updater, CommandHandler

TOKEN = '6695572072:AAGxx6Rn8wyTshwhFfOnfSY6AKfhSvJIa6o'


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Hello! I am your bot.")


def main():
    updater = Updater("YOUR_TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
