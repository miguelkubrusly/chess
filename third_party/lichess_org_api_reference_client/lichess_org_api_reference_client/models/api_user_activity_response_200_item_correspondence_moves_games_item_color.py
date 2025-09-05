from enum import Enum

class ApiUserActivityResponse200ItemCorrespondenceMovesGamesItemColor(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
