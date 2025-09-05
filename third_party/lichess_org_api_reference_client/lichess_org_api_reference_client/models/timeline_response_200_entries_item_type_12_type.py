from enum import Enum

class TimelineResponse200EntriesItemType12Type(str, Enum):
    UBLOG_POST_LIKE = "ublog-post-like"

    def __str__(self) -> str:
        return str(self.value)
