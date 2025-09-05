from enum import Enum

class BroadcastTopActiveItemTourInfoFideTc(str, Enum):
    BLITZ = "blitz"
    RAPID = "rapid"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
