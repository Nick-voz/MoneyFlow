import re

from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import ConversationHandler
from telegram.ext import MessageHandler
from telegram.ext import filters

from handlers.states import GettingKey
from templates.sign_in import text_success
from utils.authentication import save_user

UUID_V4_REGEX = (
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b"
)


# TODO: its look bad, should be decompose
async def find_global_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    chat_id = update.effective_chat.id

    res = re.findall(UUID_V4_REGEX, text)
    if len(res) != 1:
        await context.bot.send_message(
            chat_id=chat_id,
            # TODO: rewrite it in templates
            text="не удолось распознать формат ключа, попробуйте еще раз или отправть комманду /cancel чтобы прекратить диалог",
        )
        return GettingKey.getting

    key = res[0]

    try:
        save_user(chat_id, key)
        replay_text = text_success(key)
    except Exception:
        # TODO: rewrite it in templates
        # TODO: there is to ways:
        # (1)key exist (2)and key exist and it is the same as current case,
        # also there is therd way: key exist and it related with ather id,
        # it should be refactor, all case should pracess correct
        replay_text = "У нас уже есть связанный с вами ключ"

    await context.bot.send_message(chat_id, text=replay_text)
    return ConversationHandler.END


handler_get_global_key: MessageHandler = MessageHandler(
    filters.TEXT & ~filters.COMMAND, find_global_key
)
