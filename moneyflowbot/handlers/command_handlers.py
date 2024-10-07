from telegram import Update
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes

from moneyflowbot.utils.authentication import genertate_global_user_id


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id is None:
        return
    await context.bot.send_message(
        chat_id=chat_id, text="Hellow I'm MoneFlow bot"
    )


async def sign_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id is None:
        return

    global_user_id = genertate_global_user_id()

    # TODO: it mastu be implement by templates
    text = "это твой ключ, который понадобится в бодущем для доступа к данным, это ключ мы не сохраняем, помни что при его утере твои данны будут навсегда утерены."
    text += "\n" + " - " + global_user_id
    await context.bot.send_message(chat_id=chat_id, text=text)


start_hendler = CommandHandler("start", start)


def regester(app: Application) -> None:
    app.add_handlers((start_hendler,))
