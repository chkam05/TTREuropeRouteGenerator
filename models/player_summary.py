from datetime import datetime, timezone
from typing import List, Optional

from models.route_summary import RouteSummary


class PlayerSummary:
    DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
    FIELD_GAME_NAME_KEY = 'game_name'
    FIELD_CREATION_DATE_KEY = 'creation_date'
    FIELD_ROUTES_KEY = 'routes'

    def __init__(self, game_name: str, routes: List[RouteSummary], creation_date: Optional[datetime] = None):
        self.game_name = game_name
        self.creation_date = creation_date if creation_date else datetime.now()
        self.routes: List[RouteSummary] = routes if routes else []

    def creation_date_to_str(self, format_: str = DATE_TIME_FORMAT, utc: bool = False) -> str:
        date_time = self.creation_date.astimezone(timezone.utc) if utc else self.creation_date
        return date_time.strftime(format_)

    @staticmethod
    def _str_to_date(date_time_str: str, format_: str = DATE_TIME_FORMAT, utc: bool = False):
        if date_time_str[-3] == ":":
            date_time_str = date_time_str[:-3] + date_time_str[-2:]

        dt = datetime.strptime(date_time_str, format_)
        if utc:
            dt = dt.astimezone(timezone.utc)
        return dt

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'PlayerSummary':
        creation_dt_str = data.get(cls.FIELD_CREATION_DATE_KEY)
        routes = data.get(cls.FIELD_ROUTES_KEY, [])

        return cls(
            game_name=data.get(cls.FIELD_GAME_NAME_KEY),
            routes=[RouteSummary.from_dict(route) for route in routes],
            creation_date=cls._str_to_date(creation_dt_str)
        )

    def to_dict(self) -> dict:
        creation_dt_str = self.creation_date_to_str()
        routes = [route.to_dict() for route in self.routes]

        return {
            self.FIELD_GAME_NAME_KEY: self.game_name,
            self.FIELD_CREATION_DATE_KEY: creation_dt_str,
            self.FIELD_ROUTES_KEY: routes
        }

    # endregion
