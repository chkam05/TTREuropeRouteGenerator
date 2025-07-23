from utils.cookies.enums.cookies_state_enum import CookiesStateEnum


class CookiesStateEnumHelper:
    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @classmethod
    def from_str(cls, int_value: int) -> CookiesStateEnum:
        return next((gt for gt in CookiesStateEnum if gt.value == int_value), CookiesStateEnum.INITIALIZED)

    @classmethod
    def get_list(cls) -> list:
        return [cookies_state_enum.value for cookies_state_enum in CookiesStateEnum]

    @classmethod
    def to_int(cls, cookies_state_enum: CookiesStateEnum) -> int:
        return cookies_state_enum.value
