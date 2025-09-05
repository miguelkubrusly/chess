from enum import Enum

class TimelineEntryStudyLikeType(str, Enum):
    STUDY_LIKE = "study-like"

    def __str__(self) -> str:
        return str(self.value)
