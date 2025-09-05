from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GameEventInfoAIOpponent")



@_attrs_define
class GameEventInfoAIOpponent:
    """ 
        Attributes:
            id (None):
            username (str):
            ai (int): AI level, from 1 to 8, where 1 is the weakest and 8 is the strongest.
     """

    id: None
    username: str
    ai: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        ai = self.ai


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "username": username,
            "ai": ai,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        ai = d.pop("ai")

        game_event_info_ai_opponent = cls(
            id=id,
            username=username,
            ai=ai,
        )


        game_event_info_ai_opponent.additional_properties = d
        return game_event_info_ai_opponent

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
