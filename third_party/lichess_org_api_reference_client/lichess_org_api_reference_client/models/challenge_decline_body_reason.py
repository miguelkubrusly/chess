from enum import Enum

class ChallengeDeclineBodyReason(str, Enum):
    CASUAL = "casual"
    GENERIC = "generic"
    LATER = "later"
    NOBOT = "noBot"
    ONLYBOT = "onlyBot"
    RATED = "rated"
    STANDARD = "standard"
    TIMECONTROL = "timeControl"
    TOOFAST = "tooFast"
    TOOSLOW = "tooSlow"
    VARIANT = "variant"

    def __str__(self) -> str:
        return str(self.value)
