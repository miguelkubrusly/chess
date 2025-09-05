from enum import Enum

class BroadcastTourGetResponse200TourInfoFideTc(str, Enum):
    BLITZ = "blitz"
    RAPID = "rapid"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
