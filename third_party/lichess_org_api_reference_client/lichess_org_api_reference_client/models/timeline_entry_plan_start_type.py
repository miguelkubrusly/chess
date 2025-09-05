from enum import Enum

class TimelineEntryPlanStartType(str, Enum):
    PLAN_START = "plan-start"

    def __str__(self) -> str:
        return str(self.value)
