from enum import Enum

class UserPreferencesPieceSet(str, Enum):
    ALPHA = "alpha"
    CALIFORNIA = "california"
    CARDINAL = "cardinal"
    CBURNETT = "cburnett"
    CHESS7 = "chess7"
    CHESSNUT = "chessnut"
    COMPANION = "companion"
    DUBROVNY = "dubrovny"
    FANTASY = "fantasy"
    FRESCA = "fresca"
    GIOCO = "gioco"
    GOVERNOR = "governor"
    ICPIECES = "icpieces"
    KOSAL = "kosal"
    LEIPZIG = "leipzig"
    LETTER = "letter"
    MAESTRO = "maestro"
    MERIDA = "merida"
    PIROUETTI = "pirouetti"
    PIXEL = "pixel"
    REILLYCRAIG = "reillycraig"
    RIOHACHA = "riohacha"
    SHAPES = "shapes"
    SPATIAL = "spatial"
    STAUNTY = "staunty"
    TATIANA = "tatiana"

    def __str__(self) -> str:
        return str(self.value)
