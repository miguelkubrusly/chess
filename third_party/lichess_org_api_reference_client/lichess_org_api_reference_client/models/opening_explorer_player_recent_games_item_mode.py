from enum import Enum

class OpeningExplorerPlayerRecentGamesItemMode(str, Enum):
    CASUAL = "casual"
    RATED = "rated"

    def __str__(self) -> str:
        return str(self.value)
