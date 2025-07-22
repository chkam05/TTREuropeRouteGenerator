from typing import Tuple

from interactors.base_interactor import get_data_container_error
from interactors.models.interactor_result import InteractorResult
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.error_keys import ErrorKeys
from static.language_keys import LanguageKeys
from static.translations import Translations


def _input_check(data_container: DataContainer, game_name: str, nickname: str):
    if not game_name:
        raise Exception(Translations.get_error(ErrorKeys.ERROR_MISSING_GAME_NAME, data_container.language))

    if not nickname:
        raise Exception(Translations.get_error(ErrorKeys.ERROR_MISSING_NICKNAME, data_container.language))


def create_game(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    try:
        _input_check(data_container, game_name, nickname)

        game_name = game_name.upper()
        nickname = nickname.upper()

        if data_container.has_game(game_name):
            raise Exception(Translations.get_error(
                ErrorKeys.ERROR_GAME_EXISTS, data_container.language, game_name))

        player = data_container.get_or_create_player(nickname)
        game = data_container.create_game(game_name, player)

        return InteractorResult(True, {
            DataKeys.SESSION_GAME_NAME_KEY: game.name,
            DataKeys.SESSION_NICKNAME_KEY: player.nickname
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))


def join_game(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    try:
        _input_check(data_container, game_name, nickname)

        game_name = game_name.upper()
        nickname = nickname.upper()

        if not data_container.has_game(game_name):
            raise Exception(Translations.get_error(
                ErrorKeys.ERROR_GAME_NOT_EXISTS, data_container.language, game_name))

        player = data_container.get_or_create_player(nickname)
        game = data_container.get_game(game_name)
        game.add_player(player.nickname)

        return InteractorResult(True, {
            DataKeys.SESSION_GAME_NAME_KEY: game.name,
            DataKeys.SESSION_NICKNAME_KEY: player.nickname
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))
