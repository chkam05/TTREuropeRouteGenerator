from core.enums.direction_enum import DirectionEnum


class DirectionEnumHelper:
    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @staticmethod
    def from_str(str_value: str) -> DirectionEnum:
        return next((gt for gt in DirectionEnum if gt.value == str_value), DirectionEnum.CENTER)

    @staticmethod
    def get_list() -> list:
        return [direction_enum.value for direction_enum in DirectionEnum]

    @staticmethod
    def to_str(direction_enum: DirectionEnum) -> str:
        return direction_enum.value
