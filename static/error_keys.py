class ErrorKeys:
    ERROR_GAME_EXISTS = 'error_game_exists'
    ERROR_GAME_NOT_EXISTS = 'error_game_not_exists'
    ERROR_MISSING_DATA = 'error_missing_data'
    ERROR_MISSING_GAME_NAME = 'error_missing_game_name'
    ERROR_MISSING_NICKNAME = 'error_missing_nickname'

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")
