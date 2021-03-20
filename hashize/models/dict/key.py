from typing import Any

class DictKeySet:
    def __init__(self, keys: list) -> None:
        self.keys = keys

    def __repr__(self) -> str:
    	return 'DictKeySet({})'.format(self.keys)

    def __len__(self) -> int:
    	return len(self.keys)

    def __contains__(self, other) -> bool:
        return other in self.keys

    def __getitem__(self, index: int) -> Any:
        return self.keys[index]

    def __setitem__(self, index: int, value: Any) -> list:
        self.keys[index] = value
        return self.keys

    def __eq__(self, other) -> bool:
        return other == self.keys

    def __nq__(self, other) -> bool:
        return other != self.keys

    def __gt__(self, other) -> bool:
        return other > len(self.keys)

    def __lt__(self, other) -> bool:
        return other < len(self.keys)

    def __le__(self, other) -> bool:
        return other <= len(self.keys)

    def __ge__(self, other) -> bool:
        return other >= len(self.keys)