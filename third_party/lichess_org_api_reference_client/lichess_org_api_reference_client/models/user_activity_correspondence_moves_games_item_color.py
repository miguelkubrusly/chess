from enum import Enum

class UserActivityCorrespondenceMovesGamesItemColor(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
