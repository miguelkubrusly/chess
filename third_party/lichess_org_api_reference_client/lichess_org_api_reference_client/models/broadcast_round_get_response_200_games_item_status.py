from enum import Enum

class BroadcastRoundGetResponse200GamesItemStatus(str, Enum):
    VALUE_0 = "*"
    VALUE_1 = "1-0"
    VALUE_2 = "0-1"
    VALUE_3 = "½-½"

    def __str__(self) -> str:
        return str(self.value)
