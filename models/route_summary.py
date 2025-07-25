class RouteSummary:
    FIELD_CITY_A_KEY = 'city_a'
    FIELD_CITY_B_KEY = 'city_b'
    FIELD_POINTS_KEY = 'points'
    FIELD_IS_PRIMARY_KEY = 'is_primary'
    FIELD_IS_COMPLETED_KEY = 'is_completed'

    def __init__(self, city_a: str, city_b: str, points: int, is_primary: bool, is_completed: bool):
        self.city_a = city_a
        self.city_b = city_b
        self.points = points
        self.is_primary = is_primary
        self.is_completed = is_completed

    # region --- LOAD & SAVE ---

    @classmethod
    def from_dict(cls, data: dict) -> 'RouteSummary':
        return cls(
            city_a=data.get(cls.FIELD_CITY_A_KEY),
            city_b=data.get(cls.FIELD_CITY_B_KEY),
            points=data.get(cls.FIELD_POINTS_KEY),
            is_primary=data.get(cls.FIELD_IS_PRIMARY_KEY),
            is_completed=data.get(cls.FIELD_IS_COMPLETED_KEY)
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_CITY_A_KEY: self.city_a,
            self.FIELD_CITY_B_KEY: self.city_b,
            self.FIELD_POINTS_KEY: self.points,
            self.FIELD_IS_PRIMARY_KEY: self.is_primary,
            self.FIELD_IS_COMPLETED_KEY: self.is_completed
        }

    # endregion
