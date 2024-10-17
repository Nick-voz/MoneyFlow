from os import getenv


# TODO: the file name should be other, but while autentification.py  in this
# folder, it is not refactored, so it can be there with this name
def get_token() -> str:
    """
    Retrieves the bot token from the environment variables.

    This function looks for the bot token in the environment variable named
    'BOT_TOKEN'. If the token is not found, it raises a RuntimeError

    Returns:
        str: The bot token retrieved from the environment variable.

    Raises:
        RuntimeError: If the 'BOT_TOKEN' environment variable is not set or is None.
    """
    token = getenv("BOT_TOKEN")
    if token is None:
        raise RuntimeError("can not load token from .env")
    return token
