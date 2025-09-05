from enum import Enum

class ChallengeCreateResponse200Status(str, Enum):
    ACCEPTED = "accepted"
    CANCELED = "canceled"
    CREATED = "created"
    DECLINED = "declined"
    OFFLINE = "offline"

    def __str__(self) -> str:
        return str(self.value)
