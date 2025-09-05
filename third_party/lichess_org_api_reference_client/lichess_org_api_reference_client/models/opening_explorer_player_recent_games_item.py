from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.opening_explorer_player_recent_games_item_mode import OpeningExplorerPlayerRecentGamesItemMode
from ..models.opening_explorer_player_recent_games_item_speed import OpeningExplorerPlayerRecentGamesItemSpeed
from ..models.opening_explorer_player_recent_games_item_winner import OpeningExplorerPlayerRecentGamesItemWinner
from typing import cast

if TYPE_CHECKING:
  from ..models.opening_explorer_player_recent_games_item_black import OpeningExplorerPlayerRecentGamesItemBlack
  from ..models.opening_explorer_player_recent_games_item_white import OpeningExplorerPlayerRecentGamesItemWhite





T = TypeVar("T", bound="OpeningExplorerPlayerRecentGamesItem")



@_attrs_define
class OpeningExplorerPlayerRecentGamesItem:
    """ 
        Attributes:
            uci (str):
            id (str):
            winner (OpeningExplorerPlayerRecentGamesItemWinner):
            speed (OpeningExplorerPlayerRecentGamesItemSpeed):
            mode (OpeningExplorerPlayerRecentGamesItemMode):
            white (OpeningExplorerPlayerRecentGamesItemWhite):
            black (OpeningExplorerPlayerRecentGamesItemBlack):
            year (float):
            month (str):
     """

    uci: str
    id: str
    winner: OpeningExplorerPlayerRecentGamesItemWinner
    speed: OpeningExplorerPlayerRecentGamesItemSpeed
    mode: OpeningExplorerPlayerRecentGamesItemMode
    white: 'OpeningExplorerPlayerRecentGamesItemWhite'
    black: 'OpeningExplorerPlayerRecentGamesItemBlack'
    year: float
    month: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_player_recent_games_item_black import OpeningExplorerPlayerRecentGamesItemBlack
        from ..models.opening_explorer_player_recent_games_item_white import OpeningExplorerPlayerRecentGamesItemWhite
        uci = self.uci

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
            "uci": uci,
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
        from ..models.opening_explorer_player_recent_games_item_black import OpeningExplorerPlayerRecentGamesItemBlack
        from ..models.opening_explorer_player_recent_games_item_white import OpeningExplorerPlayerRecentGamesItemWhite
        d = dict(src_dict)
        uci = d.pop("uci")

        id = d.pop("id")

        winner = OpeningExplorerPlayerRecentGamesItemWinner(d.pop("winner"))




        speed = OpeningExplorerPlayerRecentGamesItemSpeed(d.pop("speed"))




        mode = OpeningExplorerPlayerRecentGamesItemMode(d.pop("mode"))




        white = OpeningExplorerPlayerRecentGamesItemWhite.from_dict(d.pop("white"))




        black = OpeningExplorerPlayerRecentGamesItemBlack.from_dict(d.pop("black"))




        year = d.pop("year")

        month = d.pop("month")

        opening_explorer_player_recent_games_item = cls(
            uci=uci,
            id=id,
            winner=winner,
            speed=speed,
            mode=mode,
            white=white,
            black=black,
            year=year,
            month=month,
        )


        opening_explorer_player_recent_games_item.additional_properties = d
        return opening_explorer_player_recent_games_item

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
