from enum import Enum

class ChallengeListResponse200OutItemVariantKey(str, Enum):
    ANTICHESS = "antichess"
    ATOMIC = "atomic"
    CHESS960 = "chess960"
    CRAZYHOUSE = "crazyhouse"
    FROMPOSITION = "fromPosition"
    HORDE = "horde"
    KINGOFTHEHILL = "kingOfTheHill"
    RACINGKINGS = "racingKings"
    STANDARD = "standard"
    THREECHECK = "threeCheck"

    def __str__(self) -> str:
        return str(self.value)
