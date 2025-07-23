from core.enums.color_enum import ColorEnum


class ColorEnumHelper:
    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @classmethod
    def from_str(cls, str_value: str) -> ColorEnum:
        return next((gt for gt in ColorEnum if gt.value == str_value), ColorEnum.TRANSPARENT)

    @classmethod
    def get_list(cls) -> list:
        return [color_enum.value for color_enum in ColorEnum]

    @classmethod
    def to_str(cls, color_enum: ColorEnum) -> str:
        return color_enum.value
