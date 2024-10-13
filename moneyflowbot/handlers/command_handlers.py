from handlers.states import GettingKey
from telegram import Update
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes
from telegram.ext import ConversationHandler
from templates.cancel import text_cancel_conversation
from templates.greeting import text_start
from templates.log_out import text_log_out
from templates.sign_in import text_ask_for_key
from templates.sign_up import text_send_key
from utils.authentication import delete_user
from utils.authentication import genertate_global_user_id


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = text_start()
    await context.bot.send_message(chat_id, text)


async def sign_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    global_user_id = genertate_global_user_id()
    text = text_send_key(global_user_id)
    await context.bot.send_message(chat_id, text)


async def sign_in(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = text_ask_for_key()
    await context.bot.send_message(chat_id, text)
    return GettingKey.getting


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_chat.id
    text = text_cancel_conversation()
    await context.bot.send_message(chat_id, text)
    return ConversationHandler.END


async def log_out(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    try:
        delete_user(chat_id)
        text = text_log_out()
    except Exception:
        print("trouble while deleting", f"{hash(chat_id)=}")
        text = "возникли неожиданный проблемы, мы это исправим"
    await context.bot.send_message(chat_id, text)


handler_start: CommandHandler = CommandHandler("start", start)
handler_sign_up: CommandHandler = CommandHandler("signUp", sign_up)
handler_sign_in: CommandHandler = CommandHandler("signIn", sign_in)
handler_cancel: CommandHandler = CommandHandler("cancel", cancel)
handler_log_out: CommandHandler = CommandHandler("logOut", log_out)


def regester(app: Application) -> None:
    app.add_handlers(
        [
            handler_start,
            handler_sign_up,
            handler_log_out,
            handler_cancel,
        ]
    )
