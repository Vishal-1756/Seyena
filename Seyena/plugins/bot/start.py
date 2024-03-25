from ... import bot
from pyrogram import filters

@bot.on_message(filters.command("start"))
async def start(c,m):
    m.reply_text("Hello")