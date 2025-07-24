from flask import redirect, url_for, session, jsonify, make_response, render_template

from controlers.base_controller import BaseController
from interactors.game_interactors import game_exists
from interactors.map_interactors import map_
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.http_methods import HttpMethods
from static.language_keys import LanguageKeys
from static.redirections import Redirections
from static.static_info import StaticInfo
from utils.cookies.cookies_manager import CookiesManager
from utils.request_data_manager import RequestDataManager


class MapController(BaseController):
    NAME = 'map'
    TEMPLATE = 'map.html'
    URL_PREFIX = '/map'

    IMAGE_FILE = 'images/map.png'

    ENDPOINT_INDEX = '/'
    ENDPOINT_GAME_EXISTS = '/game_exists'
    ENDPOINT_SET_LANGUAGE = '/set_language'

    def __init__(self, cookies_manager: CookiesManager, data_container: DataContainer):
        super().__init__(self.NAME, __name__, self.URL_PREFIX, cookies_manager, data_container)

    def _register_routes(self):
        self._register_route(self.ENDPOINT_INDEX, self.map, methods=[HttpMethods.GET])
        self._register_route(self.ENDPOINT_GAME_EXISTS, self.game_exists, methods=[HttpMethods.GET])
        self._register_route(self.ENDPOINT_SET_LANGUAGE, self.set_language, methods=[HttpMethods.POST])

    # region --- PROPERTIES ---

    @property
    def _self_endpoint(self) -> str:
        return f'{self.ENDPOINT_INDEX}{self.NAME}'

    # endregion

    # region --- REDIRECTIONS ---

    @staticmethod
    def _redirect_home():
        return redirect(url_for(Redirections.HOME))

    @staticmethod
    def _redirect_game():
        return redirect(url_for(Redirections.GAME))

    @staticmethod
    def _redirect_itself():
        return redirect(url_for(Redirections.MAP))

    # endregion

    def map(self):
        session_id, cookies_data = self._cookies_manager.get_cookies_data()
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)
        route_dict = session.get(DataKeys.SESSION_ROUTE_KEY)

        result = map_(self._data_container, game_name, nickname, route_dict, self._get_language())

        if result.success:
            response = make_response(render_template(
                self.TEMPLATE,
                footer_data=StaticInfo.get_footer(self._get_language()),
                labels_data=StaticInfo.get_game_labels(self._get_language()),
                languages=LanguageKeys.LANGUAGES,
                map_image=self.IMAGE_FILE,
                route=result.get(DataKeys.SESSION_ROUTE_KEY),
                route_path=result.get(DataKeys.SESSION_ROUTE_PATH_KEY),
                selected_language=cookies_data.language
            ))

            self._cookies_manager.save_cookies_data(session_id, response)
            return response
        elif result.get(DataKeys.INTERACTOR_REDIRECTION_KEY) == Redirections.GAME:
            return self._redirect_game()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def game_exists(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = game_exists(self._data_container, game_name, nickname, self._get_language(), self._self_endpoint)

        if not result.success:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error

        return jsonify(result.results), result.get(DataKeys.RESPONSE_CODE_KEY)

    def set_language(self):
        session_id, cookies_data = self._cookies_manager.get_cookies_data()
        selected_language = RequestDataManager.get_str(DataKeys.REQUEST_LANGUAGE_KEY)

        cookies_data.language = selected_language

        return self._redirect_itself()
