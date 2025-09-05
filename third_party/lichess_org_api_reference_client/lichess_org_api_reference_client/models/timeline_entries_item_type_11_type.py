from enum import Enum

class TimelineEntriesItemType11Type(str, Enum):
    PLAN_RENEW = "plan-renew"

    def __str__(self) -> str:
        return str(self.value)
