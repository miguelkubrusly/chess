from enum import Enum

class ApiExternalEngineListResponse200ItemVariantsItem(str, Enum):
    ANTICHESS = "antichess"
    ATOMIC = "atomic"
    CHESS = "chess"
    CRAZYHOUSE = "crazyhouse"
    HORDE = "horde"
    KINGOFTHEHILL = "kingofthehill"
    RACINGKINGS = "racingkings"
    VALUE_7 = "3check"

    def __str__(self) -> str:
        return str(self.value)
