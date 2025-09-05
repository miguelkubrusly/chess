from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.game_status_id import GameStatusId
from ..models.game_status_name import GameStatusName






T = TypeVar("T", bound="GameStatus")



@_attrs_define
class GameStatus:
    """ 
        Attributes:
            id (GameStatusId):
            name (GameStatusName):
     """

    id: GameStatusId
    name: GameStatusName
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        name = self.name.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = GameStatusId(d.pop("id"))




        name = GameStatusName(d.pop("name"))




        game_status = cls(
            id=id,
            name=name,
        )


        game_status.additional_properties = d
        return game_status

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
