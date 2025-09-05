from enum import Enum

class TimelineResponse200EntriesItemType2Type(str, Enum):
    TEAM_CREATE = "team-create"

    def __str__(self) -> str:
        return str(self.value)
