from typing import List, Tuple

from core.enums.color_enum import ColorEnum
from core.models.generator.gen_route_part import GenRoutePart
from core.models.point import Point


class GenRoute:
    FIELD_CITY_A_KEY = 'city_a'
    FIELD_CITY_B_KEY = 'city_b'
    FIELD_POINTS_KEY = 'points'
    FIELD_PARTS_KEY = 'parts'
    FIELD_IS_PRIMARY_KEY = 'is_primary'

    def __init__(self,
                 city_a: str,
                 city_b: str,
                 points: int,
                 parts: List[GenRoutePart],
                 is_primary: bool = False):
        self.city_a = city_a
        self.city_b = city_b
        self.points = points
        self.parts: List[GenRoutePart] = parts if parts else []
        self.is_primary = is_primary

    @staticmethod
    def _get_edge_points(segments: List[List[Point]]) -> Tuple[Point, Point]:
        found_segments = {}

        for segment in segments:
            for coord in segment:
                if not coord in found_segments:
                    found_segments[coord] = 1
                else:
                    found_segments[coord] += 1

        ep_coords = [point for point, length in found_segments.items() if length == 1]
        return ep_coords[0], ep_coords[1]

    def get_all_points(self) -> List[Point]:
        segments = [part.points for part in self.parts]
        start, end = self._get_edge_points(segments)

        coordinates = [start]

        while len(segments) > 0:
            found_segment = None

            for segment in segments:
                if segment[0] == coordinates[-1]:
                    coordinates.append(segment[1])
                    found_segment = segment
                    break
                elif segment[1] == coordinates[-1]:
                    coordinates.append(segment[0])
                    found_segment = segment
                    break

            if found_segment:
                segments.remove(found_segment)
                found_segment = None
            else:
                raise Exception('Lack of continuity of route segments')

        return coordinates

    # region --- LOAD & SAVE ---

    @staticmethod
    def from_dict(data: dict) -> 'GenRoute':
        parts = data.get(GenRoute.FIELD_PARTS_KEY, [])

        return GenRoute(city_a=data.get(GenRoute.FIELD_CITY_A_KEY), city_b=data.get(GenRoute.FIELD_CITY_B_KEY),
                        points=data.get(GenRoute.FIELD_POINTS_KEY, 1),
                        parts=[GenRoutePart.from_dict(part) for part in parts],
                        is_primary=data.get(GenRoute.FIELD_IS_PRIMARY_KEY, False))

    def to_dict(self) -> dict:
        return {
            self.FIELD_CITY_A_KEY: self.city_a,
            self.FIELD_CITY_B_KEY: self.city_b,
            self.FIELD_POINTS_KEY: self.points,
            self.FIELD_PARTS_KEY: [part.to_dict() for part in self.parts],
            self.FIELD_IS_PRIMARY_KEY: self.is_primary
        }

    # endregion
