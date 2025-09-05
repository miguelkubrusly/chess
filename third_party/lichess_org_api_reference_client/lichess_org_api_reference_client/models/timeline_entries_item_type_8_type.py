from enum import Enum

class TimelineEntriesItemType8Type(str, Enum):
    SIMUL_CREATE = "simul-create"
    SIMUL_JOIN = "simul-join"

    def __str__(self) -> str:
        return str(self.value)
