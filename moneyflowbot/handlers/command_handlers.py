from telegram import Update
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id is None:
        return
    await context.bot.send_message(
        chat_id=chat_id, text="Hellow I'm MoneFlow bot"
    )


start_hendler = CommandHandler("start", start)


def regester(app: Application) -> None:
    app.add_handlers((start_hendler,))
