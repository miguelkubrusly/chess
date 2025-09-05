from enum import Enum

class ApiSwissUpdateBodyVariant(str, Enum):
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
