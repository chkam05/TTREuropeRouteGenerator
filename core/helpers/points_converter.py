class PointsConverter:
    _POINTS_PER_LENGTH = {
        1: 1,
        2: 2,
        3: 4,
        4: 7,
        6: 15,
        8: 21
    }

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @classmethod
    def convert_length_to_points(cls, length: int) -> int:
        return cls._POINTS_PER_LENGTH[length]

    @classmethod
    def convert_points_to_length(cls, points: int) -> int:
        return next((key for key, val in cls._POINTS_PER_LENGTH.items() if val == points), 0)
