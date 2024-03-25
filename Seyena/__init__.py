import json
from .core.client import Seyena
from .core.message import SeyanaMessage
from config import Config
from typing import Any
from functools import wraps
from pyrogram.enums import ChatType
from pyrogram.handlers import MessageHandler
from pyrogram import filters

# Load the JSON file
with open('lang/en.json', 'r') as f:
    lang = json.load(f)

bot = Seyena(
    name="SeyanaBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins={"root": "Seyena.plugins.bot"}
)

seyena = Seyena(
    name="Seyena",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.STRING_SESSION,
    plugins={"root": "Seyena.plugins.user"}
)

class ProSeyena:
    def __init__(self, command, filters: Any | None = None, group:int = 0, sudo: bool = False, super: bool = False, private: bool = False):
        self.command = command
        self.filters = filters
        self.group = group
        self.sudo = sudo
        self.super = super
        self.private = private

    def __call__(self, callback):

        @wraps(callback)
        async def wrapper(client: Seyena, message: SeyanaMessage):
            user_id = message.from_user.id

            if self.private and message.chat.type != ChatType.PRIVATE:
                try:
                    message.editr("This command can be used in private chat only")
                except Exception:
                    pass
                return
            
            if self.super and user_id not in Config.SUPER_USERS:
                try:
                    message.editr("You need to be a super user to perform this task")
                except Exception:
                    pass
                return
            
            if self.sudo and user_id not in Config.SUDO_USERS:
                try:
                    message.editr("You need to be a sudo user to perform this task")
                except Exception:
                    pass
                return
            
            await callback(client, message)
        
        if self.filters != None:
            seyena.add_handler(MessageHandler(wrapper, filters=filters.command(self.command, prefixes=Config.PREFIX) & self.filters), group=self.group)
        else:
            seyena.add_handler(MessageHandler(wrapper, filters=filters.command(self.command, prefixes=Config.PREFIX)), group=self.group)
        return wrapper