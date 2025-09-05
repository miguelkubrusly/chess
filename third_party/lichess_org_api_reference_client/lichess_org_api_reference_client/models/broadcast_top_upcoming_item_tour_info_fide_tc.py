from enum import Enum

class BroadcastTopUpcomingItemTourInfoFideTc(str, Enum):
    BLITZ = "blitz"
    RAPID = "rapid"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
