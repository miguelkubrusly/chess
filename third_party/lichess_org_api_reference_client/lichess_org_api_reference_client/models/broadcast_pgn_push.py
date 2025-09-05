from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.broadcast_pgn_push_games_item import BroadcastPgnPushGamesItem





T = TypeVar("T", bound="BroadcastPgnPush")



@_attrs_define
class BroadcastPgnPush:
    """ 
        Attributes:
            games (list['BroadcastPgnPushGamesItem']):
     """

    games: list['BroadcastPgnPushGamesItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_pgn_push_games_item import BroadcastPgnPushGamesItem
        games = []
        for games_item_data in self.games:
            games_item = games_item_data.to_dict()
            games.append(games_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "games": games,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_pgn_push_games_item import BroadcastPgnPushGamesItem
        d = dict(src_dict)
        games = []
        _games = d.pop("games")
        for games_item_data in (_games):
            games_item = BroadcastPgnPushGamesItem.from_dict(games_item_data)



            games.append(games_item)


        broadcast_pgn_push = cls(
            games=games,
        )


        broadcast_pgn_push.additional_properties = d
        return broadcast_pgn_push

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
