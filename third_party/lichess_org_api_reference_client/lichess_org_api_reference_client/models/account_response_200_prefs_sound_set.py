from enum import Enum

class AccountResponse200PrefsSoundSet(str, Enum):
    FUTURISTIC = "futuristic"
    MUSIC = "music"
    NES = "nes"
    PIANO = "piano"
    ROBOT = "robot"
    SFX = "sfx"
    SILENT = "silent"
    SPEECH = "speech"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
