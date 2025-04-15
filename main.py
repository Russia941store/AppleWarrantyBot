# main.py

from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import bot_token
from handlers import start, handle_callback

def main():
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))

    print("🤖 Бот запущен. Ожидаю команды в Telegram...")
    app.run_polling()

if __name__ == "__main__":
    main()