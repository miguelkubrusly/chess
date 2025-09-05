from enum import Enum

class TimelineEntryGameEndType(str, Enum):
    GAME_END = "game-end"

    def __str__(self) -> str:
        return str(self.value)
