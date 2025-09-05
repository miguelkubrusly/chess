from enum import Enum

class TimelineEntriesItemType10Type(str, Enum):
    PLAN_START = "plan-start"

    def __str__(self) -> str:
        return str(self.value)
