from enum import IntEnum

class BroadcastTourCreateBodyTier(IntEnum):
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

    def __str__(self) -> str:
        return str(self.value)
