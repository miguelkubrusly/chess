from enum import Enum

class ApiPuzzleNextResponse200GamePerfKey(str, Enum):
    ANTICHESS = "antichess"
    ATOMIC = "atomic"
    BLITZ = "blitz"
    BULLET = "bullet"
    CHESS960 = "chess960"
    CLASSICAL = "classical"
    CORRESPONDENCE = "correspondence"
    CRAZYHOUSE = "crazyhouse"
    HORDE = "horde"
    KINGOFTHEHILL = "kingOfTheHill"
    RACINGKINGS = "racingKings"
    RAPID = "rapid"
    THREECHECK = "threeCheck"
    ULTRABULLET = "ultraBullet"

    def __str__(self) -> str:
        return str(self.value)
