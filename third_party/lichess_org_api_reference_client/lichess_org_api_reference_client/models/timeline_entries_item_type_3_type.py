from enum import Enum

class TimelineEntriesItemType3Type(str, Enum):
    FORUM_POST = "forum-post"

    def __str__(self) -> str:
        return str(self.value)
