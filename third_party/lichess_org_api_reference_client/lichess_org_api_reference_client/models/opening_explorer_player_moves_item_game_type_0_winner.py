from enum import Enum

class OpeningExplorerPlayerMovesItemGameType0Winner(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
