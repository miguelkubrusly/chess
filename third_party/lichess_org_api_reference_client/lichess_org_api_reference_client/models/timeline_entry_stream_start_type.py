from enum import Enum

class TimelineEntryStreamStartType(str, Enum):
    STREAM_START = "stream-start"

    def __str__(self) -> str:
        return str(self.value)
