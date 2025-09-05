from enum import Enum

class TimelineEntriesItemType0Type(str, Enum):
    FOLLOW = "follow"

    def __str__(self) -> str:
        return str(self.value)
