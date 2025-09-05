from enum import Enum

class TimelineResponse200EntriesItemType11Type(str, Enum):
    PLAN_RENEW = "plan-renew"

    def __str__(self) -> str:
        return str(self.value)
