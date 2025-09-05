from enum import Enum

class OpeningExplorerPlayerGameMode(str, Enum):
    CASUAL = "casual"
    RATED = "rated"

    def __str__(self) -> str:
        return str(self.value)
