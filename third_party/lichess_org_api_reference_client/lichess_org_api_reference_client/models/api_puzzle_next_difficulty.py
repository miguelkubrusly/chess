from enum import Enum

class ApiPuzzleNextDifficulty(str, Enum):
    EASIER = "easier"
    EASIEST = "easiest"
    HARDER = "harder"
    HARDEST = "hardest"
    NORMAL = "normal"

    def __str__(self) -> str:
        return str(self.value)
