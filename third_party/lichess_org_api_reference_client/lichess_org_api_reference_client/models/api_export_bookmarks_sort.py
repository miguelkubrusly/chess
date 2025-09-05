from enum import Enum

class ApiExportBookmarksSort(str, Enum):
    DATEASC = "dateAsc"
    DATEDESC = "dateDesc"

    def __str__(self) -> str:
        return str(self.value)
