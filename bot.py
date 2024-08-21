from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')


async def start(update: Update, context) -> None:
    await update.message.reply_text('Halo! Saya bot Telegram Anda.')


async def help_command(update: Update, context) -> None:
    await update.message.reply_text('Gunakan /start untuk memulai dan /help untuk bantuan.')


async def echo(update: Update, context) -> None:
    await update.message.reply_text(update.message.text)


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()


if __name__ == '__main__':
    main()
