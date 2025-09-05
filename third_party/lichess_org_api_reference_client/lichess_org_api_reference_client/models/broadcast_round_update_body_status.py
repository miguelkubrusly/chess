from enum import Enum

class BroadcastRoundUpdateBodyStatus(str, Enum):
    FINISHED = "finished"
    NEW = "new"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
