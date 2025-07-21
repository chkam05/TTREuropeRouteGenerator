from core.enums.color_enum import ColorEnum


class ColorEnumHelper:
    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @staticmethod
    def from_str(str_value: str) -> ColorEnum:
        return next((gt for gt in ColorEnum if gt.value == str_value), ColorEnum.TRANSPARENT)

    @staticmethod
    def get_list() -> list:
        return [color_enum.value for color_enum in ColorEnum]

    @staticmethod
    def to_str(color_enum: ColorEnum) -> str:
        return color_enum.value
