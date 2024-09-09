import sys

from telethon import TelegramClient
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import EagleClient

def validate_session(session):
    if "==Eagle" and "bot==" in session.lower():
        new_session = session[6:-5]
        return str(new_session)
    else:
        print(f"EAGLEBOT SESSION - Wrong session string!")
        sys.exit()

__version__ = "1.10.6"

loop = None

if Config.EAGLE_STRING:
    session = 
    session = StringSession(str(Config.EAGLE_STRING))
else:
    session = "EagleUserBot"

try:
    eagle = EagleClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"EAGLE_STRING - {e}")
    sys.exit()

eagle.tgbot = tgbot = EagleClient(
    session="EagleTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)
