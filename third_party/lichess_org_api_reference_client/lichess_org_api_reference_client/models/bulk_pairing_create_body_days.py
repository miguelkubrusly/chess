from enum import IntEnum

class BulkPairingCreateBodyDays(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_5 = 5
    VALUE_7 = 7
    VALUE_10 = 10
    VALUE_14 = 14

    def __str__(self) -> str:
        return str(self.value)
