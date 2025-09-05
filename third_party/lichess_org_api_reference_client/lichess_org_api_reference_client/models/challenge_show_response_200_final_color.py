from enum import Enum

class ChallengeShowResponse200FinalColor(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
