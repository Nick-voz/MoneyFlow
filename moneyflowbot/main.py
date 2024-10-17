from os import getenv

from dotenv import load_dotenv
from handlers import command_handlers
from handlers import conversation_handlers
from telegram.ext import ApplicationBuilder


def get_token() -> str:
    token = getenv("BOT_TOKEN")
    if token is None:
        raise RuntimeError("can not load token from .env")
    return token


if __name__ == "__main__":
    load_dotenv()
    TOKEN = get_token()

    app = ApplicationBuilder().token(TOKEN).build()

    command_handlers.regester(app)
    conversation_handlers.regester(app)

    app.run_polling()
