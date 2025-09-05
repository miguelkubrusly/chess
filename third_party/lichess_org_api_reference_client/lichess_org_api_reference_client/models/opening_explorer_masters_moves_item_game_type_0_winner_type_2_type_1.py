from enum import Enum

class OpeningExplorerMastersMovesItemGameType0WinnerType2Type1(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
