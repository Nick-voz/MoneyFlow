from os import getenv

from dotenv import load_dotenv

load_dotenv()


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


def get_db_url() -> str:
    """
    Retrieve the database URL from environment variables.

    This function attempts to get the database connection URL from
    the environment variable named "DB_URL". If the environment
    variable is not set, it raises a RuntimeError.

    Returns:
        str: The database connection URL.

    Raises:
        RuntimeError: If the "DB_URL" environment variable is not set.
    """
    db_url = getenv("DB_URL")
    if db_url is None:
        raise RuntimeError("can't load DB_URL")
    return db_url
