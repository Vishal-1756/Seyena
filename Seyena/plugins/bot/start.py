from pyrogram import filters

from ... import bot


@bot.on_message(filters.command("start"))
async def start(c, m):
    await m.reply_text(f"Hello {m.from_user.mention}")