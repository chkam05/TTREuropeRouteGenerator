import json
import time
from typing import Dict, Tuple

from flask import request, Response

from utils.cookies.enums.cookies_state_enum import CookiesStateEnum
from utils.cookies.models.cookies_cache_entry import CookiesCacheEntry
from utils.cookies.models.cookies_data import CookiesData


class CookiesCache:
    _COOKIE_DATA_KEY = 'cookies_data'

    _CACHE_EXPIRY_SEC = 900 # 15 min
    _COOKIE_EXPIRY_SEC = 2592000  # 30 days
    _CROSS_SITE_COOKIES = 'Lax'
    _ONLY_BACKEND = True

    def __init__(self, expiry_seconds: int = _CACHE_EXPIRY_SEC):
        self._cache: Dict[str, CookiesCacheEntry] = {}
        self._expiry = expiry_seconds

    @classmethod
    def _load_data_from_cookies(cls) -> Tuple['CookiesData', CookiesStateEnum]:
        cookie_data = request.cookies.get(cls._COOKIE_DATA_KEY)

        if not cookie_data:
            return CookiesData(), CookiesStateEnum.INITIALIZED

        try:
            data = json.loads(cookie_data)
        except (json.JSONDecodeError, TypeError):
            return CookiesData(), CookiesStateEnum.INITIALIZED

        return CookiesData.from_dict(data), CookiesStateEnum.LOADED

    def has_cookies(self, session_id: str) -> bool:
        entry = self._cache.get(session_id)

        if not entry:
            return False
        if time.time() - entry.last_access > self._expiry:
            del self._cache[session_id]
            return False
        return True

    def has_session(self, session_id: str) -> bool:
        return session_id in self._cache

    def get_cookies(self, session_id: str) -> CookiesData:
        entry = self._cache.get(session_id)

        if entry:
            entry.update_access()
            return entry.data

        data, state = self._load_data_from_cookies()
        self._cache[session_id] = CookiesCacheEntry(data, state)
        return data

    def save_cookies(self, session_id: str, response: Response):
        if self.has_cookies(session_id):
            data = self.get_cookies(session_id)
            cookie_value = json.dumps(data.to_dict())

            response.set_cookie(
                self._COOKIE_DATA_KEY,
                cookie_value,
                max_age=self._COOKIE_EXPIRY_SEC,  # 30 dni
                httponly=self._ONLY_BACKEND,
                samesite=self._CROSS_SITE_COOKIES
            )

    def set_cookies_data(self, session_id: str, data: CookiesData):
        self._cache[session_id] = CookiesCacheEntry(data, CookiesStateEnum.MODIFIED)

    def clear_expired(self):
        now = time.time()
        to_delete = [k for k, v in self._cache.items() if now - v.last_access > self._expiry]
        for key in to_delete:
            del self._cache[key]
