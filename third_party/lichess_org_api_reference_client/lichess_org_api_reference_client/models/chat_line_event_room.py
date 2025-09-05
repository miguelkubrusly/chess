from enum import Enum

class ChatLineEventRoom(str, Enum):
    PLAYER = "player"
    SPECTATOR = "spectator"

    def __str__(self) -> str:
        return str(self.value)
