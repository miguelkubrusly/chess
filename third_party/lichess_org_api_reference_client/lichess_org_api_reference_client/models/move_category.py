from enum import Enum

class MoveCategory(str, Enum):
    BLESSED_LOSS = "blessed-loss"
    CURSED_WIN = "cursed-win"
    DRAW = "draw"
    LOSS = "loss"
    MAYBE_LOSS = "maybe-loss"
    MAYBE_WIN = "maybe-win"
    SYZYGY_LOSS = "syzygy-loss"
    SYZYGY_WIN = "syzygy-win"
    UNKNOWN = "unknown"
    WIN = "win"

    def __str__(self) -> str:
        return str(self.value)
