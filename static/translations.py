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
            ErrorKeys.ERROR_SESSION_DATA_MISSING: 'Missing or corrupt session data: \"{0}\"',
            ErrorKeys.ERROR_SUMMARY_NOT_EXISTS: '\"{0}\" Game summary does not exists.'
        },
        LanguageKeys.LANG_PL: {
            ErrorKeys.ERROR_END_GAME_PERMISSIONS: 'Niewystarczające uprawnienia do zakończenia gry.',
            ErrorKeys.ERROR_GAME_ENDED: 'Gra \"{0}\" zakończyła się.',
            ErrorKeys.ERROR_GAME_EXISTS: 'Gra o nazwie \"{0}\" już istnieje.',
            ErrorKeys.ERROR_GAME_NOT_EXISTS: 'Gra o nazwie \"{0}\" nie istnieje.',
            ErrorKeys.ERROR_MISSING_DATA: 'Kontener danych aplikacji nie został załadowany.',
            ErrorKeys.ERROR_MISSING_GAME_NAME: 'Brakuje \"Nazwy gry\".',
            ErrorKeys.ERROR_MISSING_NICKNAME: 'Brakuje \"Nazwy gracza\".',
            ErrorKeys.ERROR_PLAYER_NOT_EXISTS: 'Gracz o nazwie \"{0}\" nie istnieje.',
            ErrorKeys.ERROR_ROUTE_PATH_NOT_EXISTS: 'Ścieżka trasy nie istnieje.',
            ErrorKeys.ERROR_SESSION_DATA_MISSING: 'Brakujące lub uszkodzone dane sesji: \"{0}\"',
            ErrorKeys.ERROR_SUMMARY_NOT_EXISTS: 'Podsumowanie gry \"{0}\" nie istnieje.'
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
