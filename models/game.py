from typing import Optional, Dict, List

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
        self.used_routes: Game._flatten_routes(routes_per_player)

    @staticmethod
    def _flatten_routes(routes_per_player: Optional[Dict[str, List[RouteWrapper]]] = None):
        return [route for _, routes in routes_per_player.items() for route in routes] if routes_per_player else []

    # region --- LOAD & SAVE ---

    @staticmethod
    def from_dict(data: dict) -> 'Game':
        routes_per_player = data.get(Game.FIELD_ROUTES_PER_PLAYER_KEY, {})

        return Game(
            name=data.get(Game.FIELD_NAME_KEY),
            host=data.get(Game.FILED_HOST_KEY, 'ADMIN'),
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

    def add_player(self, nickname: str):
        if not self.has_player(nickname):
            self.routes_per_player[nickname] = []

    def get_player_routes(self, nickname: str) -> List[RouteWrapper]:
        if self.has_player(nickname):
            return self.routes_per_player[nickname]
        return []

    def has_player(self, nickname: str) -> bool:
        return nickname in self.routes_per_player
