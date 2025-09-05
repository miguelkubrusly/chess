from enum import Enum

class OpeningExplorerLichessResponse200TopGamesItemWinnerType2Type1(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
