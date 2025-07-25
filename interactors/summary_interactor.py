from interactors.base_interactor import get_data_container_error
from interactors.models.interactor_result import InteractorResult
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.error_keys import ErrorKeys
from static.translations import Translations


def _input_check(game_name: str, nickname: str, language: str):
    if not game_name:
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_SESSION_DATA_MISSING, language, DataKeys.SESSION_GAME_NAME_KEY))

    if not nickname:
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_SESSION_DATA_MISSING, language, DataKeys.SESSION_NICKNAME_KEY))


def _game_data_check(data_container: DataContainer, game_name: str, nickname: str, language: str):
    if not data_container.has_summary(game_name):
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_SUMMARY_NOT_EXISTS, language, game_name))

    if not data_container.has_player(nickname):
        raise Exception(Translations.get_error(
            ErrorKeys.ERROR_PLAYER_NOT_EXISTS, language, nickname))


def summary(data_container: DataContainer, game_name: str, nickname: str, language: str) -> InteractorResult:
    if data_container is None:
        return get_data_container_error(language)

    try:
        _input_check(game_name, nickname, language)

        game_name = game_name.upper()
        nickname = nickname.upper()

        _game_data_check(data_container, game_name, nickname, language)

        summary_data = data_container.get_summary(game_name)
        player = data_container.get_player(nickname)

        return InteractorResult(True, {
            DataKeys.SESSION_SUMMARY_DATA_KEY: summary_data,
            DataKeys.SESSION_PLAYER_DATA_KEY: player
        })
    except Exception as e:
        return InteractorResult(False, error=str(e))
