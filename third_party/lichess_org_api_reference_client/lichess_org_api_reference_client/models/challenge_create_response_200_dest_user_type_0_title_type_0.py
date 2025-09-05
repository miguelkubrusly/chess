from enum import Enum

class ChallengeCreateResponse200DestUserType0TitleType0(str, Enum):
    BOT = "BOT"
    CM = "CM"
    FM = "FM"
    GM = "GM"
    IM = "IM"
    LM = "LM"
    NM = "NM"
    WCM = "WCM"
    WFM = "WFM"
    WGM = "WGM"
    WIM = "WIM"
    WNM = "WNM"

    def __str__(self) -> str:
        return str(self.value)
