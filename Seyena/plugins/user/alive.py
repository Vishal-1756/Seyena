from ... import (
    ProSeyena, 
    Seyena, 
    SeyanaMessage, 
    lang
)


@ProSeyena(command="alive")
async def alive(client: Seyena, message: SeyanaMessage) -> SeyanaMessage:
   await message.editr(lang["alive"])
