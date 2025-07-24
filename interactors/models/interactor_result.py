from typing import Optional, Dict, List, Any


class InteractorResult:

    def __init__(self, success: bool, results: Optional[Dict[str, Any]] = None, error: Optional[str] = None):
        self._success = success
        self._results: Dict[str, Any] = results if results else {}
        self._error = error

    # region --- PROPERTIES ---

    @property
    def error(self) -> Optional[str]:
        return self._error

    @property
    def results(self) -> Dict[str, Any]:
        return {key: value for key, value in self._results.items()}

    @property
    def success(self) -> bool:
        return self._success

    # endregion

    def get(self, key: str, default: Any = None) -> Any:
        return self._results.get(key, default)

    def has_error(self) -> bool:
        return self._error is not None and len(self._error) > 0

    def has_result(self, key: str) -> bool:
        return key in self._results

    def has_results(self) -> bool:
        return any(self._results)
