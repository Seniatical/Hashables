from typing import Any

class DictItemSet:
    def __init__(self, items: list) -> None:
        self.items = items

    def __repr__(self) -> str:
    	return 'DictItemSet({})'.format(self.items)

    def __len__(self) -> int:
    	return len(self.items)

    def __contains__(self, other) -> bool:
        return other in self.items

    def __getitem__(self, index: int) -> Any:
        return self.items[index]

    def __setitem__(self, index: int, value: Any) -> list:
        self.items[index] = value
        return self.items

    def __eq__(self, other) -> bool:
        return other == self.items

    def __nq__(self, other) -> bool:
        return other != self.items

    def __gt__(self, other) -> bool:
        return other > len(self.items)

    def __lt__(self, other) -> bool:
        return other < len(self.items)

    def __le__(self, other) -> bool:
        return other <= len(self.items)

    def __ge__(self, other) -> bool:
        return other >= len(self.items)

    def to_dict(self):
        return dict(self.items)