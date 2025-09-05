from enum import Enum

class TimelineEntriesItemType1Type(str, Enum):
    TEAM_JOIN = "team-join"

    def __str__(self) -> str:
        return str(self.value)
