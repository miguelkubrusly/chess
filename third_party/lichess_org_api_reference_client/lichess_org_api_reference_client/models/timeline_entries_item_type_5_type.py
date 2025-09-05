from enum import Enum

class TimelineEntriesItemType5Type(str, Enum):
    UBLOG_POST = "ublog-post"

    def __str__(self) -> str:
        return str(self.value)
