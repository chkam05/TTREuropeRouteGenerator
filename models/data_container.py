from typing import Optional, Dict

from core.models.world_map import WorldMap
from core.routes_generator import RoutesGenerator
from models.game import Game
from models.player import Player
from static.language_keys import LanguageKeys


class DataContainer:
    FIELD_LANG_KEY = 'lang'
    FIELD_GAMES_KEY = 'games'
    FIELD_PLAYERS_KEY = 'players'

    def __init__(self,
                 language: Optional[str] = None,
                 games: Optional[Dict[str, Game]] = None,
                 players: Optional[Dict[str, Player]] = None):
        self._language = language if language else LanguageKeys.LANG_EN_US
        self._games: Dict[str, Game] = games if games else {}
        self._players: Dict[str, Player] = players if players else {}

        self._generator = RoutesGenerator(WorldMap.create_default())

    # region --- PROPERTIES ---

    @property
    def generator(self) -> RoutesGenerator:
        return self._generator

    @property
    def language(self) -> str:
        return self._language

    # endregion

    # region --- GAME ---

    def create_game(self, game_name: str, player: Player) -> Optional[Game]:
        if not self.has_game(game_name):
            new_game = Game(game_name, player.nickname)
            self._games[game_name] = new_game
            return new_game
        return None

    def get_game(self, game_name: str) -> Optional[Game]:
        if self.has_game(game_name):
            return self._games[game_name]
        return None

    def has_game(self, game_name: str) -> bool:
        return game_name in self._games

    # endregion

    # region --- PLAYER ---

    def create_player(self, nickname: str) -> Optional[Player]:
        if not self.has_player(nickname):
            new_player = Player(nickname, '')
            self._players[nickname] = new_player
            return new_player
        return None

    def get_or_create_player(self, nickname: str) -> Player:
        return self.get_player(nickname) if self.has_player(nickname) else self.create_player(nickname)

    def get_player(self, nickname: str) -> Optional[Player]:
        if self.has_player(nickname):
            return self._players[nickname]
        return None

    def has_player(self, nickname: str):
        return nickname in self._players

    # endregion