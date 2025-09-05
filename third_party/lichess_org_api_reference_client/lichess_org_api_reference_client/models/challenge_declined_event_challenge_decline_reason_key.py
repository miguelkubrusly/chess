from enum import Enum

class ChallengeDeclinedEventChallengeDeclineReasonKey(str, Enum):
    CASUAL = "casual"
    GENERIC = "generic"
    LATER = "later"
    NOBOT = "nobot"
    ONLYBOT = "onlybot"
    RATED = "rated"
    STANDARD = "standard"
    TIMECONTROL = "timecontrol"
    TOOFAST = "toofast"
    TOOSLOW = "tooslow"
    VARIANT = "variant"

    def __str__(self) -> str:
        return str(self.value)
