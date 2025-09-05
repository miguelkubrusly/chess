from enum import Enum

class TimelineResponse200EntriesItemType7Type(str, Enum):
    GAME_END = "game-end"

    def __str__(self) -> str:
        return str(self.value)
