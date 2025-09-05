from enum import Enum

class TimelineEntryFollowType(str, Enum):
    FOLLOW = "follow"

    def __str__(self) -> str:
        return str(self.value)
