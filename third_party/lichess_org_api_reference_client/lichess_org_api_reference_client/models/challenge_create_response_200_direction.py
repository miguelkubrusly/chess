from enum import Enum

class ChallengeCreateResponse200Direction(str, Enum):
    IN = "in"
    OUT = "out"

    def __str__(self) -> str:
        return str(self.value)
