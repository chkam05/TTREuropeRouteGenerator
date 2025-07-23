from core.enums.direction_enum import DirectionEnum


class DirectionEnumHelper:
    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @classmethod
    def from_str(cls, str_value: str) -> DirectionEnum:
        return next((gt for gt in DirectionEnum if gt.value == str_value), DirectionEnum.CENTER)

    @classmethod
    def get_list(cls) -> list:
        return [direction_enum.value for direction_enum in DirectionEnum]

    @classmethod
    def to_str(cls, direction_enum: DirectionEnum) -> str:
        return direction_enum.value
