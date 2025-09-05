from enum import Enum

class ChallengeDeclinedJsonStatus(str, Enum):
    ACCEPTED = "accepted"
    CANCELED = "canceled"
    CREATED = "created"
    DECLINED = "declined"
    OFFLINE = "offline"

    def __str__(self) -> str:
        return str(self.value)
