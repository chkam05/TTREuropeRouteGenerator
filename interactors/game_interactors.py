from typing import Optional

from interactors.base_interactor import get_data_container_error
from interactors.models.interactor_result import InteractorResult
from models.data_container import DataContainer
from models.game import Game
from models.player import Player
from static.data_keys import DataKeys
from static.error_keys import ErrorKeys
from static.language_keys import LanguageKeys
from static.translations import Translations


def _input_check(data_container: DataContainer, game_name: str, nickname: str):
    if not game_name:
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_SESSION_DATA_MISSING, data_container.language, DataKeys.SESSION_GAME_NAME_KEY))

    if not nickname:
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_SESSION_DATA_MISSING, data_container.language, DataKeys.SESSION_NICKNAME_KEY))


def _game_data_check(data_container: DataContainer, game_data: Optional[Game], player: Optional[Player]):
    if not game_data:
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_GAME_NOT_EXISTS, data_container.language, game_name))

    if not player:
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_PLAYER_NOT_EXISTS, data_container.language, nickname))


def game(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    try:
        _input_check(data_container, game_name, nickname)

        game_name = game_name.upper()
        nickname = nickname.upper()

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        _game_data_check(data_container, game_data, player)

        player_routes = game_data.get_player_routes(player.nickname)

        return InteractorResult(True, {
            DataKeys.SESSION_GAME_DATA_KEY: game_data,
            DataKeys.SESSION_PLAYER_DATA_KEY: player,
            DataKeys.SESSION_PLAYER_ROUTES_KEY: player_routes
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))


def accept_routes(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    try:
        _input_check(data_container, game_name, nickname)

        game_name = game_name.upper()
        nickname = nickname.upper()

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        _game_data_check(data_container, game_data, player)

        game_data.accept_routes(player.nickname)

        return InteractorResult(True)
    except Exception as e:
        return InteractorResult(False, error=str(e))


def create_routes(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    try:
        _input_check(data_container, game_name, nickname)

        game_name = game_name.upper()
        nickname = nickname.upper()

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        _game_data_check(data_container, game_data, player)

        game_data.create_routes(data_container.generator, player.nickname)

        return InteractorResult(True)
    except Exception as e:
        return InteractorResult(False, error=str(e))


def create_primary_route(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    try:
        _input_check(data_container, game_name, nickname)

        game_name = game_name.upper()
        nickname = nickname.upper()

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        _game_data_check(data_container, game_data, player)

        game_data.create_primary_route(data_container.generator, player.nickname)

        return InteractorResult(True)
    except Exception as e:
        return InteractorResult(False, error=str(e))


def end_game(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    try:
        _input_check(data_container, game_name, nickname)

        game_name = game_name.upper()
        nickname = nickname.upper()

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        _game_data_check(data_container, game_data, player)

        if not data_container.is_host(game_name, player):
            raise Exception(Translations.get_error(ErrorKeys.ERROR_END_GAME_PERMISSIONS, data_container.language))

        game_data = data_container.end_game(game_name, player)
        return InteractorResult(True, {
            DataKeys.SESSION_GAME_DATA_KEY: game_data
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))


def game_exists(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    response_data = {
        DataKeys.RESPONSE_CODE_KEY: 200,
        DataKeys.RESPONSE_GAME_EXISTS_KEY: False,
        DataKeys.RESPONSE_SUMMARY_EXISTS_KEY: False,
        DataKeys.RESPONSE_HOME_ROUTE_KEY: '/',
        DataKeys.RESPONSE_SELF_ROUTE_KEY: '/game',
        DataKeys.RESPONSE_SUMMARY_ROUTE_KEY: '/summary'
    }

    try:
        if data_container is None:
            raise Exception(Translations.get_error(ErrorKeys.ERROR_MISSING_DATA, LanguageKeys.get_default()))

        _input_check(data_container, game_name, nickname)

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

        raise Exception(Translations.get_error(ErrorKeys.ERROR_GAME_ENDED, data_container.language, game_name))
    except Exception as e:
        response_data[DataKeys.RESPONSE_CODE_KEY] = 404
        return InteractorResult(False, response_data, error=str(e))


def remove_route(data_container: DataContainer,
                 game_name: str,
                 nickname: str,
                 city_a: str,
                 city_b: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    try:
        _input_check(data_container, game_name, nickname)

        game_name = game_name.upper()
        nickname = nickname.upper()

        game_data = data_container.get_game(game_name)
        player = data_container.get_player(nickname)

        _game_data_check(data_container, game_data, player)

        game_data.remove_route(city_a, city_b, player.nickname)

        return InteractorResult(True, {
            DataKeys.INTERACTOR_NEW_ROUTES_COUNT_KEY: game_data.count_new_routes(nickname)
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))
