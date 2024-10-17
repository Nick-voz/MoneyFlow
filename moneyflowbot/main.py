from dotenv import load_dotenv
from handlers import commands
from handlers import conversations
from telegram.ext import ApplicationBuilder
from utils.utils import get_token

if __name__ == "__main__":
    load_dotenv()
    TOKEN = get_token()

    app = ApplicationBuilder().token(TOKEN).build()

    commands.regester(app)
    conversations.regester(app)

    app.run_polling()
