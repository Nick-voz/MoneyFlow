from telegram.ext import ApplicationBuilder

from handlers import commands
from handlers import conversations
from utils.utils import get_token

if __name__ == "__main__":
    TOKEN = get_token()

    app = ApplicationBuilder().token(TOKEN).build()

    commands.regester(app)
    conversations.regester(app)

    app.run_polling()
