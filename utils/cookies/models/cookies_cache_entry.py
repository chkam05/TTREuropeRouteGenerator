import time

from utils.cookies.enums.cookies_state_enum import CookiesStateEnum
from utils.cookies.models.cookies_data import CookiesData


class CookiesCacheEntry:
    def __init__(self, data: CookiesData, state: CookiesStateEnum = CookiesStateEnum.INITIALIZED):
        self.data = data
        self.last_access = time.time()
        self.state = state

    def update_access(self):
        self.last_access = time.time()
