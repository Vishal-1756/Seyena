from ... import ProSeyena, Seyena, SeyanaMessage, lang

@ProSeyena(command="alive")
async def alive(client: Seyena, message:SeyanaMessage):
    message.editr(lang["alive"])