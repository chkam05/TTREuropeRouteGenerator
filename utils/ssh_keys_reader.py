from typing import Tuple, Optional

from models.ssh_keys import SshKeys
from utils.file_utils import FileUtils


class SshKeysReader:

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @staticmethod
    def _read_ssh_public_key(key_file_content: str) -> str:
        key_lines = []
        for line in key_file_content.splitlines()[1:-1]:
            line = line.strip()
            if line.startswith('Comment:'):
                continue
            key_lines.append(line)
        return ''.join(key_lines)

    @staticmethod
    def _read_ssh_private_key(key_file_content: str) -> Tuple[str, str]:
        public_key_lines = []
        private_key_lines = []
        in_public = False
        in_private = False

        for line in key_file_content.splitlines():
            line = line.strip()

            if line.startswith('Public-Lines:'):
                in_public = True
                in_private = False
                continue

            if line.startswith('Private-Lines:'):
                in_public = False
                in_private = True
                continue

            if line.startswith('Private-MAC:'):
                break

            if in_public:
                public_key_lines.append(line)
            elif in_private:
                private_key_lines.append(line)

        return ''.join(public_key_lines), ''.join(private_key_lines)

    @staticmethod
    def read_ssh_public_key(file_path: str) -> Optional[SshKeys]:
        file_content = FileUtils.read_file(file_path)

        if not file_content:
            return None

        public_key = SshKeysReader._read_ssh_public_key(file_content)

        if not public_key:
            return None

        return SshKeys(public_key)

    @staticmethod
    def read_ssh_private_key(file_path: str) -> Optional[SshKeys]:
        file_content = FileUtils.read_file(file_path)

        if not file_content:
            return None

        public_key, private_key = SshKeysReader._read_ssh_private_key(file_content)

        if not public_key and not private_key:
            return None

        return SshKeys(public_key, private_key)
