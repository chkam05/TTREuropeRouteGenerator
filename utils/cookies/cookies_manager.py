import uuid
from typing import Tuple

from flask import request, Response

from utils.cookies.cookies_cache import CookiesCache
from utils.cookies.models.cookies_data import CookiesData


class CookiesManager:
    _COOKIE_SESSION_ID_KEY = "session_id"

    _COOKIE_EXPIRY_SEC = 2592000  # 30 days
    _CROSS_SITE_COOKIES = 'Lax'
    _ONLY_BACKEND = True

    def __init__(self):
        self._cache = CookiesCache()

    @classmethod
    def get_session_id(cls) -> str:
        session_id = request.cookies.get(cls._COOKIE_SESSION_ID_KEY)
        if not session_id:
            session_id = str(uuid.uuid4())
        return session_id

    @classmethod
    def save_session_id(cls, session_id: str, response: Response):
        response.set_cookie(
            cls._COOKIE_SESSION_ID_KEY,
            session_id,
            max_age=cls._COOKIE_EXPIRY_SEC,
            httponly=cls._ONLY_BACKEND,
            samesite=cls._CROSS_SITE_COOKIES
        )
        return response

    def get_cookies_data(self) -> Tuple[str, CookiesData]:
        session_id = self.get_session_id()
        cookies_data = self._cache.get_cookies(session_id)
        self._cache.clear_expired()
        return session_id, cookies_data

    def update_cookies_data(self, session_id: str, cookies_data: CookiesData):
        self._cache.set_cookies_data(session_id, cookies_data)
        self._cache.clear_expired()

    def save_cookies_data(self, session_id: str, response: Response):
        self._cache.save_cookies(session_id, response)
        self._cache.clear_expired()
        self.save_session_id(session_id, response)
