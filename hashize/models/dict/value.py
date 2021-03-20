from typing import Any

class DictValueSet:
    def __init__(self, values: list) -> None:
        self.values = values

    def __repr__(self) -> str:
    	return 'DictValueSet({})'.format(self.values)

    def __len__(self) -> int:
    	return len(self.values)

    def __contains__(self, other) -> bool:
        return other in self.values

    def __getitem__(self, index: int) -> Any:
        return self.values[index]

    def __setitem__(self, index: int, value: Any) -> list:
        self.values[index] = value
        return self.values

    def __eq__(self, other) -> bool:
        return other == self.values

    def __nq__(self, other) -> bool:
        return other != self.values

    def __gt__(self, other) -> bool:
        return other > len(self.values)

    def __lt__(self, other) -> bool:
        return other < len(self.values)

    def __le__(self, other) -> bool:
        return other <= len(self.values)

    def __ge__(self, other) -> bool:
        return other >= len(self.values)