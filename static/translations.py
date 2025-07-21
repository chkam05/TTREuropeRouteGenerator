from typing import Optional

from static.error_keys import ErrorKeys
from static.language_keys import LanguageKeys


class Translations:

    ERRORS = {
        LanguageKeys.LANG_EN_US: {
            ErrorKeys.ERROR_GAME_EXISTS: 'Game with name \"{0}\" already exists.',
            ErrorKeys.ERROR_GAME_NOT_EXISTS: 'Game with name \"{0}\" does not exists.',
            ErrorKeys.ERROR_MISSING_DATA: 'Application data container not loaded.',
            ErrorKeys.ERROR_MISSING_GAME_NAME: 'Missing \"Game Name\".',
            ErrorKeys.ERROR_MISSING_NICKNAME: 'Missing \"Nickname\".'
        }
    }

    LANGUAGES = {
        LanguageKeys.LANG_EN_US: {
            LanguageKeys.LANG_EN_US: 'English United-States',
            LanguageKeys.LANG_PL: 'Polish'
        },
    }

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @staticmethod
    def _format(template: str, *args) -> str:
        if not args:
            return template

        if any(f'{{{i}}}' in template for i in range(len(args))):
            return template.format(*args)

        return template

    @staticmethod
    def get_error(error_key: str, lang_key: str, *args):
        translations = Translations.ERRORS.get(lang_key, {})
        error_message = translations.get(error_key, error_key)
        return Translations._format(error_message, *args)

    @staticmethod
    def get_language(language_key: str, lang_key: str):
        translations = Translations.LANGUAGES.get(lang_key, {})
        language = translations.get(language_key, language_key)
        return language
