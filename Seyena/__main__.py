import asyncio, logging, platform, importlib
from pyrogram import idle
from . import bot, seyena, lang
from config import Config
from .constants.symbols import Symbols
from .plugins.bot import BOT_MODULES
from .plugins.user import USER_MODULES

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s.%(funcName)s | %(levelname)s | %(message)s",
    datefmt="[%X]",
)

# To avoid some annoying log
logging.getLogger("pyrogram.syncer").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

try:
    import uvloop
    uvloop.install()
except ImportError:
    if platform.system() != "Windows":
        logger.warning("uvloop is not installed and therefore will be disabled.")

async def main():
    for x in BOT_MODULES:
        importlib.import_module("Seyena.plugins.bot." + x)
    for y in USER_MODULES:
        importlib.import_module("Seyena.plugins.user." + y)
    try:
        await seyena.start()
        await bot.start()
        logger.info(Config.LOG_GROUP)
        await seyena.send_message(
            chat_id= Config.LOG_GROUP,
            text="started"
        )
        await idle()

    except KeyboardInterrupt:
        logger.warning("Forced stop… Bye!")

    except Exception as err:
        logger.error(err)
    

    
if __name__ == "__main__":
    event_policy = asyncio.get_event_loop_policy()
    event_loop = event_policy.new_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(main())
    event_loop.close()