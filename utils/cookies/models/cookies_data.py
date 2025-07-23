from typing import Optional

from static.language_keys import LanguageKeys


class CookiesData:
    FIELD_LANGUAGE_KEY = 'language'

    def __init__(self, language: Optional[str] = None):
        self._language = language if LanguageKeys.is_language(language) else LanguageKeys.LANG_EN_US

    # region --- PROPERTIES ---

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, value: str):
        self._language = value if LanguageKeys.is_language(value) else LanguageKeys.LANG_EN_US

    # endregion

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'CookiesData':
        return CookiesData(
            language=data.get(cls.FIELD_LANGUAGE_KEY, LanguageKeys.LANG_EN_US)
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_LANGUAGE_KEY: self._language
        }

    # endregion
