from enum import Enum

class TvChannelsResponse200Chess960Color(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
