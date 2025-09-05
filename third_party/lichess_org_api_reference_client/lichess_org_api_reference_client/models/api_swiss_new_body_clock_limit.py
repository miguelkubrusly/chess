from enum import IntEnum

class ApiSwissNewBodyClockLimit(IntEnum):
    VALUE_0 = 0
    VALUE_15 = 15
    VALUE_30 = 30
    VALUE_45 = 45
    VALUE_60 = 60
    VALUE_90 = 90
    VALUE_120 = 120
    VALUE_180 = 180
    VALUE_240 = 240
    VALUE_300 = 300
    VALUE_360 = 360
    VALUE_420 = 420
    VALUE_480 = 480
    VALUE_600 = 600
    VALUE_900 = 900
    VALUE_1200 = 1200
    VALUE_1500 = 1500
    VALUE_1800 = 1800
    VALUE_2400 = 2400
    VALUE_3000 = 3000
    VALUE_3600 = 3600
    VALUE_4200 = 4200
    VALUE_4800 = 4800
    VALUE_5400 = 5400
    VALUE_6000 = 6000
    VALUE_6600 = 6600
    VALUE_7200 = 7200
    VALUE_7800 = 7800
    VALUE_8400 = 8400
    VALUE_9000 = 9000
    VALUE_9600 = 9600
    VALUE_10200 = 10200
    VALUE_10800 = 10800

    def __str__(self) -> str:
        return str(self.value)
