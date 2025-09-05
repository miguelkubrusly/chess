from enum import Enum

class OpeningExplorerLichessResponse200MovesItemGameType0WinnerType3Type1(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
