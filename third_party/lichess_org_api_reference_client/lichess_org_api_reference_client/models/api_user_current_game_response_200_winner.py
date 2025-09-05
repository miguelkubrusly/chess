from enum import Enum

class ApiUserCurrentGameResponse200Winner(str, Enum):
    BLACK = "black"
    WHITE = "white"

    def __str__(self) -> str:
        return str(self.value)
