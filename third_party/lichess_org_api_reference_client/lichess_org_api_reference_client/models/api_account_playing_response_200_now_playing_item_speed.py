from enum import Enum

class ApiAccountPlayingResponse200NowPlayingItemSpeed(str, Enum):
    BLITZ = "blitz"
    BULLET = "bullet"
    CLASSICAL = "classical"
    CORRESPONDENCE = "correspondence"
    RAPID = "rapid"
    ULTRABULLET = "ultraBullet"

    def __str__(self) -> str:
        return str(self.value)
