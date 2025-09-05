from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.opening_explorer_player_moves_item_game_type_0_mode import OpeningExplorerPlayerMovesItemGameType0Mode
from ..models.opening_explorer_player_moves_item_game_type_0_speed import OpeningExplorerPlayerMovesItemGameType0Speed
from ..models.opening_explorer_player_moves_item_game_type_0_winner import OpeningExplorerPlayerMovesItemGameType0Winner
from typing import cast

if TYPE_CHECKING:
  from ..models.opening_explorer_player_moves_item_game_type_0_white import OpeningExplorerPlayerMovesItemGameType0White
  from ..models.opening_explorer_player_moves_item_game_type_0_black import OpeningExplorerPlayerMovesItemGameType0Black





T = TypeVar("T", bound="OpeningExplorerPlayerMovesItemGameType0")



@_attrs_define
class OpeningExplorerPlayerMovesItemGameType0:
    """ 
        Attributes:
            id (str):
            winner (OpeningExplorerPlayerMovesItemGameType0Winner):
            speed (OpeningExplorerPlayerMovesItemGameType0Speed):
            mode (OpeningExplorerPlayerMovesItemGameType0Mode):
            white (OpeningExplorerPlayerMovesItemGameType0White):
            black (OpeningExplorerPlayerMovesItemGameType0Black):
            year (float):
            month (str):
     """

    id: str
    winner: OpeningExplorerPlayerMovesItemGameType0Winner
    speed: OpeningExplorerPlayerMovesItemGameType0Speed
    mode: OpeningExplorerPlayerMovesItemGameType0Mode
    white: 'OpeningExplorerPlayerMovesItemGameType0White'
    black: 'OpeningExplorerPlayerMovesItemGameType0Black'
    year: float
    month: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_player_moves_item_game_type_0_white import OpeningExplorerPlayerMovesItemGameType0White
        from ..models.opening_explorer_player_moves_item_game_type_0_black import OpeningExplorerPlayerMovesItemGameType0Black
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
        from ..models.opening_explorer_player_moves_item_game_type_0_white import OpeningExplorerPlayerMovesItemGameType0White
        from ..models.opening_explorer_player_moves_item_game_type_0_black import OpeningExplorerPlayerMovesItemGameType0Black
        d = dict(src_dict)
        id = d.pop("id")

        winner = OpeningExplorerPlayerMovesItemGameType0Winner(d.pop("winner"))




        speed = OpeningExplorerPlayerMovesItemGameType0Speed(d.pop("speed"))




        mode = OpeningExplorerPlayerMovesItemGameType0Mode(d.pop("mode"))




        white = OpeningExplorerPlayerMovesItemGameType0White.from_dict(d.pop("white"))




        black = OpeningExplorerPlayerMovesItemGameType0Black.from_dict(d.pop("black"))




        year = d.pop("year")

        month = d.pop("month")

        opening_explorer_player_moves_item_game_type_0 = cls(
            id=id,
            winner=winner,
            speed=speed,
            mode=mode,
            white=white,
            black=black,
            year=year,
            month=month,
        )


        opening_explorer_player_moves_item_game_type_0.additional_properties = d
        return opening_explorer_player_moves_item_game_type_0

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
