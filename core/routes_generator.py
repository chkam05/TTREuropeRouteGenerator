import heapq
import random

from typing import Tuple, Dict, List, Optional

from core.models.generator.gen_route import GenRoute
from core.models.generator.gen_route_part import GenRoutePart
from core.models.route import Route
from core.models.world_map import WorldMap


PathStep = Tuple[str, str, Route]
RouteGraph = Dict[str, List[Tuple[str, int, Route]]]
ShortestPath = Tuple[Optional[List[PathStep]], float]


class RoutesGenerator:
    MAX_DISTANCE = 10
    MAX_POINTS = 18
    MIN_DISTANCE = 3
    MIN_POINTS = 5
    PRIMARY_EXTRA_POINTS = 10
    PRIMARY_MAX_DISTANCE = 999
    PRIMARY_MIN_DISTANCE = 7
    PRIMARY_MIN_POINTS = 20
    TRIES = 20

    def __init__(self, world_map: WorldMap, max_distance: int = MAX_DISTANCE, min_distance: int = MIN_DISTANCE):
        self.max_distance = max_distance
        self.min_distance = min_distance

        self._world_map = world_map
        self._graph = self._build_graph()

    def _build_graph(self) -> RouteGraph:
        graph = {}
        for route in self._world_map.routes:
            weight = route.length
            graph.setdefault(route.city_a.name, []).append((route.city_b.name, weight, route))
            graph.setdefault(route.city_b.name, []).append((route.city_a.name, weight, route))
        return graph

    def _calculate_route_points(self, path: List[PathStep], primary: bool = False) -> int:
        weight_sum = int(round(sum([route.get_weight() for _, _, route in path])))

        if primary:
            return max(self.PRIMARY_MIN_POINTS, weight_sum + self.PRIMARY_EXTRA_POINTS)
        else:
            return max(self.MIN_POINTS, min(self.MAX_POINTS, weight_sum))

    def _find_shortest_path(self, start: str, end: str) -> ShortestPath:
        queue = [(0, start, [])]
        visited = set()

        while queue:
            total_weight, city, path = heapq.heappop(queue)
            if city in visited:
                continue
            visited.add(city)

            if city == end:
                return path, total_weight

            for neighbor, weight, option in self._graph.get(city, []):
                heapq.heappush(queue, (total_weight + weight, neighbor, path + [(city, neighbor, option)]))

        return None, float('inf')

    def _generate_route(self,
                        primary: bool,
                        min_distance: int,
                        max_distance: int,
                        tries: int = 20) -> Optional[GenRoute]:
        start_cities = [city for key, city in self._world_map.cities.items() if not primary or city.edge_point]

        while tries > 0:
            start_city = random.choice(start_cities)

            if primary:
                potential_ends = [city for key, city in self._world_map.cities.items()
                                  if city.name != start_city.name
                                  and city.edge_point
                                  and city.is_opposite_direction(start_city.direction)]
            else:
                potential_ends = [city for key, city in self._world_map.cities.items()
                                  if city.name != start_city.name]

            if not any(potential_ends):
                tries -= 1
                continue

            end_city = random.choice(potential_ends)
            path, length = self._find_shortest_path(start_city.name, end_city.name)

            if path and min_distance <= len(path) <= max_distance:
                parts = [GenRoutePart.from_route(r) for _, _, r in path]
                total_points = self._calculate_route_points(path, primary)

                return GenRoute(city_a=start_city.name, city_b=end_city.name, points=total_points, parts=parts,
                                is_primary=primary)

            tries -= 1

        return None

    def generate_primary_route(self, tries: int = TRIES) -> Optional[GenRoute]:
        return self._generate_route(True, self.PRIMARY_MIN_DISTANCE, self.PRIMARY_MAX_DISTANCE, tries)

    def generate_route(self,
                       min_distance: int = MIN_DISTANCE,
                       max_distance: int = MAX_DISTANCE,
                       tries: int = TRIES) -> Optional[GenRoute]:
        return self._generate_route(False, min_distance, max_distance, tries)
