from interactors.models.interactor_result import InteractorResult
from static.error_keys import ErrorKeys
from static.language_keys import LanguageKeys
from static.translations import Translations


def get_data_container_error() -> InteractorResult:
    error_message = Translations.get_error(ErrorKeys.ERROR_MISSING_DATA, LanguageKeys.get_default())
    return InteractorResult(False, error=error_message)
