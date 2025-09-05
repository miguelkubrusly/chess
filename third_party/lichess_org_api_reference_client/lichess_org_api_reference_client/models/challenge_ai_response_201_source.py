from enum import Enum

class ChallengeAiResponse201Source(str, Enum):
    AI = "ai"
    API = "api"
    FRIEND = "friend"
    IMPORT = "import"
    IMPORTLIVE = "importlive"
    LOBBY = "lobby"
    POOL = "pool"
    POSITION = "position"
    RELAY = "relay"
    SIMUL = "simul"
    SWISS = "swiss"
    TOURNAMENT = "tournament"

    def __str__(self) -> str:
        return str(self.value)
