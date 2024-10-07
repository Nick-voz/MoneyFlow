from os import getenv

import handlers.command_handlers as command_handlers
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder


def get_token() -> str:
    load_dotenv()
    TOKEN = getenv("BOT_TOKEN")
    if TOKEN is None:
        raise RuntimeError
    return TOKEN


if __name__ == "__main__":
    TOKEN = get_token()
    app = ApplicationBuilder().token(TOKEN).build()

    command_handlers.regester(app)

    app.run_polling()
