from enum import Enum

class StreamerLiveResponse200ItemStreamService(str, Enum):
    TWITCH = "twitch"
    YOUTUBE = "youTube"

    def __str__(self) -> str:
        return str(self.value)
