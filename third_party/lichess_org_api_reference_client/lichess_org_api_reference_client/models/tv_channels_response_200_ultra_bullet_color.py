from enum import Enum

class TvChannelsResponse200UltraBulletColor(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
