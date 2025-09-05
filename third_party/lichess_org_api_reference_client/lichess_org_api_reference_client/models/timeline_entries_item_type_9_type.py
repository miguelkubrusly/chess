from enum import Enum

class TimelineEntriesItemType9Type(str, Enum):
    STUDY_LIKE = "study-like"

    def __str__(self) -> str:
        return str(self.value)
