from pyrogram.types import Message
from config import Config
from pyrogram.errors import RPCError

class SeyanaMessage(Message):
    async def editr(self, text: str, link_preview: bool = True):
        if self.from_user.id == Config.get_user_id():
            await self.edit_text(text, disable_web_page_preview=link_preview)
        else:
            try:
                await self.delete()
            except RPCError:
                pass
            try:
                await self.reply_text(text, quote=True, disable_web_page_preview=link_preview)
            except RPCError:
                pass