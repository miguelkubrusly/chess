from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_push_response_200_games_item_tags import BroadcastPushResponse200GamesItemTags





T = TypeVar("T", bound="BroadcastPushResponse200GamesItem")



@_attrs_define
class BroadcastPushResponse200GamesItem:
    """ 
        Attributes:
            tags (BroadcastPushResponse200GamesItemTags):
            moves (Union[Unset, int]):
            error (Union[Unset, str]):
     """

    tags: 'BroadcastPushResponse200GamesItemTags'
    moves: Union[Unset, int] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_push_response_200_games_item_tags import BroadcastPushResponse200GamesItemTags
        tags = self.tags.to_dict()

        moves = self.moves

        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tags": tags,
        })
        if moves is not UNSET:
            field_dict["moves"] = moves
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_push_response_200_games_item_tags import BroadcastPushResponse200GamesItemTags
        d = dict(src_dict)
        tags = BroadcastPushResponse200GamesItemTags.from_dict(d.pop("tags"))




        moves = d.pop("moves", UNSET)

        error = d.pop("error", UNSET)

        broadcast_push_response_200_games_item = cls(
            tags=tags,
            moves=moves,
            error=error,
        )


        broadcast_push_response_200_games_item.additional_properties = d
        return broadcast_push_response_200_games_item

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
