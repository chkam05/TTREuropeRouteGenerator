class Point:
    FIELD_X_KEY = 'x'
    FIELD_Y_KEY = 'y'

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    # region --- LOAD & SAVE ---

    @staticmethod
    def from_dict(data: dict) -> 'Point':
        return Point(
            x=data.get(Point.FIELD_X_KEY),
            y=data.get(Point.FIELD_Y_KEY)
        )

    def to_dict(self) -> dict:
        return {
            self.FIELD_X_KEY: self.x,
            self.FIELD_Y_KEY: self.y
        }

    # endregion
