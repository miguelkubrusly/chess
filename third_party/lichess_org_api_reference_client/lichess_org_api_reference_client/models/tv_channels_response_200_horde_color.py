from enum import Enum

class TvChannelsResponse200HordeColor(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
