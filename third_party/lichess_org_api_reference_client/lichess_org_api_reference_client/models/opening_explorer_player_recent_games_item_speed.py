from enum import Enum

class OpeningExplorerPlayerRecentGamesItemSpeed(str, Enum):
    BLITZ = "blitz"
    BULLET = "bullet"
    CLASSICAL = "classical"
    CORRESPONDENCE = "correspondence"
    RAPID = "rapid"
    ULTRABULLET = "ultraBullet"

    def __str__(self) -> str:
        return str(self.value)
