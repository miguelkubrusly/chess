from enum import Enum

class OpeningExplorerMastersGameWinnerType3Type1(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
