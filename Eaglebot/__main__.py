import sys

import Eaglebot
from Eaglebot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import eagle
from .start import killer
from .utils import (
    add_bot_to_logger_group,
    hekp,
    install_externalrepo,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,)
    
LOGS = logging.getLogger("CatUserbot")

print(Eaglebot.__copyright__)
print("𝐿𝑖𝑐𝑒𝑛𝑠𝑒𝑑 𝑈𝑛𝑑𝑒𝑟 𝑇ℎ𝑒 𝑇𝑒𝑟𝑚𝑠 𝑂𝑓 𝑇ℎ𝑒 " + Eaglebot.__license__)
cmdhr = Config.HANDLER

try:
    LOGS.info("Starting Userbot")
    eagle.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    LOGS.info(
        "============================================================================"
    )
    LOGS.info("||               Yay your userbot is officially working.!!!")
    LOGS.info(
        f"||   Congratulation, now type {cmdhr}alive to see message if eagle is live"
    )
    LOGS.info("||   If you need assistance, head to https://t.me/catuserbot_support")
    LOGS.info(
        "============================================================================"
    )
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return


async def externalrepo():
    string = "<b>Your external repo plugins have imported.<b>\n\n"
    if Config.EXTERNAL_REPO:
        data = await install_externalrepo(
            Config.EXTERNAL_REPO, Config.EXTERNAL_REPOBRANCH, "xtraplugins"
        )
        string += f"<b>➜ Repo:  </b><a href='{data[0]}'><b>{data[1]}</b></a>\n<b>     • Imported Plugins:</b>  <code>{data[2]}</code>\n<b>     • Failed to Import:</b>  <code>{', '.join(data[3])}</code>\n\n"
    if Config.VCMODE:
        data = await install_externalrepo(Config.VC_REPO, Config.VC_REPOBRANCH, "catvc")
        string += f"<b>➜ Repo:  </b><a href='{data[0]}'><b>{data[1]}</b></a>\n<b>     • Imported Plugins:</b>  <code>{data[2]}</code>\n<b>     • Failed to Import:</b>  <code>{', '.join(data[3])}</code>\n\n"
    if "Imported Plugins" in string:
        await eagle.tgbot.send_message(BOTLOG_CHATID, string, parse_mode="html")


eagle.loop.run_until_complete(startup_process())

eagle.loop.run_until_complete(externalrepo())

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        eagle.run_until_disconnected()
else:
    eagle.disconnect()
