from enum import Enum

class ChallengeListResponse200InItemSpeed(str, Enum):
    BLITZ = "blitz"
    BULLET = "bullet"
    CLASSICAL = "classical"
    CORRESPONDENCE = "correspondence"
    RAPID = "rapid"
    ULTRABULLET = "ultraBullet"

    def __str__(self) -> str:
        return str(self.value)
