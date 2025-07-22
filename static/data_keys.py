class DataKeys:
    INTERACTOR_NEW_ROUTES_COUNT_KEY = 'new_routes_count'

    REQUEST_GAME_NAME_KEY = 'game_name'
    REQUEST_NICKNAME_KEY = 'nickname'
    REQUEST_ROUTE_CITY_A_KEY = 'city_a'
    REQUEST_ROUTE_CITY_B_KEY = 'city_b'

    RESPONSE_CODE_KEY = 'response_code'
    RESPONSE_GAME_EXISTS_KEY = 'game_exists'
    RESPONSE_SUMMARY_EXISTS_KEY = 'summary_exists'
    RESPONSE_HOME_ROUTE_KEY = 'home_route'
    RESPONSE_SELF_ROUTE_KEY = 'self_route'
    RESPONSE_SUMMARY_ROUTE_KEY = 'summary_route'

    SESSION_ERROR_MESSAGE_KEY = 'error_message'
    SESSION_GAME_DATA_KEY = 'game_data'
    SESSION_GAME_NAME_KEY = REQUEST_GAME_NAME_KEY
    SESSION_NICKNAME_KEY = REQUEST_NICKNAME_KEY
    SESSION_PLAYER_DATA_KEY = 'player_data'
    SESSION_PLAYER_ROUTES_KEY = 'player_routes'
    SESSION_ROUTE_KEY = 'route'

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")
