from enum import Enum

class TimelineResponse200EntriesItemType0Type(str, Enum):
    FOLLOW = "follow"

    def __str__(self) -> str:
        return str(self.value)
