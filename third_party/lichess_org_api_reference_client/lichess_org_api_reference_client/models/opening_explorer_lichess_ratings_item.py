from enum import IntEnum

class OpeningExplorerLichessRatingsItem(IntEnum):
    VALUE_0 = 0
    VALUE_1000 = 1000
    VALUE_1200 = 1200
    VALUE_1400 = 1400
    VALUE_1600 = 1600
    VALUE_1800 = 1800
    VALUE_2000 = 2000
    VALUE_2200 = 2200
    VALUE_2500 = 2500

    def __str__(self) -> str:
        return str(self.value)
