from enum import Enum

class AccountResponse200PrefsPieceSet3D(str, Enum):
    BASIC = "Basic"
    CUBESANDPI = "CubesAndPi"
    EXPERIMENTAL = "Experimental"
    GLASS = "Glass"
    METAL = "Metal"
    MODERNJADE = "ModernJade"
    MODERNWOOD = "ModernWood"
    REDVBLUE = "RedVBlue"
    STAUNTON = "Staunton"
    TRIMMED = "Trimmed"
    WOOD = "Wood"

    def __str__(self) -> str:
        return str(self.value)
