from flask import redirect, url_for, session, render_template, jsonify

from controlers.base_controller import BaseController
from interactors.game_interactors import game, accept_routes, create_routes, create_primary_route, end_game, \
    remove_route, game_exists
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.http_methods import HttpMethods
from static.redirections import Redirections
from static.static_info import StaticInfo
from utils.request_data_manager import RequestDataManager


class GameController(BaseController):
    NAME = 'game'
    TEMPLATE = 'game.html'
    URL_PREFIX = '/'

    ENDPOINT_INDEX = '/'
    ENDPOINT_ACCEPT_ROUTES = '/accept_routes'
    ENDPOINT_CREATE_ROUTES = '/create_routes'
    ENDPOINT_CREATE_PRIMARY_ROUTE = '/create_primary_route'
    ENDPOINT_END_GAME = '/end_game'
    ENDPOINT_GAME_EXISTS = '/game_exists'
    ENDPOINT_REMOVE_ROUTE = '/remove_route'
    ENDPOINT_SHOW_ROUTE_ON_MAP = '/show_route_on_map'

    def __init__(self, data_container: DataContainer):
        super().__init__(self.NAME, __name__, self.URL_PREFIX, data_container)

    def _register_routes(self):
        self._register_route(self.ENDPOINT_INDEX, self.game, methods=[HttpMethods.GET])

    # region --- REDIRECTIONS ---

    @staticmethod
    def _redirect_home():
        return redirect(url_for(Redirections.HOME))

    @staticmethod
    def _redirect_itself():
        return redirect(url_for(Redirections.GAME))

    # endregion

    def game(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = game(self._data_container, game_name, nickname)

        if result.success:
            return render_template(
                self.TEMPLATE,
                header_data=StaticInfo.get_header(self._get_language()),
                game_data=result.get(DataKeys.SESSION_GAME_DATA_KEY),
                player_data=result.get(DataKeys.SESSION_PLAYER_DATA_KEY),
                player_routes=result.get(DataKeys.SESSION_PLAYER_ROUTES_KEY)
            )
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def accept_routes(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = accept_routes(self._data_container, game_name, nickname)

        if result.success:
            return self._redirect_itself()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def create_routes(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = create_routes(self._data_container, game_name, nickname)

        if result.success:
            return self._redirect_itself()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def create_primary_route(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = create_primary_route(self._data_container, game_name, nickname)

        if result.success:
            return self._redirect_itself()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def end_game(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = end_game(self._data_container, game_name, nickname)

        if result.success:
            return self._redirect_home()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def game_exists(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = game_exists(self._data_container, game_name, nickname)

        if not result.success:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error

        return jsonify(result.results), result.get(DataKeys.RESPONSE_CODE_KEY)

    def remove_route(self):
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)
        city_a = RequestDataManager.get_str(DataKeys.REQUEST_ROUTE_CITY_A_KEY)
        city_b = RequestDataManager.get_str(DataKeys.REQUEST_ROUTE_CITY_B_KEY)

        result = remove_route(self._data_container, game_name, nickname, city_a, city_b)

        if result.success:
            if result.get(DataKeys.INTERACTOR_NEW_ROUTES_COUNT_KEY) == 1:
                return self.accept_routes()
            return self._redirect_itself()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def show_route_on_map(self):
        pass
