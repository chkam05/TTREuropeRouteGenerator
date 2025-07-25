from flask import redirect, url_for, session, make_response, render_template

from controlers.base_controller import BaseController
from interactors.summary_interactor import summary
from models.data_container import DataContainer
from static.data_keys import DataKeys
from static.http_methods import HttpMethods
from static.language_keys import LanguageKeys
from static.redirections import Redirections
from static.static_info import StaticInfo
from utils.cookies.cookies_manager import CookiesManager
from utils.request_data_manager import RequestDataManager


class SummaryController(BaseController):
    NAME = 'summary'
    TEMPLATE = 'summary.html'
    URL_PREFIX = '/summary'

    ENDPOINT_INDEX = '/'
    ENDPOINT_EXIT = '/exit'
    ENDPOINT_SET_LANGUAGE = '/set_language'

    def __init__(self, cookies_manager: CookiesManager, data_container: DataContainer):
        super().__init__(self.NAME, __name__, self.URL_PREFIX, cookies_manager, data_container)

    def _register_routes(self):
        self._register_route(self.ENDPOINT_INDEX, self.summary, methods=[HttpMethods.GET])
        self._register_route(self.ENDPOINT_EXIT, self.exit, methods=[HttpMethods.POST])
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
    def _redirect_itself():
        return redirect(url_for(Redirections.SUMMARY))

    # endregion

    def summary(self):
        session_id, cookies_data = self._cookies_manager.get_cookies_data()
        game_name = session.get(DataKeys.SESSION_GAME_NAME_KEY)
        nickname = session.get(DataKeys.SESSION_NICKNAME_KEY)

        result = summary(self._data_container, game_name, nickname, self._get_language())

        if result.success:
            response = make_response(render_template(
                self.TEMPLATE,
                footer_data=StaticInfo.get_footer(self._get_language()),
                labels_data=StaticInfo.get_summary_labels(self._get_language()),
                languages=LanguageKeys.LANGUAGES,
                player_data=result.get(DataKeys.SESSION_PLAYER_DATA_KEY),
                selected_language=cookies_data.language,
                summary_data=result.get(DataKeys.SESSION_SUMMARY_DATA_KEY)
            ))

            self._cookies_manager.save_cookies_data(session_id, response)
            return response
        else:
            session[DataKeys.SESSION_ERROR_MESSAGE_KEY] = result.error
            return self._redirect_home()

    def exit(self):
        return self._redirect_home()

    def set_language(self):
        session_id, cookies_data = self._cookies_manager.get_cookies_data()
        selected_language = RequestDataManager.get_str(DataKeys.REQUEST_LANGUAGE_KEY)

        cookies_data.language = selected_language

        return self._redirect_itself()
