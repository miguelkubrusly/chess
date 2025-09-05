from enum import Enum

class ChallengeCanceledEventChallengeColor(str, Enum):
    BLACK = "black"
    RANDOM = "random"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
