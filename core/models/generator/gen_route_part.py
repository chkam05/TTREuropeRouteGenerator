from typing import List

from core.enums.color_enum import ColorEnum
from core.helpers.color_enum_helper import ColorEnumHelper
from core.models.point import Point
from core.models.route import Route


class GenRoutePart:
    FIELD_CITY_A_KEY = 'city_a'
    FIELD_CITY_B_KEY = 'city_b'
    FIELD_POINTS_KEY = 'points'
    FIELD_COLORS_KEY = 'colors'
    FIELD_LENGTH_KEY = 'length'
    FIELD_LOCOMOTIVES_KEY = 'locomotives'
    FIELD_DEFENSIVE_KEY = 'defensive'

    def __init__(self,
                 city_a: str,
                 city_b: str,
                 points: List[Point],
                 colors: List[ColorEnum],
                 length: int,
                 locomotives: int = 0,
                 defensive: bool = False):
        self.city_a = city_a
        self.city_b = city_b
        self.points = points if points else []
        self.colors = colors
        self.length = length
        self.locomotives = locomotives
        self.defensive = defensive

    @staticmethod
    def from_route(route: Route) -> 'GenRoutePart':
        return GenRoutePart(
            city_a=route.city_a.name,
            city_b=route.city_b.name,
            points=route.get_points(),
            colors=route.colors,
            length=route.length,
            locomotives=route.locomotives,
            defensive=route.defensive
        )

    def get_colors_str(self, separator: str = ','):
        return f'{separator} '.join(self.get_colors_str_list())

    def get_colors_str_list(self) -> List[str]:
        return [ColorEnumHelper.to_str(color) for color in self.colors]

    # region --- LOAD & SAVE ---

    @staticmethod
    def from_dict(data: dict) -> 'GenRoutePart':
        colors = data.get(GenRoutePart.FIELD_COLORS_KEY, [])
        points = data.get(GenRoutePart.FIELD_POINTS_KEY, [])

        return GenRoutePart(
            city_a=data.get(GenRoutePart.FIELD_CITY_A_KEY),
            city_b=data.get(GenRoutePart.FIELD_CITY_B_KEY),
            points=[Point.from_dict(p) for p in points],
            colors=[ColorEnumHelper.from_str(color) for color in colors],
            length=data.get(GenRoutePart.FIELD_LENGTH_KEY, 1),
            locomotives=data.get(GenRoutePart.FIELD_LOCOMOTIVES_KEY, 0),
            defensive=data.get(GenRoutePart.FIELD_DEFENSIVE_KEY, False)
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_CITY_A_KEY: self.city_a,
            self.FIELD_CITY_B_KEY: self.city_b,
            self.FIELD_POINTS_KEY: [p.to_dict() for p in self.points],
            self.FIELD_COLORS_KEY: self.get_colors_str_list(),
            self.FIELD_LENGTH_KEY: self.length,
            self.FIELD_LOCOMOTIVES_KEY: self.locomotives,
            self.FIELD_DEFENSIVE_KEY: self.defensive
        }

    # endregion
