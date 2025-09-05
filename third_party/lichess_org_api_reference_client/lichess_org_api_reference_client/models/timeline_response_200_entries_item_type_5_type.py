from enum import Enum

class TimelineResponse200EntriesItemType5Type(str, Enum):
    UBLOG_POST = "ublog-post"

    def __str__(self) -> str:
        return str(self.value)
