from typing import Optional, Any

from flask import request, session

from static.data_keys import DataKeys


class RequestDataManager:
    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static utility class and cannot be instantiated.")

    @staticmethod
    def get(attrib_key: str) -> Any:
        return request.form.get(attrib_key)

    @staticmethod
    def get_bool(attrib_key: str) -> Optional[bool]:
        value = request.form.get(attrib_key)
        return bool(value) if value else None

    @staticmethod
    def get_str(attrib_key: str, default: Optional[str] = None) -> Optional[str]:
        value = request.form.get(attrib_key)
        return str(value) if value else default if default else None

    @staticmethod
    def get_upper_str(attrib_key: str, default: Optional[str] = None) -> Optional[str]:
        value = request.form.get(attrib_key, default)
        return str(value).upper() if value else None
