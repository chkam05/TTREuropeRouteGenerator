from datetime import datetime, timezone
from typing import Dict, Optional

from models.player_summary import PlayerSummary


class GameSummary:
    DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
    FIELD_GAME_NAME_KEY = 'game_name'
    FIELD_CREATION_DATE_KEY = 'creation_date'
    FIELD_PLAYER_SUMMARIES_KEY = 'player_summaries'

    def __init__(self, game_name: str,
                 player_summaries: Dict[str, PlayerSummary],
                 creation_date: Optional[datetime] = None):
        self.game_name = game_name
        self.creation_date = creation_date if creation_date else datetime.now()
        self.player_summaries: Dict[str, PlayerSummary] = player_summaries if player_summaries else {}

    def creation_date_to_str(self, format_: str = DATE_TIME_FORMAT, utc: bool = False) -> str:
        date_time = self.creation_date.astimezone(timezone.utc) if utc else self.creation_date
        return date_time.strftime(format_)

    @staticmethod
    def _str_to_date(date_time_str: str, format_: str = DATE_TIME_FORMAT, utc: bool = False):
        if date_time_str[-3] == ":":
            date_time_str = date_time_str[:-3] + date_time_str[-2:]

        dt = datetime.strptime(date_time_str, format_)
        if utc:
            dt = dt.astimezone(timezone.utc)
        return dt

    # region --- PROPERTIES ---

    @property
    def winner(self) -> str:
        top_player = max(self.player_summaries.values(), key=lambda p: p.points)
        return top_player.nickname

    # endregion

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'GameSummary':
        creation_dt_str = data.get(cls.FIELD_CREATION_DATE_KEY)
        player_summaries = data.get(cls.FIELD_PLAYER_SUMMARIES_KEY, {})

        return cls(
            game_name=data.get(cls.FIELD_GAME_NAME_KEY),
            creation_date=cls._str_to_date(creation_dt_str),
            player_summaries={nickname: PlayerSummary.from_dict(summary)
                              for nickname, summary in player_summaries.items()}
        )

    def to_dict(self) -> dict:
        creation_dt_str = self.creation_date_to_str()
        player_summaries = {nickname: summary.to_dict() for nickname, summary in self.player_summaries.items()}

        return {
            self.FIELD_GAME_NAME_KEY: self.game_name,
            self.FIELD_CREATION_DATE_KEY: creation_dt_str,
            self.FIELD_PLAYER_SUMMARIES_KEY: player_summaries
        }

    # endregion
