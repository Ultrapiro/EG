from asyncio import sleep

from Eaglebot import eagle
from Eaglebot.core.logger import logging

menu_category = "tools"
LOGS = logging.getLogger(__name__)


@eagle.eagle_cmd(
    pattern="sdm (\d*) ([\s\S]*)",
    command=("sdm", menu_category),
    info={
        "header": "To self destruct the message after paticualr time.",
        "description": "Suppose if you use .sdm 10 hi then message will be immediately send new message as hi and then after 10 sec this message will auto delete.`",
        "usage": "{tr}sdm [number] [text]",
        "examples": "{tr}sdm 10 hi",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    eagle = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = eagle[1]
    ttl = int(eagle[0])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()


@eagle.eagle_cmd(
    pattern="selfdm (\d*) ([\s\S]*)",
    command=("selfdm", menu_category),
    info={
        "header": "To self destruct the message after paticualr time. and in message will show the time.",
        "description": "Suppose if you use .sdm 10 hi then message will be immediately will send new message as hi and then after 10 sec this message will auto delete.",
        "usage": "{tr}selfdm [number] [text]",
        "examples": "{tr}selfdm 10 hi",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    eagle = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = eagle[1]
    ttl = int(eagle[0])
    text = message + f"\n\n`This message shall be self-destructed in {ttl} seconds`"

    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(ttl)
    await smsg.delete()