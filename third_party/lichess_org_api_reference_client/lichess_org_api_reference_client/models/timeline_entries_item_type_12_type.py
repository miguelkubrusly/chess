from enum import Enum

class TimelineEntriesItemType12Type(str, Enum):
    UBLOG_POST_LIKE = "ublog-post-like"

    def __str__(self) -> str:
        return str(self.value)
