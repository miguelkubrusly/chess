from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.broadcast_round_update_response_200_games_item_players_item_title import BroadcastRoundUpdateResponse200GamesItemPlayersItemTitle
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="BroadcastRoundUpdateResponse200GamesItemPlayersItem")



@_attrs_define
class BroadcastRoundUpdateResponse200GamesItemPlayersItem:
    """ 
        Attributes:
            name (Union[Unset, str]):
            title (Union[Unset, BroadcastRoundUpdateResponse200GamesItemPlayersItemTitle]): only appears if the user is a
                titled player or a bot user
            rating (Union[Unset, int]):
            fide_id (Union[Unset, int]):
            fed (Union[Unset, str]):
            clock (Union[Unset, int]):
     """

    name: Union[Unset, str] = UNSET
    title: Union[Unset, BroadcastRoundUpdateResponse200GamesItemPlayersItemTitle] = UNSET
    rating: Union[Unset, int] = UNSET
    fide_id: Union[Unset, int] = UNSET
    fed: Union[Unset, str] = UNSET
    clock: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value


        rating = self.rating

        fide_id = self.fide_id

        fed = self.fed

        clock = self.clock


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if rating is not UNSET:
            field_dict["rating"] = rating
        if fide_id is not UNSET:
            field_dict["fideId"] = fide_id
        if fed is not UNSET:
            field_dict["fed"] = fed
        if clock is not UNSET:
            field_dict["clock"] = clock

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _title = d.pop("title", UNSET)
        title: Union[Unset, BroadcastRoundUpdateResponse200GamesItemPlayersItemTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = BroadcastRoundUpdateResponse200GamesItemPlayersItemTitle(_title)




        rating = d.pop("rating", UNSET)

        fide_id = d.pop("fideId", UNSET)

        fed = d.pop("fed", UNSET)

        clock = d.pop("clock", UNSET)

        broadcast_round_update_response_200_games_item_players_item = cls(
            name=name,
            title=title,
            rating=rating,
            fide_id=fide_id,
            fed=fed,
            clock=clock,
        )


        broadcast_round_update_response_200_games_item_players_item.additional_properties = d
        return broadcast_round_update_response_200_games_item_players_item

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
