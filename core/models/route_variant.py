from core.enums.color_enum import ColorEnum
from core.helpers.color_enum_helper import ColorEnumHelper
from core.helpers.points_converter import PointsConverter


class RouteVariant:
    FIELD_COLOR_KEY = 'color'
    FIELD_LENGTH_KEY = 'length'
    FIELD_LOCOMOTIVES_KEY = 'locomotives'
    FIELD_DEFENSIVE_KEY = 'defensive'

    DEFENSIVE_WEIGHT_POINTS = 2
    FREE_COLOR_WEIGHT_PERCENT = 0.8
    LOCOMOTIVES_WEIGHT_PERCENT = 1.5

    def __init__(self, color: ColorEnum, length: int, locomotives: int = 0, defensive: bool = False):
        self.color = color
        self.length = length
        self.locomotives = locomotives
        self.defensive = defensive

    def color_as_str(self) -> str:
        return ColorEnumHelper.to_str(self.color)

    def get_weight(self) -> float:
        points = PointsConverter.convert_length_to_points(self.length)
        weight = points

        if self.is_free_color():
            weight = weight * self.FREE_COLOR_WEIGHT_PERCENT - points

        if self.has_locomotives():
            weight += self.locomotives * self.LOCOMOTIVES_WEIGHT_PERCENT

        if self.defensive:
            weight += self.DEFENSIVE_WEIGHT_POINTS

        return weight

    def has_locomotives(self) -> bool:
        return self.locomotives > 0

    def is_free_color(self) -> bool:
        return self.color == ColorEnum.TRANSPARENT

    # region --- LOAD & SAVE ---

    @staticmethod
    def from_dict(data: dict) -> 'RouteVariant':
        color_str = data.get(RouteVariant.FIELD_COLOR_KEY, ColorEnum.TRANSPARENT.value)

        return RouteVariant(
            color=ColorEnumHelper.from_str(color_str),
            length=data.get(RouteVariant.FIELD_LENGTH_KEY, 1),
            locomotives=data.get(RouteVariant.FIELD_LOCOMOTIVES_KEY, 0),
            defensive=data.get(RouteVariant.FIELD_DEFENSIVE_KEY, False)
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_COLOR_KEY: self.color_as_str(),
            self.FIELD_LENGTH_KEY: self.length,
            self.FIELD_LOCOMOTIVES_KEY: self.locomotives,
            self.FIELD_DEFENSIVE_KEY: self.defensive
        }

    # endregion
