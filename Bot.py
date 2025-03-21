from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

TOKEN = "70883226:AAFnuMkcI75el4Tbkey-hVP_z8Jr6pqHTFk"

def start(update: Update, context):
    update.message.reply_text("Привет! Отправь свой заказ.")

def handle_message(update: Update, context):
    message = update.message.text
    update.message.reply_text(f"Ваш заказ: {message}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()￼Enter
