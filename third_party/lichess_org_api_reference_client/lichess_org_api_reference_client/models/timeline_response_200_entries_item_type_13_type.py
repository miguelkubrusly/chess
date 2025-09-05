from enum import Enum

class TimelineResponse200EntriesItemType13Type(str, Enum):
    STREAM_START = "stream-start"

    def __str__(self) -> str:
        return str(self.value)
