from telegram import Update
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes
from utils.authentication import genertate_global_user_id
from utils.authentication import get_global_user_id
from utils.authentication import save_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id=chat_id, text="Hellow I'm MoneyFlow bot"
    )


async def sign_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    try:
        global_user_id = get_global_user_id(chat_id)
        await context.bot.send_message(
            chat_id, text=f"your key is {global_user_id}"
        )
    except Exception as e:
        global_user_id = None
        print(e)
        pass

    global_user_id = global_user_id or genertate_global_user_id()

    # TODO: it mastu be implement by templates
    text = "это твой ключ, который понадобится в бодущем для доступа к данным, это ключ мы не сохраняем, помни что при его утере твои данны будут навсегда утерены."
    text += "\n" + " - " + global_user_id

    save_user(chat_id=chat_id, global_user_id=global_user_id)
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
