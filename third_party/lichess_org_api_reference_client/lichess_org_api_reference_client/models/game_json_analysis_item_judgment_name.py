from enum import Enum

class GameJsonAnalysisItemJudgmentName(str, Enum):
    BLUNDER = "Blunder"
    INACCURACY = "Inaccuracy"
    MISTAKE = "Mistake"

    def __str__(self) -> str:
        return str(self.value)
