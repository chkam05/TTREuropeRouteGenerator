from typing import Optional, Dict, List

from core.models.generator.gen_route import GenRoute
from core.routes_generator import RoutesGenerator
from models.route_wrapper import RouteWrapper


class Game:
    FIELD_NAME_KEY = 'name'
    FILED_HOST_KEY = 'host'
    FIELD_ROUTES_PER_PLAYER_KEY = 'routes_per_player'

    def __init__(self,
                 name: str,
                 host: str,
                 routes_per_player: Optional[Dict[str, List[RouteWrapper]]] = None):
        self.name = name
        self.host = host
        self.routes_per_player: Dict[str, List[RouteWrapper]] = routes_per_player if routes_per_player else {host: []}
        self.used_routes: List[RouteWrapper] = Game._flatten_routes(routes_per_player)

    @staticmethod
    def _flatten_routes(routes_per_player: Optional[Dict[str, List[RouteWrapper]]] = None) -> List[RouteWrapper]:
        return [route for _, routes in routes_per_player.items() for route in routes] if routes_per_player else []

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'Game':
        routes_per_player = data.get(cls.FIELD_ROUTES_PER_PLAYER_KEY, {})

        return cls(
            name=data.get(cls.FIELD_NAME_KEY),
            host=data.get(cls.FILED_HOST_KEY, 'ADMIN'),
            routes_per_player={player: [RouteWrapper.from_dict(r) for r in routes]
                               for player, routes in routes_per_player.items()}
        )

    def to_dict(self) -> dict:
        routes_per_player = {player: [r.to_dict() for r in routes]
                             for player, routes in self.routes_per_player.items()}

        return {
            self.FIELD_NAME_KEY: self.name,
            self.FILED_HOST_KEY: self.host,
            self.FIELD_ROUTES_PER_PLAYER_KEY: routes_per_player
        }

    # endregion

    def accept_routes(self, nickname: str):
        for route in [r for r in self.get_player_routes(nickname) if r.is_new]:
            route.accept()

    def add_player(self, nickname: str):
        if not self.has_player(nickname):
            self.routes_per_player[nickname] = []

    def count_new_routes(self, nickname: str) -> int:
        if not self.has_player(nickname):
            return 0
        return len([r for r in self.get_player_routes(nickname) if r.is_new])

    def create_primary_route(self, generator: RoutesGenerator, nickname: str):
        if not generator or not self.has_player(nickname):
            return

        if self.has_primary_route(nickname):
            return

        tries = 20

        while tries > 0:
            primary_route = generator.generate_primary_route()

            if not self.is_used_route(primary_route):
                route_wrapper = RouteWrapper(primary_route, False)
                self.used_routes.append(route_wrapper)
                self.routes_per_player[nickname].append(route_wrapper)
                return

            tries -= 1

    def create_routes(self, generator: RoutesGenerator, nickname: str):
        if not generator or not self.has_player(nickname):
            return

        new_routes = []
        tries = 20

        while tries > 0:
            route = generator.generate_route()

            if not self.is_used_route(route):
                new_routes.append(RouteWrapper(route))

                if len(new_routes) == 3:
                    break
                continue

            tries -= 1

        if len(new_routes) == 3:
            self.used_routes.extend(new_routes)
            self.routes_per_player[nickname].extend(new_routes)

    def find_player_route_by_cities(self, city_a: str, city_b: str, nickname: str) -> Optional[RouteWrapper]:
        if not self.has_player(nickname):
            return None

        return next((r for r in self.get_player_routes(nickname) if r.equal_cities(city_a, city_b)), None)

    def find_route_by_cities(self, city_a: str, city_b: str) -> Optional[RouteWrapper]:
        return next((r for r in self.used_routes if r.equal_cities(city_a, city_b)), None)

    def get_player_routes(self, nickname: str) -> List[RouteWrapper]:
        if self.has_player(nickname):
            return self.routes_per_player[nickname]
        return []

    def has_player(self, nickname: str) -> bool:
        return nickname in self.routes_per_player

    def has_primary_route(self, nickname: str) -> bool:
        if not self.has_player(nickname):
            return False
        return any(r.is_primary for r in self.get_player_routes(nickname))

    def is_used_route(self, route: GenRoute) -> bool:
        return self.find_route_by_cities(route.city_a, route.city_b) is not None

    def remove_route(self, city_a: str, city_b: str, nickname: str):
        route = self.find_player_route_by_cities(city_a, city_b, nickname)

        if not route:
            return

        if route in self.used_routes:
            self.used_routes.remove(route)

        if route in self.routes_per_player[nickname]:
            self.routes_per_player[nickname].remove(route)
