from enum import Enum

class ApiGamesUserSort(str, Enum):
    DATEASC = "dateAsc"
    DATEDESC = "dateDesc"

    def __str__(self) -> str:
        return str(self.value)
