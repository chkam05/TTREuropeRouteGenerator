class DataKeys:
    REQUEST_GAME_NAME_KEY = 'game_name'
    REQUEST_NICKNAME_KEY = 'nickname'

    SESSION_ERROR_MESSAGE_KEY = 'error_message'
    SESSION_GAME_NAME_KEY = REQUEST_GAME_NAME_KEY
    SESSION_NICKNAME_KEY = REQUEST_NICKNAME_KEY
    SESSION_ROUTE_KEY = 'route'

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")
