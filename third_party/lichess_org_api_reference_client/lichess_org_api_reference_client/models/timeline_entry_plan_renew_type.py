from enum import Enum

class TimelineEntryPlanRenewType(str, Enum):
    PLAN_RENEW = "plan-renew"

    def __str__(self) -> str:
        return str(self.value)
