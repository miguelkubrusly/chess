from enum import Enum

class TimelineResponse200EntriesItemType6Type(str, Enum):
    TOUR_JOIN = "tour-join"

    def __str__(self) -> str:
        return str(self.value)
