from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.broadcast_push_response_200_games_item import BroadcastPushResponse200GamesItem





T = TypeVar("T", bound="BroadcastPushResponse200")



@_attrs_define
class BroadcastPushResponse200:
    """ 
        Attributes:
            games (list['BroadcastPushResponse200GamesItem']):
     """

    games: list['BroadcastPushResponse200GamesItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_push_response_200_games_item import BroadcastPushResponse200GamesItem
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
        from ..models.broadcast_push_response_200_games_item import BroadcastPushResponse200GamesItem
        d = dict(src_dict)
        games = []
        _games = d.pop("games")
        for games_item_data in (_games):
            games_item = BroadcastPushResponse200GamesItem.from_dict(games_item_data)



            games.append(games_item)


        broadcast_push_response_200 = cls(
            games=games,
        )


        broadcast_push_response_200.additional_properties = d
        return broadcast_push_response_200

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
