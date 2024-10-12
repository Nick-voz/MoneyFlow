from os import getenv

import handlers.command_handlers as command_handlers
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder


def get_token() -> str:
    TOKEN = getenv("BOT_TOKEN")
    if TOKEN is None:
        raise RuntimeError("can not load TOKEN from .env")
    return TOKEN


if __name__ == "__main__":
    load_dotenv()
    TOKEN = get_token()
    app = ApplicationBuilder().token(TOKEN).build()

    command_handlers.regester(app)

    app.run_polling()
