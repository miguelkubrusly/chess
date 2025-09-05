from enum import Enum

class TimelineEntryTeamCreateType(str, Enum):
    TEAM_CREATE = "team-create"

    def __str__(self) -> str:
        return str(self.value)
