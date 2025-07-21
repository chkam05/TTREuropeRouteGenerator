from typing import Optional

from core.enums.direction_enum import DirectionEnum
from core.helpers.direction_enum_helper import DirectionEnumHelper
from core.models.point import Point


class City:
    FIELD_NAME_KEY = 'name'
    FIELD_COUNTRY_KEY = 'country'
    FIELD_POINT_KEY = 'point'
    FIELD_DIRECTION_KEY = 'direction'
    FIELD_EDGE_POINT_KEY = 'edge_point'

    def __init__(self,
                 name: str,
                 country: str,
                 point: Point,
                 direction: Optional[DirectionEnum] = None,
                 edge_point: bool = False):
        self.name = name
        self.country = country
        self.point = point
        self.direction = direction if direction else DirectionEnum.CENTER
        self.edge_point = edge_point

    def direction_to_str(self):
        return DirectionEnumHelper.to_str(self.direction)

    def is_opposite_direction(self, direction: DirectionEnum):
        if self.direction == DirectionEnum.CENTER or direction == DirectionEnum.CENTER:
            return True

        current_direction_str = DirectionEnumHelper.to_str(direction)
        this_direction_str = self.direction_to_str()

        for ch in current_direction_str:
            if ch in this_direction_str:
                return False

        return True

    # region --- LOAD & SAVE ---

    @staticmethod
    def from_dict(data: dict) -> 'City':
        point_str = data.get(City.FIELD_POINT_KEY, Point(0, 0).to_dict())
        direction_str = data.get(City.FIELD_DIRECTION_KEY, DirectionEnum.CENTER.value)

        return City(
            name=data.get(City.FIELD_NAME_KEY),
            country=data.get(City.FIELD_COUNTRY_KEY),
            point=Point.from_dict(point_str),
            direction=DirectionEnumHelper.from_str(direction_str),
            edge_point=data.get(City.FIELD_EDGE_POINT_KEY, False)
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_NAME_KEY: self.name,
            self.FIELD_COUNTRY_KEY: self.country,
            self.FIELD_POINT_KEY: self.point.to_dict(),
            self.FIELD_DIRECTION_KEY: self.direction_to_str(),
            self.FIELD_EDGE_POINT_KEY: self.edge_point
        }

    # endregion
