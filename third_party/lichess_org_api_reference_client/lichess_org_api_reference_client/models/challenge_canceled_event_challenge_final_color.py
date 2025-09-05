from enum import Enum

class ChallengeCanceledEventChallengeFinalColor(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
