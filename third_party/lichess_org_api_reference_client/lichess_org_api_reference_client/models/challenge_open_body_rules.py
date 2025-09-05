from enum import Enum

class ChallengeOpenBodyRules(str, Enum):
    NOABORT = "noAbort"
    NOCLAIMWIN = "noClaimWin"
    NOEARLYDRAW = "noEarlyDraw"
    NOGIVETIME = "noGiveTime"
    NOREMATCH = "noRematch"

    def __str__(self) -> str:
        return str(self.value)
