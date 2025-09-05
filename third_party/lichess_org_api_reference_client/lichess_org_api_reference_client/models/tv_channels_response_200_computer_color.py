from enum import Enum

class TvChannelsResponse200ComputerColor(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
