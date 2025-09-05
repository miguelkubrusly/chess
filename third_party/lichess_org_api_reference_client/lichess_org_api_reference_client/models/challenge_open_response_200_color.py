from enum import Enum

class ChallengeOpenResponse200Color(str, Enum):
    BLACK = "black"
    RANDOM = "random"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
