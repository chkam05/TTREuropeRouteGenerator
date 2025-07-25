from typing import Tuple

from interactors.base_interactor import get_data_container_error
from interactors.models.interactor_result import InteractorResult
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.error_keys import ErrorKeys
from static.language_keys import LanguageKeys
from static.translations import Translations


def _input_check(game_name: str, nickname: str, language: str):
    if not game_name:
        raise Exception(Translations.get_error(ErrorKeys.ERROR_MISSING_GAME_NAME, language))

    if not nickname:
        raise Exception(Translations.get_error(ErrorKeys.ERROR_MISSING_NICKNAME, language))


def create_game(data_container: DataContainer, game_name: str, nickname: str, language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        if data_container.has_game(game_name):
            raise Exception(Translations.get_error(ErrorKeys.ERROR_GAME_EXISTS, language, game_name))

        player = data_container.get_or_create_player(nickname)
        game = data_container.create_game(game_name, player)

        return InteractorResult(True, {
            DataKeys.SESSION_GAME_NAME_KEY: game.name,
            DataKeys.SESSION_NICKNAME_KEY: player.nickname
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))


def join_game(data_container: DataContainer, game_name: str, nickname: str, language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        if not data_container.has_game(game_name):
            raise Exception(Translations.get_error(ErrorKeys.ERROR_GAME_NOT_EXISTS, language, game_name))

        player = data_container.get_or_create_player(nickname)
        game = data_container.get_game(game_name)
        game.add_player(player.nickname)

        data_container.set_refresh(game_name, player.nickname)

        return InteractorResult(True, {
            DataKeys.SESSION_GAME_NAME_KEY: game.name,
            DataKeys.SESSION_NICKNAME_KEY: player.nickname
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))
