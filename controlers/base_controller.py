from abc import abstractmethod, ABC
from typing import Callable, List, Optional

from flask import Blueprint, session

from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.language_keys import LanguageKeys
from utils.cookies.cookies_manager import CookiesManager


class BaseController(ABC):

    def __init__(self,
                 controller_name: str,
                 import_name: str,
                 url_prefix: str,
                 cookies_manager: CookiesManager,
                 data_container: DataContainer):
        self._cookies_manager = cookies_manager
        self._data_container = data_container
        self._blueprint = Blueprint(controller_name, import_name, url_prefix=url_prefix)
        self._register_routes()

    # region --- PROPERTIES ---

    @property
    def blueprint(self) -> Blueprint:
        return self._blueprint

    # endregion

    def _register_route(self,
                        endpoint: str,
                        method: Callable,
                        methods: List[str],
                        endpoint_name: Optional[str] = None):
        self._blueprint.add_url_rule(
            endpoint,
            view_func=method,
            methods=methods,
            endpoint=endpoint_name or method.__name__
        )

    @abstractmethod
    def _register_routes(self):
        pass

    @staticmethod
    def _get_error() -> Optional[str]:
        error_message = session.get(DataKeys.SESSION_ERROR_MESSAGE_KEY, None)
        if error_message:
            del session[DataKeys.SESSION_ERROR_MESSAGE_KEY]
            return error_message
        return None

    def _get_language(self):
        session_id, cookies_data = self._cookies_manager.get_cookies_data()
        return cookies_data.language
