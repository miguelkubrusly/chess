from enum import Enum

class UserPreferencesTheme(str, Enum):
    BLUE = "blue"
    BLUE2 = "blue2"
    BLUE3 = "blue3"
    BLUE_MARBLE = "blue-marble"
    BROWN = "brown"
    CANVAS = "canvas"
    GREEN = "green"
    GREEN_PLASTIC = "green-plastic"
    GREY = "grey"
    IC = "ic"
    LEATHER = "leather"
    MAPLE = "maple"
    MAPLE2 = "maple2"
    MARBLE = "marble"
    METAL = "metal"
    NEWSPAPER = "newspaper"
    OLIVE = "olive"
    PINK = "pink"
    PURPLE = "purple"
    PURPLE_DIAG = "purple-diag"
    WOOD = "wood"
    WOOD2 = "wood2"
    WOOD3 = "wood3"
    WOOD4 = "wood4"

    def __str__(self) -> str:
        return str(self.value)
