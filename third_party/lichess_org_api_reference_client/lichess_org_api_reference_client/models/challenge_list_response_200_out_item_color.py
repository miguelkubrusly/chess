from enum import Enum

class ChallengeListResponse200OutItemColor(str, Enum):
    BLACK = "black"
    RANDOM = "random"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
