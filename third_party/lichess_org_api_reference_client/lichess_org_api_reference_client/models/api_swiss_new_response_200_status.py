from enum import Enum

class ApiSwissNewResponse200Status(str, Enum):
    CREATED = "created"
    FINISHED = "finished"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
