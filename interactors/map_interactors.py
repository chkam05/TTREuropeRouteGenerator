from interactors.base_interactor import get_data_container_error
from interactors.models.interactor_result import InteractorResult
from models.data_container import DataContainer
from models.route_wrapper import RouteWrapper
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


def map_(data_container: DataContainer,
        game_name: str,
        nickname: str,
        route_dict: dict,
        language: str) -> InteractorResult:
    redirect = Redirections.HOME

    try:
        if data_container is None:
            raise Exception(Translations.get_error(ErrorKeys.ERROR_MISSING_DATA, language))

        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        _game_data_check(data_container, game_name, nickname, language)

        if not route_dict:
            redirect = Redirections.GAME
            raise Exception(Translations.get_error(ErrorKeys.ERROR_ROUTE_PATH_NOT_EXISTS, language))

        route = RouteWrapper.from_dict(route_dict)
        points = route.get_points()
        j_routes = [[point.to_dict() for point in points]]

        return InteractorResult(True, {
            DataKeys.SESSION_ROUTE_KEY: route.to_dict(),
            DataKeys.SESSION_ROUTE_PATH_KEY: j_routes,
            DataKeys.INTERACTOR_REDIRECTION_KEY: Redirections.MAP
        })
    except Exception as e:
        return InteractorResult(False, {
            DataKeys.INTERACTOR_REDIRECTION_KEY: redirect
        }, error=str(e))
