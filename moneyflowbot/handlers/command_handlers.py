from telegram import Update
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes
from templates.greeting import text_greeting
from templates.sign_up import text_send_key
from utils.authentication import genertate_global_user_id


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = text_greeting()
    await context.bot.send_message(chat_id=chat_id, text=text)


async def sign_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    global_user_id = genertate_global_user_id()
    text = text_send_key(global_user_id)

    await context.bot.send_message(chat_id=chat_id, text=text)


start_hendler = CommandHandler("start", start)
sign_up_handler = CommandHandler("signUp", sign_up)


def regester(app: Application) -> None:
    app.add_handlers(
        [
            start_hendler,
            sign_up_handler,
        ]
    )
