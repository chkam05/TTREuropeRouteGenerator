from typing import Optional, Dict, List

from core.models.world_map import WorldMap
from core.routes_generator import RoutesGenerator
from models.game import Game
from models.game_summary import GameSummary
from models.player import Player
from models.player_summary import PlayerSummary
from models.route_summary import RouteSummary
from models.route_wrapper import RouteWrapper
from utils.file_utils import FileUtils


class DataContainer:
    FIELD_GAMES_KEY = 'games'
    FIELD_PLAYERS_KEY = 'players'
    FIELD_REFRESH_KEY = 'refresh'
    FIELD_SUMMARY_KEY = 'summary'

    def __init__(self,
                 games: Optional[Dict[str, Game]] = None,
                 players: Optional[Dict[str, Player]] = None,
                 refresh: Optional[Dict[str, bool]] = None,
                 summary: Optional[Dict[str, GameSummary]] = None):
        self._games: Dict[str, Game] = games if games else {}
        self._players: Dict[str, Player] = players if players else {}
        self._refresh: Dict[str, bool] = refresh if refresh else {}
        self._summary: Dict[str, GameSummary] = summary if summary else {}

        self._generator = RoutesGenerator(WorldMap.create_default())

    def have_refresh(self, nickname: str) -> bool:
        if nickname in self._refresh:
            have_refresh = self._refresh[nickname]
            self._refresh[nickname] = False
            return have_refresh
        return False

    def set_refresh(self, game_name: str, current_nickname: str):
        if self.has_game(game_name):
            for nickname in self.get_game(game_name).get_players():
                if nickname == current_nickname:
                    continue
                self._refresh[nickname] = True

    # region --- PROPERTIES ---

    @property
    def generator(self) -> RoutesGenerator:
        return self._generator

    # endregion

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'DataContainer':
        games = data.get(cls.FIELD_GAMES_KEY, {})
        players = data.get(cls.FIELD_PLAYERS_KEY, {})
        summaries = data.get(cls.FIELD_SUMMARY_KEY, {})

        return cls(
            games={game_name: Game.from_dict(game) for game_name, game in games.items()},
            players={nickname: Player.from_dict(player) for nickname, player in players.items()},
            refresh=data.get(cls.FIELD_REFRESH_KEY, {}),
            summary={nickname: GameSummary.from_dict(s) for nickname, s in summaries.items()}
        )

    @classmethod
    def load_from_file(cls, file_path: str) -> 'DataContainer':
        if not FileUtils.file_exists(file_path):
            raise Exception(f'File \"{file_path}\" not found.')

        raw_data = FileUtils.read_json(file_path)
        return cls.from_dict(raw_data)

    def to_dict(self) -> dict:
        games = {game_name: game.to_dict() for game_name, game in self._games.items()}
        players = {nickname: player.to_dict() for nickname, player in self._players.items()}
        summaries = {nickname: s.to_dict() for nickname, s in self._summary.items()}

        return {
            self.FIELD_GAMES_KEY: games,
            self.FIELD_PLAYERS_KEY: players,
            self.FIELD_REFRESH_KEY: self._refresh,
            self.FIELD_SUMMARY_KEY: summaries,
        }

    def save_to_file(self, file_path: str):
        if not FileUtils.is_valid_file_path(file_path):
            raise Exception(f'Invalid file path \"{file_path}\".')

        FileUtils.ensure_folder_for_file(file_path)
        FileUtils.save_json(file_path, self.to_dict())

    # endregion

    # region --- GAME ---

    def create_game(self, game_name: str, player: Player) -> Optional[Game]:
        if not self.has_game(game_name):
            new_game = Game(game_name, player.nickname)
            self._games[game_name] = new_game
            return new_game
        return None

    def end_game(self, game_name: str, player: Player) -> Optional[Game]:
        if self.is_host(game_name, player):
            game = self.get_game(game_name)
            self.create_summary(game.name, game.routes_per_player)
            del self._games[game_name]
            return game
        return None

    def get_game(self, game_name: str) -> Optional[Game]:
        if self.has_game(game_name):
            return self._games[game_name]
        return None

    def has_game(self, game_name: str) -> bool:
        return game_name in self._games

    def is_host(self, game_name: str, player: Player) -> bool:
        return self.has_game(game_name) and self._games[game_name].host == player.nickname

    # endregion

    # region --- PLAYER ---

    def create_player(self, nickname: str) -> Optional[Player]:
        if not self.has_player(nickname):
            new_player = Player(nickname, '')
            self._players[nickname] = new_player
            self._refresh[nickname] = False
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

    # region --- SUMMARY ---

    def create_summary(self, game_name: str, routes_per_player: Dict[str, List[RouteWrapper]]):
        player_summaries = {}

        for nickname, routes in routes_per_player.items():
            route_summaries = [RouteSummary(r.city_a, r.city_b, r.points, r.is_primary, r.is_completed)
                               for r in routes]
            player_summaries[nickname] = PlayerSummary(nickname, route_summaries)

        summary = GameSummary(game_name, player_summaries)
        self._summary[game_name] = summary

    def get_summary(self, game_name: str) -> Optional[GameSummary]:
        return self._summary[game_name] if self.has_summary(game_name) else None

    def has_summary(self, game_name: str) -> bool:
        return game_name in self._summary

    # endregion
