from flask import redirect, url_for, session, render_template, jsonify, make_response

from controlers.base_controller import BaseController
from interactors.game_interactors import game, accept_routes, create_routes, create_primary_route, end_game, \
    remove_route, game_exists
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.http_methods import HttpMethods
from static.language_keys import LanguageKeys
from static.redirections import Redirections
from static.static_info import StaticInfo
from utils.cookies.cookies_manager import CookiesManager
from utils.request_data_manager import RequestDataManager


class GameController(BaseController):
    NAME = 'game'
    TEMPLATE = 'game.html'
    URL_PREFIX = '/game'

    ENDPOINT_GAME = '/'
    ENDPOINT_ACCEPT_ROUTES = '/accept_routes'
    ENDPOINT_CREATE_ROUTES = '/create_routes'
    ENDPOINT_CREATE_PRIMARY_ROUTE = '/create_primary_route'
    ENDPOINT_END_GAME = '/end_game'
    ENDPOINT_GAME_EXISTS = '/game_exists'
    ENDPOINT_REMOVE_ROUTE = '/remove_route'
    ENDPOINT_SHOW_ROUTE_ON_MAP = '/show_route_on_map'

    def __init__(self, cookies_manager: CookiesManager, data_container: DataContainer):
        super().__init__(self.NAME, __name__, self.URL_PREFIX, cookies_manager, data_container)

    def _register_routes(self):
        self._register_route(self.ENDPOINT_GAME, self.game, methods=[HttpMethods.GET])

    # region --- REDIRECTIONS ---

    @staticmethod
    def _redirect_home():
        return redirect(url_for(Redirections.HOME))

    @staticmethod
    def _redirect_itself():
        return redirect(url_for(Redirections.GAME))

    # endregion

    def game(self):
        session_id, cookies_data = self._cookies_manager.get_cookies_data()
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = game(self._data_container, game_name, nickname, self._get_language())

        if result.success:
            response = make_response(render_template(
                self.TEMPLATE,
                footer_data=StaticInfo.get_footer(self._get_language()),
                game_data=result.get(DataKeys.SESSION_GAME_DATA_KEY),
                labels_data=StaticInfo.get_game_labels(self._get_language()),
                languages=LanguageKeys.LANGUAGES,
                player_data=result.get(DataKeys.SESSION_PLAYER_DATA_KEY),
                player_routes=result.get(DataKeys.SESSION_PLAYER_ROUTES_KEY),
                selected_language=cookies_data.language
            ))

            self._cookies_manager.save_cookies_data(session_id, response)
            return response
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def accept_routes(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = accept_routes(self._data_container, game_name, nickname, self._get_language())

        if result.success:
            return self._redirect_itself()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def create_routes(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = create_routes(self._data_container, game_name, nickname, self._get_language())

        if result.success:
            return self._redirect_itself()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def create_primary_route(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = create_primary_route(self._data_container, game_name, nickname, self._get_language())

        if result.success:
            return self._redirect_itself()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def end_game(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = end_game(self._data_container, game_name, nickname, self._get_language())

        if result.success:
            return self._redirect_home()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def game_exists(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = game_exists(self._data_container, game_name, nickname, self._get_language())

        if not result.success:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error

        return jsonify(result.results), result.get(DataKeys.RESPONSE_CODE_KEY)

    def remove_route(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)
        city_a = RequestDataManager.get_str(DataKeys.REQUEST_ROUTE_CITY_A_KEY)
        city_b = RequestDataManager.get_str(DataKeys.REQUEST_ROUTE_CITY_B_KEY)

        result = remove_route(self._data_container, game_name, nickname, city_a, city_b, self._get_language())

        if result.success:
            if result.get(DataKeys.INTERACTOR_NEW_ROUTES_COUNT_KEY) == 1:
                return self.accept_routes()
            return self._redirect_itself()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def show_route_on_map(self):
        pass
