from typing import Optional


class SshKeys:

    def __init__(self, public_key: str, private_key: Optional[str] = None):
        self._public_key = public_key
        self._private_key = private_key

    # region --- PROPERTIES ---

    @property
    def private_key(self) -> str:
        return self._private_key

    @property
    def public_key(self) -> str:
        return self._public_key

    # endregion
