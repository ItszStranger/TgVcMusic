import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from SoloCloud import LOGGER, app, userbot
from SoloCloud.core.call import AyushSolo
from SoloCloud.misc import sudo
from SoloCloud.plugins import ALL_MODULES
from SoloCloud.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await sudo()
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SoloCloud.plugins" + all_module)
    LOGGER("SoloCloud.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await AyushSolo.start()
    try:
        await AyushSolo.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("SoloCloud").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await AyushSolo.decorators()
    LOGGER("SoloCloud").info(
        "436865656d73204d7573696320426f742053746172746564205375636365737366756c6c792e0a0a446f6e277420666f7267657420746f207669736974202040457175696e6f785f4368617473"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SoloCloud").info("Stopping AnonX Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
