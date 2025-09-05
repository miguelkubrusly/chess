from enum import Enum

class ChallengeListResponse200InItemDirection(str, Enum):
    IN = "in"
    OUT = "out"

    def __str__(self) -> str:
        return str(self.value)
