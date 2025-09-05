from enum import Enum

class ApiAccountPlayingResponse200NowPlayingItemSource(str, Enum):
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
