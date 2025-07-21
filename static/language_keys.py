class LanguageKeys:
    LANG_EN_US = 'en-US'
    LANG_PL = 'pl-PL'

    LANGUAGES = [
        LANG_EN_US,
        LANG_PL
    ]

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @staticmethod
    def get_default() -> str:
        return LanguageKeys.LANG_EN_US

    @staticmethod
    def is_language(lang_key) -> bool:
        return lang_key in LanguageKeys.LANGUAGES
