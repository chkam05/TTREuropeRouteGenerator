class LanguageKeys:
    LANG_EN_US = 'en-US'
    LANG_PL = 'pl-PL'

    LANGUAGES = [
        LANG_EN_US,
        LANG_PL
    ]

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @classmethod
    def get_default(cls) -> str:
        return cls.LANG_EN_US

    @classmethod
    def is_language(cls, lang_key) -> bool:
        return lang_key in cls.LANGUAGES
