import json
import os


class FileUtils:
    _INVALID_CHARACTERS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static utility class and cannot be instantiated.")

    @staticmethod
    def ensure_folder_for_file(file_path: str):
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

    @staticmethod
    def file_exists(file_path: str) -> bool:
        return os.path.isfile(file_path)

    @staticmethod
    def get_file_extension(file_path: str) -> str:
        return os.path.splitext(file_path)[1].lower()

    @staticmethod
    def is_valid_file_path(path: str) -> bool:
        # Ends with separator = catalog not file
        if not path or path.endswith(os.path.sep):
            return False

        directory, filename = os.path.split(path)

        # File name must be present
        if not filename:
            return False

        # Illegal characters in file name (mainly for Windows)
        for char in FileUtils._INVALID_CHARACTERS:
            if char in filename:
                return False

        # Check if the path can be normalized (e.g. without NULL characters)
        try:
            norm_path = os.path.normpath(path)
            if '\0' in norm_path:  # NULL character
                return False
        except (Exception,):
            return False

        return True

    @staticmethod
    def read_file(file_path: str, encoding: str = 'utf-8') -> str:
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()

    @staticmethod
    def read_json(file_path: str, encoding: str = 'utf-8') -> dict | list:
        content = FileUtils.read_file(file_path, encoding)
        return json.loads(content)

    @staticmethod
    def save_file(file_path: str, content: str, encoding: str = 'utf-8'):
        FileUtils.ensure_folder_for_file(file_path)
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)

    @staticmethod
    def save_json(file_path: str, content: dict | list, encoding: str = 'utf-8'):
        json_string = json.dumps(content, indent=4, ensure_ascii=False)
        FileUtils.save_file(file_path, json_string, encoding)
