from enum import Enum

class TimelineResponse200EntriesItemType10Type(str, Enum):
    PLAN_START = "plan-start"

    def __str__(self) -> str:
        return str(self.value)
