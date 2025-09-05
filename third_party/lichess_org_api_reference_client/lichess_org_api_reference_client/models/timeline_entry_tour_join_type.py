from enum import Enum

class TimelineEntryTourJoinType(str, Enum):
    TOUR_JOIN = "tour-join"

    def __str__(self) -> str:
        return str(self.value)
