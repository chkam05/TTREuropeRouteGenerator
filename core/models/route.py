from typing import Optional, List

from core.enums.color_enum import ColorEnum
from core.models.city import City
from core.models.point import Point
from core.models.route_variant import RouteVariant


class Route:
    FIELD_CITY_A_KEY = 'city_a'
    FIELD_CITY_B_KEY = 'city_b'
    FIELD_VARIANTS_KEY = 'variants'

    MANY_VARIANTS_WEIGHT_PERCENT = 0.9

    def __init__(self, city_a: City, city_b: City, variants: Optional[List[RouteVariant]]):
        self.city_a = city_a
        self.city_b = city_b
        self.variants: List[RouteVariant] = variants if variants else []

    # region --- PROPERTIES ---

    @property
    def colors(self) -> List[ColorEnum]:
        return [variant.color for variant in self.variants]

    @property
    def defensive(self) -> bool:
        return any(variant.defensive for variant in self.variants)

    @property
    def length(self) -> int:
        return max([variant.length for variant in self.variants])

    @property
    def locomotives(self) -> int:
        return max([variant.locomotives for variant in self.variants])

    @property
    def str_colors(self) -> List[str]:
        return [variant.color_as_str() for variant in self.variants]

    @property
    def variants_count(self) -> int:
        return len(self.variants)

    # endregion

    def get_points(self) -> List[Point]:
        return [self.city_a.point, self.city_b.point]

    def get_weight(self) -> float:
        weight = sum(variant.get_weight() for variant in self.variants) / len(self.variants)

        if self.variants_count > 1:
            weight *= self.MANY_VARIANTS_WEIGHT_PERCENT

        return weight

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'Route':
        city_a = data.get(cls.FIELD_CITY_A_KEY)
        city_b = data.get(cls.FIELD_CITY_B_KEY)
        variants = data.get(cls.FIELD_VARIANTS_KEY, [])

        return cls(
            city_a=City.from_dict(city_a),
            city_b=City.from_dict(city_b),
            variants=[RouteVariant.from_dict(option) for option in variants]
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_CITY_A_KEY: self.city_a.to_dict(),
            self.FIELD_CITY_B_KEY: self.city_b.to_dict(),
            self.FIELD_VARIANTS_KEY: [variant.to_dict() for variant in self.variants]
        }

    # endregion
