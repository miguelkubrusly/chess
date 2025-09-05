from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.opening_explorer_player_game_mode import OpeningExplorerPlayerGameMode
from ..models.opening_explorer_player_game_speed import OpeningExplorerPlayerGameSpeed
from ..models.opening_explorer_player_game_winner import OpeningExplorerPlayerGameWinner
from typing import cast

if TYPE_CHECKING:
  from ..models.opening_explorer_player_game_black import OpeningExplorerPlayerGameBlack
  from ..models.opening_explorer_player_game_white import OpeningExplorerPlayerGameWhite





T = TypeVar("T", bound="OpeningExplorerPlayerGame")



@_attrs_define
class OpeningExplorerPlayerGame:
    """ 
        Attributes:
            id (str):
            winner (OpeningExplorerPlayerGameWinner):
            speed (OpeningExplorerPlayerGameSpeed):
            mode (OpeningExplorerPlayerGameMode):
            white (OpeningExplorerPlayerGameWhite):
            black (OpeningExplorerPlayerGameBlack):
            year (float):
            month (str):
     """

    id: str
    winner: OpeningExplorerPlayerGameWinner
    speed: OpeningExplorerPlayerGameSpeed
    mode: OpeningExplorerPlayerGameMode
    white: 'OpeningExplorerPlayerGameWhite'
    black: 'OpeningExplorerPlayerGameBlack'
    year: float
    month: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_player_game_black import OpeningExplorerPlayerGameBlack
        from ..models.opening_explorer_player_game_white import OpeningExplorerPlayerGameWhite
        id = self.id

        winner = self.winner.value

        speed = self.speed.value

        mode = self.mode.value

        white = self.white.to_dict()

        black = self.black.to_dict()

        year = self.year

        month = self.month


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "winner": winner,
            "speed": speed,
            "mode": mode,
            "white": white,
            "black": black,
            "year": year,
            "month": month,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opening_explorer_player_game_black import OpeningExplorerPlayerGameBlack
        from ..models.opening_explorer_player_game_white import OpeningExplorerPlayerGameWhite
        d = dict(src_dict)
        id = d.pop("id")

        winner = OpeningExplorerPlayerGameWinner(d.pop("winner"))




        speed = OpeningExplorerPlayerGameSpeed(d.pop("speed"))




        mode = OpeningExplorerPlayerGameMode(d.pop("mode"))




        white = OpeningExplorerPlayerGameWhite.from_dict(d.pop("white"))




        black = OpeningExplorerPlayerGameBlack.from_dict(d.pop("black"))




        year = d.pop("year")

        month = d.pop("month")

        opening_explorer_player_game = cls(
            id=id,
            winner=winner,
            speed=speed,
            mode=mode,
            white=white,
            black=black,
            year=year,
            month=month,
        )


        opening_explorer_player_game.additional_properties = d
        return opening_explorer_player_game

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
