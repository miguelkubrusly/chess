from enum import IntEnum

class GameFinishEventGameStatusId(IntEnum):
    VALUE_10 = 10
    VALUE_20 = 20
    VALUE_25 = 25
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_37 = 37
    VALUE_38 = 38
    VALUE_39 = 39
    VALUE_60 = 60

    def __str__(self) -> str:
        return str(self.value)
