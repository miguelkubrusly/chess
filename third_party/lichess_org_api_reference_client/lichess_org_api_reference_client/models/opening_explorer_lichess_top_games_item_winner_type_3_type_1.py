from enum import Enum

class OpeningExplorerLichessTopGamesItemWinnerType3Type1(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
