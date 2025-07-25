from typing import List, Optional

from models.route_summary import RouteSummary


class PlayerSummary:
    FIELD_NICKNAME_KEY = 'nickname'
    FIELD_ROUTES_KEY = 'routes'

    def __init__(self, nickname: str, routes: Optional[List[RouteSummary]] = None):
        self.nickname = nickname
        self.routes: List[RouteSummary] = routes if routes else []

    # region --- PROPERTIES ---

    @property
    def points(self) -> int:
        return sum([r.points if r.is_completed else -r.points for r in self.routes])

    # endregion

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'PlayerSummary':
        routes = data.get(cls.FIELD_ROUTES_KEY, [])

        return cls(
            nickname=data.get(cls.FIELD_NICKNAME_KEY),
            routes=[RouteSummary.from_dict(route) for route in routes]
        )

    def to_dict(self) -> dict:
        routes = [route.to_dict() for route in self.routes]

        return {
            self.FIELD_NICKNAME_KEY: self.nickname,
            self.FIELD_ROUTES_KEY: routes
        }

    # endregion
