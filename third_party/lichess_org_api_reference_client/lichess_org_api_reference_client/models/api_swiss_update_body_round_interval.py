from enum import IntEnum

class ApiSwissUpdateBodyRoundInterval(IntEnum):
    VALUE_NEGATIVE_1 = -1
    VALUE_5 = 5
    VALUE_10 = 10
    VALUE_20 = 20
    VALUE_30 = 30
    VALUE_45 = 45
    VALUE_60 = 60
    VALUE_120 = 120
    VALUE_180 = 180
    VALUE_300 = 300
    VALUE_600 = 600
    VALUE_900 = 900
    VALUE_1200 = 1200
    VALUE_1800 = 1800
    VALUE_2700 = 2700
    VALUE_3600 = 3600
    VALUE_86400 = 86400
    VALUE_172800 = 172800
    VALUE_604800 = 604800
    VALUE_99999999 = 99999999

    def __str__(self) -> str:
        return str(self.value)
