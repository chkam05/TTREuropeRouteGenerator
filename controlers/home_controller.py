from flask import session, redirect, url_for, render_template

from controlers.base_controller import BaseController
from interactors.home_interactors import create_game, join_game
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.http_methods import HttpMethods
from static.static_info import StaticInfo
from utils.request_data_manager import RequestDataManager


class HomeController(BaseController):
    NAME = 'home'
    REDIRECTION = 'home.index'
    TEMPLATE = 'index.html'
    URL_PREFIX = '/'

    ENDPOINT_INDEX = '/'
    ENDPOINT_CREATE_GAME = '/create_game'
    ENDPOINT_JOIN_GAME = '/join_game'

    def __init__(self, data_container: DataContainer):
        super().__init__(self.NAME, __name__, self.URL_PREFIX, data_container)

    def _register_routes(self):
        self._register_route(self.ENDPOINT_INDEX, self.index, methods=[HttpMethods.GET])
        self._register_route(self.ENDPOINT_CREATE_GAME, self.create_game, methods=[HttpMethods.POST])
        self._register_route(self.ENDPOINT_JOIN_GAME, self.join_game, methods=[HttpMethods.POST])

    # region --- REDIRECTIONS ---

    @staticmethod
    def _redirect_game():
        return redirect(url_for(f''))

    def _redirect_itself(self):
        return redirect(url_for(self.REDIRECTION))

    # endregion

    def index(self):
        return render_template(
            self.TEMPLATE,
            error_message=self._get_error(),
            header_data=StaticInfo.get_header(self._get_language()),
            footer_data=StaticInfo.get_footer(self._get_language())
        )

    def create_game(self):
        game_name = RequestDataManager.get_str(DataKeys.REQUEST_GAME_NAME_KEY)
        nickname = RequestDataManager.get_str(DataKeys.REQUEST_NICKNAME_KEY)

        result = create_game(self._data_container, game_name, nickname)

        if result.success:
            session[DataKeys.SESSION_GAME_NAME_KEY] = result.get(DataKeys.SESSION_GAME_NAME_KEY)
            session[DataKeys.SESSION_NICKNAME_KEY] = result.get(DataKeys.SESSION_NICKNAME_KEY)
            self._redirect_game()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            self._redirect_itself()

    def join_game(self):
        game_name = RequestDataManager.get_str(DataKeys.REQUEST_GAME_NAME_KEY)
        nickname = RequestDataManager.get_str(DataKeys.REQUEST_NICKNAME_KEY)

        result = join_game(self._data_container, game_name, nickname)

        if result.success:
            session[DataKeys.SESSION_GAME_NAME_KEY] = result.get(DataKeys.SESSION_GAME_NAME_KEY)
            session[DataKeys.SESSION_NICKNAME_KEY] = result.get(DataKeys.SESSION_NICKNAME_KEY)
            self._redirect_game()
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            self._redirect_itself()
