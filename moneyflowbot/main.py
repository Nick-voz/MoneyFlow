from os import getenv

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id is None:
        return
    await context.bot.send_message(
        chat_id=chat_id, text="Hellow I'm MoneFlow bot"
    )


if __name__ == "__main__":
    load_dotenv()
    TOKEN = getenv("BOT_TOKEN")
    if TOKEN is None:
        raise RuntimeError

    app = ApplicationBuilder().token(TOKEN).build()

    start_hendler = CommandHandler("start", start)
    app.add_handler(start_hendler)

    app.run_polling()
