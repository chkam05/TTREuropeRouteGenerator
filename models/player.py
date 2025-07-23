class Player:
    FIELD_NICKNAME_KEY = 'nickname'
    FIELD_MD5_PASSWORD_KEY = 'md5_password'

    def __init__(self, nickname: str, md5_password: str):
        self.nickname = nickname
        self.md5_password = md5_password

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'Player':
        return cls(
            nickname=data.get(cls.FIELD_NICKNAME_KEY),
            md5_password=data.get(cls.FIELD_MD5_PASSWORD_KEY)
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_NICKNAME_KEY: self.nickname,
            self.FIELD_MD5_PASSWORD_KEY: self.md5_password
        }

    # endregion
