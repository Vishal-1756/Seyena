from pyrogram import filters, enums, Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
import strings
from ... import bot
from ... import seyena

SPAM = []

async def emoji_convert(query):
     if query==True:
         return "✅"
     elif query==False:
         return "❌"
     elif query==None:
         return "🤷"
     else:
          return "🤔"

@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
     user_id = message.from_user.id
     info = await seyena.get_me()
     name = info.first_name
     id = info.id
     botlive = await emoji_convert(bot.is_connected)
     applive = await emoji_convert(seyena.is_connected)     
     if user_id in SPAM:
         return await message.reply("[`DON'T SPAM HERE`]")
     SPAM.append(user_id)
     await message.forward(Config.LOG_GROUP)
     mention = f"[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("Deploy Your Own Seyena", url=Config.SOURCE),]])
     await message.reply_text(text=strings.BOT_START.format(mention=mention, applive=applive, botlive=botlive),quote=True, reply_markup=BUTTON ,parse_mode=enums.ParseMode.MARKDOWN)
     await asyncio.sleep(20)
     SPAM.remove(user_id)
     return 
