from interactors.base_interactor import get_data_container_error
from interactors.models.interactor_result import InteractorResult
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.error_keys import ErrorKeys
from static.language_keys import LanguageKeys
from static.translations import Translations


def create_game(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    if not game_name:
        error_message = Translations.get_error(ErrorKeys.ERROR_MISSING_GAME_NAME, data_container.language)
        return InteractorResult(False, error=error_message)

    if not nickname:
        error_message = Translations.get_error(ErrorKeys.ERROR_MISSING_NICKNAME, data_container.language)
        return InteractorResult(False, error=error_message)

    game_name = game_name.upper()
    nickname = nickname.upper()

    if data_container.has_game(game_name):
        error_message = Translations.get_error(ErrorKeys.ERROR_GAME_EXISTS, data_container.language, game_name)
        return InteractorResult(False, error=error_message)

    player = data_container.get_or_create_player(nickname)
    game = data_container.create_game(game_name, player)

    return InteractorResult(True, {
        DataKeys.SESSION_GAME_NAME_KEY: game.name,
        DataKeys.SESSION_NICKNAME_KEY: player.nickname
    })


def join_game(data_container: DataContainer, game_name: str, nickname: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error()

    if not game_name:
        error_message = Translations.get_error(ErrorKeys.ERROR_MISSING_GAME_NAME, data_container.language)
        return InteractorResult(False, error=error_message)

    if not nickname:
        error_message = Translations.get_error(ErrorKeys.ERROR_MISSING_NICKNAME, data_container.language)
        return InteractorResult(False, error=error_message)

    game_name = game_name.upper()
    nickname = nickname.upper()

    if not data_container.has_game(game_name):
        error_message = Translations.get_error(
            ErrorKeys.ERROR_GAME_NOT_EXISTS, data_container.language, game_name)
        return InteractorResult(False, error=error_message)

    player = data_container.get_or_create_player(nickname)
    game = data_container.get_game(game_name)
    game.add_player(player.nickname)

    return InteractorResult(True, {
        DataKeys.SESSION_GAME_NAME_KEY: game.name,
        DataKeys.SESSION_NICKNAME_KEY: player.nickname
    })
