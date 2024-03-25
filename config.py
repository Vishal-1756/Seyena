from os import getenv

class Config:
    API_ID: int = getenv('API_ID')
    API_HASH: str = getenv('API_HASH')
    STRING_SESSION: str = getenv('STRING_SESSION')
    BOT_TOKEN: str = getenv("BOT_TOKEN")
    OWNER_ID: int = getenv("OWNER_ID")
    USER_ID: int = 0
    SUDO_USERS: list = list(map(int, getenv("SUDO_USERS", "").split()))
    LOG_GROUP: int = getenv('LOG_GROUP')
    SUPER_USERS: list = list(map(int, getenv("SUPER_USERS", "").split()))
    PREFIX: list = list(map(int, getenv("PREFIX", "").split()))
    BOT_USERNAME: str = ""
    OWNER_NAME: str = getenv("OWNER_NAME", "root")
    SUPER_USERS.append(OWNER_ID)
    for x in SUPER_USERS:
        SUDO_USERS.append(x)
    
    @classmethod
    def set_user_id(cls, user_id: int):
        cls.USER_ID = user_id

    @classmethod
    def get_user_id(cls):
        return cls.USER_ID

    @classmethod
    def set_bot_username(cls, username: str):
        cls.BOT_USERNAME = username

    @classmethod
    def get_bot_username(cls):
        return cls.BOT_USERNAME    