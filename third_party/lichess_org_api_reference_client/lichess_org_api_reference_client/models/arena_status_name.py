from enum import Enum

class ArenaStatusName(str, Enum):
    CREATED = "created"
    FINISHED = "finished"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
