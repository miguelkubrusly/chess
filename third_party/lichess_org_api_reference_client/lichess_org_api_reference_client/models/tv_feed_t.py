from enum import Enum

class TvFeedT(str, Enum):
    FEATURED = "featured"
    FEN = "fen"

    def __str__(self) -> str:
        return str(self.value)
