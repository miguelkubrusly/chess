from enum import IntEnum

class ArenaTournamentsStartedItemStatus(IntEnum):
    VALUE_10 = 10
    VALUE_20 = 20
    VALUE_30 = 30

    def __str__(self) -> str:
        return str(self.value)
