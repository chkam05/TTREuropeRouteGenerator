from interactors.base_interactor import get_data_container_error
from interactors.models.interactor_result import InteractorResult
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.error_keys import ErrorKeys
from static.redirections import Redirections
from static.translations import Translations


def _input_check(game_name: str, nickname: str, language: str):
    if not game_name:
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_SESSION_DATA_MISSING, language, DataKeys.SESSION_GAME_NAME_KEY))

    if not nickname:
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_SESSION_DATA_MISSING, language, DataKeys.SESSION_NICKNAME_KEY))


def _game_data_check(data_container: DataContainer, game_name: str, nickname: str, language: str):
    if not data_container.has_game(game_name):
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_GAME_NOT_EXISTS, language, game_name))

    if not data_container.has_player(nickname):
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_PLAYER_NOT_EXISTS, language, nickname))


def game(data_container: DataContainer, game_name: str, nickname: str, language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        _game_data_check(data_container, game_name, nickname, language)

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)
        player_routes = game_data.get_player_routes(player.nickname)

        return InteractorResult(True, {
            DataKeys.SESSION_GAME_DATA_KEY: game_data,
            DataKeys.SESSION_PLAYER_DATA_KEY: player,
            DataKeys.SESSION_PLAYER_ROUTES_KEY: player_routes
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))


def accept_routes(data_container: DataContainer, game_name: str, nickname: str, language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        _game_data_check(data_container, game_name, nickname, language)

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        game_data.accept_routes(player.nickname)

        return InteractorResult(True)
    except Exception as e:
        return InteractorResult(False, error=str(e))


def create_routes(data_container: DataContainer, game_name: str, nickname: str, language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        _game_data_check(data_container, game_name, nickname, language)

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        game_data.create_routes(data_container.generator, player.nickname)

        return InteractorResult(True)
    except Exception as e:
        return InteractorResult(False, error=str(e))


def create_primary_route(data_container: DataContainer,
                         game_name: str,
                         nickname: str,
                         language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        _game_data_check(data_container, game_name, nickname, language)

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        game_data.create_primary_route(data_container.generator, player.nickname)

        return InteractorResult(True)
    except Exception as e:
        return InteractorResult(False, error=str(e))


def end_game(data_container: DataContainer, game_name: str, nickname: str, language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        _game_data_check(data_container, game_name, nickname, language)

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        if not data_container.is_host(game_name, player):
            raise Exception(Translations.get_error(ErrorKeys.ERROR_END_GAME_PERMISSIONS, language))

        game_data = data_container.end_game(game_name, player)
        return InteractorResult(True, {
            DataKeys.SESSION_GAME_DATA_KEY: game_data
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))


def game_exists(data_container: DataContainer,
                game_name: str,
                nickname: str,
                language: str,
                self_route: str = '/game') -> InteractorResult:
    response_data = {
        DataKeys.RESPONSE_CODE_KEY: 200,
        DataKeys.RESPONSE_GAME_EXISTS_KEY: False,
        DataKeys.RESPONSE_SUMMARY_EXISTS_KEY: False,
        DataKeys.RESPONSE_HOME_ROUTE_KEY: '/',
        DataKeys.RESPONSE_SELF_ROUTE_KEY: self_route,
        DataKeys.RESPONSE_SUMMARY_ROUTE_KEY: '/summary'
    }

    try:
        if data_container is None:
            raise Exception(Translations.get_error(ErrorKeys.ERROR_MISSING_DATA, language))

        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        if data_container.has_game(game_name):
            response_data[DataKeys.RESPONSE_GAME_EXISTS_KEY] = True
            return InteractorResult(True, response_data)

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        # if game_data in summary_data:
        #     response_data[DataKeys.RESPONSE_SUMMARY_EXISTS_KEY] = True
        #     return InteractorResult(True, response_data)

        raise Exception(Translations.get_error(ErrorKeys.ERROR_GAME_ENDED, language, game_name))
    except Exception as e:
        response_data[DataKeys.RESPONSE_CODE_KEY] = 404
        return InteractorResult(False, response_data, error=str(e))


def remove_route(data_container: DataContainer,
                 game_name: str,
                 nickname: str,
                 city_a: str,
                 city_b: str,
                 language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        _game_data_check(data_container, game_name, nickname, language)

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        game_data.remove_route(city_a, city_b, player.nickname)

        return InteractorResult(True, {
            DataKeys.INTERACTOR_NEW_ROUTES_COUNT_KEY: game_data.count_new_routes(nickname)
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))

def show_route_on_map(data_container: DataContainer,
                      game_name: str,
                      nickname: str,
                      city_a: str,
                      city_b: str,
                      language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        _game_data_check(data_container, game_name, nickname, language)

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        route = game_data.find_player_route_by_cities(city_a, city_b, player.nickname)

        if not route:
            error_message = Translations.get_error(ErrorKeys.ERROR_ROUTE_PATH_NOT_EXISTS, language)
            return InteractorResult(False, {
                DataKeys.INTERACTOR_REDIRECTION_KEY: Redirections.MAP
            }, error_message)

        return InteractorResult(True, {
            DataKeys.SESSION_ROUTE_KEY: route.to_dict(),
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))
