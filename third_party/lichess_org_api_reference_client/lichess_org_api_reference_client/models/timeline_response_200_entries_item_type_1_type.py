from enum import Enum

class TimelineResponse200EntriesItemType1Type(str, Enum):
    TEAM_JOIN = "team-join"

    def __str__(self) -> str:
        return str(self.value)
