from enum import Enum

class GameFullEventStateStatus(str, Enum):
    ABORTED = "aborted"
    CHEAT = "cheat"
    CREATED = "created"
    DRAW = "draw"
    INSUFFICIENTMATERIALCLAIM = "insufficientMaterialClaim"
    MATE = "mate"
    NOSTART = "noStart"
    OUTOFTIME = "outoftime"
    RESIGN = "resign"
    STALEMATE = "stalemate"
    STARTED = "started"
    TIMEOUT = "timeout"
    UNKNOWNFINISH = "unknownFinish"
    VARIANTEND = "variantEnd"

    def __str__(self) -> str:
        return str(self.value)
