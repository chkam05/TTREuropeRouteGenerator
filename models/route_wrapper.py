from typing import List

from core.models.generator.gen_route import GenRoute
from core.models.point import Point


class RouteWrapper:
    FIELD_GENERATED_ROUTE_KEY = 'generated_route'
    FIELD_IS_NEW_KEY = 'is_new'
    FIELD_IS_COMPLETED = 'is_completed'

    def __init__(self, generated_route: GenRoute, is_new: bool = True, is_completed: bool = False):
        self._generated_route = generated_route
        self._is_new = is_new
        self._is_completed = is_completed

    # region --- PROPERTIES ---

    @property
    def city_a(self) -> str:
        return self._generated_route.city_a

    @property
    def city_b(self) -> str:
        return self._generated_route.city_b

    @property
    def points(self) -> int:
        return self._generated_route.points

    @property
    def is_completed(self) -> bool:
        return self._is_completed

    @is_completed.setter
    def is_completed(self, value: bool):
        self._is_completed = value

    @property
    def is_new(self) -> bool:
        return self._is_new

    @property
    def is_primary(self) -> bool:
        return self._generated_route.is_primary

    # endregion

    def accept(self):
        self._is_new = False

    def equal_cities(self, city_a: str, city_b: str) -> bool:
        if self.city_a == city_a and self.city_b == city_b:
            return True

        if self.city_a == city_b and self.city_b == city_a:
            return True

        return False

    def get_points(self) -> List[Point]:
        return self._generated_route.get_all_points()

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'RouteWrapper':
        generated_route = data.get(cls.FIELD_GENERATED_ROUTE_KEY)

        return cls(
            generated_route=GenRoute.from_dict(generated_route),
            is_new=data.get(cls.FIELD_IS_NEW_KEY),
            is_completed=data.get(cls.FIELD_IS_COMPLETED)
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_GENERATED_ROUTE_KEY: self._generated_route.to_dict(),
            self.FIELD_IS_NEW_KEY: self._is_new,
            self.FIELD_IS_COMPLETED: self._is_completed
        }

    # endregion
