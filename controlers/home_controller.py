from flask import session, redirect, url_for, render_template, make_response

from controlers.base_controller import BaseController
from interactors.home_interactors import create_game, join_game
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.http_methods import HttpMethods
from static.language_keys import LanguageKeys
from static.redirections import Redirections
from static.static_info import StaticInfo
from utils.cookies.cookies_manager import CookiesManager
from utils.request_data_manager import RequestDataManager


class HomeController(BaseController):
    NAME = 'home'
    TEMPLATE = 'index.html'
    URL_PREFIX = '/'

    ENDPOINT_INDEX = '/'
    ENDPOINT_CREATE_GAME = '/create_game'
    ENDPOINT_JOIN_GAME = '/join_game'
    ENDPOINT_SET_LANGUAGE = '/set_language'

    def __init__(self, cookies_manager: CookiesManager, data_container: DataContainer):
        super().__init__(self.NAME, __name__, self.URL_PREFIX, cookies_manager, data_container)

    def _register_routes(self):
        self._register_route(self.ENDPOINT_INDEX, self.index, methods=[HttpMethods.GET])
        self._register_route(self.ENDPOINT_CREATE_GAME, self.create_game, methods=[HttpMethods.POST])
        self._register_route(self.ENDPOINT_JOIN_GAME, self.join_game, methods=[HttpMethods.POST])
        self._register_route(self.ENDPOINT_SET_LANGUAGE, self.set_language, methods=[HttpMethods.POST])

    # region --- REDIRECTIONS ---

    @staticmethod
    def _redirect_game():
        return redirect(url_for(Redirections.GAME))

    @staticmethod
    def _redirect_itself():
        return redirect(url_for(Redirections.HOME))

    # endregion

    def index(self):
        session_id, cookies_data = self._cookies_manager.get_cookies_data()

        response = make_response(render_template(
            self.TEMPLATE,
            error_message=self._get_error(),
            footer_data=StaticInfo.get_footer(self._get_language()),
            labels_data=StaticInfo.get_home_labels(self._get_language()),
            languages=LanguageKeys.LANGUAGES,
            selected_language=cookies_data.language
        ))

        self._cookies_manager.save_cookies_data(session_id, response)
        return response

    def create_game(self):
        game_name = RequestDataManager.get_str(DataKeys.REQUEST_GAME_NAME_KEY)
        nickname = RequestDataManager.get_str(DataKeys.REQUEST_NICKNAME_KEY)

        result = create_game(self._data_container, game_name, nickname, self._get_language())

        if result.success:
            session[DataKeys.SESSION_GAME_NAME_KEY] = result.get(DataKeys.SESSION_GAME_NAME_KEY)
            session[DataKeys.SESSION_NICKNAME_KEY] = result.get(DataKeys.SESSION_NICKNAME_KEY)
            return self._redirect_game()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_itself()

    def join_game(self):
        game_name = RequestDataManager.get_str(DataKeys.REQUEST_GAME_NAME_KEY)
        nickname = RequestDataManager.get_str(DataKeys.REQUEST_NICKNAME_KEY)

        result = join_game(self._data_container, game_name, nickname, self._get_language())

        if result.success:
            session[DataKeys.SESSION_GAME_NAME_KEY] = result.get(DataKeys.SESSION_GAME_NAME_KEY)
            session[DataKeys.SESSION_NICKNAME_KEY] = result.get(DataKeys.SESSION_NICKNAME_KEY)
            return self._redirect_game()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_itself()

    def set_language(self):
        session_id, cookies_data = self._cookies_manager.get_cookies_data()
        selected_language = RequestDataManager.get_str(DataKeys.REQUEST_LANGUAGE_KEY)

        cookies_data.language = selected_language

        return self._redirect_itself()
