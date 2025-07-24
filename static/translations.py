from static.error_keys import ErrorKeys
from static.language_keys import LanguageKeys


class Translations:

    ERRORS = {
        LanguageKeys.LANG_EN_US: {
            ErrorKeys.ERROR_END_GAME_PERMISSIONS: 'Insufficient permissions to end the game.',
            ErrorKeys.ERROR_GAME_ENDED: 'The \"{0}\" game has ended.',
            ErrorKeys.ERROR_GAME_EXISTS: 'Game with name \"{0}\" already exists.',
            ErrorKeys.ERROR_GAME_NOT_EXISTS: 'Game with name \"{0}\" does not exists.',
            ErrorKeys.ERROR_MISSING_DATA: 'Application data container not loaded.',
            ErrorKeys.ERROR_MISSING_GAME_NAME: 'Missing \"Game Name\".',
            ErrorKeys.ERROR_MISSING_NICKNAME: 'Missing \"Nickname\".',
            ErrorKeys.ERROR_PLAYER_NOT_EXISTS: 'Player with nickname \"{0}\" does not exists.',
            ErrorKeys.ERROR_ROUTE_PATH_NOT_EXISTS: 'Route path does not exist.',
            ErrorKeys.ERROR_SESSION_DATA_MISSING: 'Missing or corrupt session data: \"{0}\"'
        },
        LanguageKeys.LANG_PL: {

        }
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

    @classmethod
    def get_error(cls, error_key: str, lang_key: str, *args):
        translations = cls.ERRORS.get(lang_key, {})
        error_message = translations.get(error_key, error_key)
        return cls._format(error_message, *args)
