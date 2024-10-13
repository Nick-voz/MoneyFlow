from handlers.command_handlers import handler_cancel
from handlers.command_handlers import handler_sign_in
from handlers.message_handlers import handler_get_global_key
from handlers.states import GettingKey
from telegram.ext import Application
from telegram.ext import ConversationHandler

sign_in_handler = ConversationHandler(
    entry_points=[
        handler_sign_in,
    ],
    states={
        GettingKey.getting: [
            handler_get_global_key,
        ],
    },
    fallbacks=[
        handler_cancel,
    ],
)


def regester(app: Application) -> None:
    app.add_handler(sign_in_handler)
