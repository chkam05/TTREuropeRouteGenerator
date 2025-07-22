from typing import Optional, Dict

from core.models.world_map import WorldMap
from core.routes_generator import RoutesGenerator
from models.game import Game
from models.player import Player
from static.language_keys import LanguageKeys
from utils.file_utils import FileUtils


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

    # region --- LOAD & SAVE ---

    @staticmethod
    def from_dict(data: dict) -> 'DataContainer':
        games = data.get(DataContainer.FIELD_GAMES_KEY, {})
        players = data.get(DataContainer.FIELD_PLAYERS_KEY, {})

        return DataContainer(
            language=data.get(DataContainer.FIELD_LANG_KEY, LanguageKeys.LANG_EN_US),
            games={game_name: Game.from_dict(game) for game_name, game in games.items()},
            players={nickname: Player.from_dict(player) for nickname, player in players.items()}
        )

    @staticmethod
    def load_from_file(file_path: str) -> 'DataContainer':
        if not FileUtils.file_exists(file_path):
            raise Exception(f'File \"{file_path}\" not found.')

        raw_data = FileUtils.read_json(file_path)
        return DataContainer.from_dict(raw_data)

    def to_dict(self) -> dict:
        games = {game_name: game.to_dict() for game_name, game in self._games.items()}
        players = {nickname: player.to_dict() for nickname, player in self._players.items()}

        return {
            self.FIELD_LANG_KEY: self._language,
            self.FIELD_GAMES_KEY: games,
            self.FIELD_PLAYERS_KEY: players
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
