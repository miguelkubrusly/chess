from enum import Enum

class UserPreferencesTheme3D(str, Enum):
    BLACK_WHITE_ALUMINIUM = "Black-White-Aluminium"
    BRUSHED_ALUMINIUM = "Brushed-Aluminium"
    CHINA_BLUE = "China-Blue"
    CHINA_GREEN = "China-Green"
    CHINA_GREY = "China-Grey"
    CHINA_SCARLET = "China-Scarlet"
    CLASSIC_BLUE = "Classic-Blue"
    GOLD_SILVER = "Gold-Silver"
    JADE = "Jade"
    LIGHT_WOOD = "Light-Wood"
    MARBLE = "Marble"
    POWER_COATED = "Power-Coated"
    ROSEWOOD = "Rosewood"
    WAX = "Wax"
    WOODI = "Woodi"

    def __str__(self) -> str:
        return str(self.value)
