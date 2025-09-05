from enum import Enum

class OpeningExplorerPlayerModesItem(str, Enum):
    CASUAL = "casual"
    RATED = "rated"

    def __str__(self) -> str:
        return str(self.value)
