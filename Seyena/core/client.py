import time
from pyrogram import Client
from pyrogram.enums.parse_mode import ParseMode
from config import Config

class Seyena(Client):
    def __init__(self, name: str, api_id: int | str = None, api_hash: str = None, bot_token: str = None, session_string: str = None, plugins: dict = None, user:bool=True):
        self.user = user
        if self.user is True:
            super().__init__(
                name=name,
                api_id=api_id,
                api_hash=api_hash,
                session_string=session_string,
                parse_mode=ParseMode.DEFAULT,
                sleep_threshold=20,
                plugins=plugins
            )
        else:
            super().__init__(
                name=name,
                api_id=api_id,
                api_hash=api_hash,
                parse_mode=ParseMode.DEFAULT,
                sleep_threshold=20,
                bot_token=bot_token,
                plugins=plugins
            )

    async def start(self):
        pro = await super().start()
        self.start_time = time.time()
        user = await pro.get_me()
        if self.user is True:
            Config.set_user_id(user.id)
        else:
            Config.set_bot_username(user.username)

    async def stop(self):
        await super().stop()