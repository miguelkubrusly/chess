from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="OpeningExplorerPlayerMovesItemOpeningType0")



@_attrs_define
class OpeningExplorerPlayerMovesItemOpeningType0:
    """ 
        Attributes:
            eco (str):
            name (str):
     """

    eco: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        eco = self.eco

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "eco": eco,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        eco = d.pop("eco")

        name = d.pop("name")

        opening_explorer_player_moves_item_opening_type_0 = cls(
            eco=eco,
            name=name,
        )


        opening_explorer_player_moves_item_opening_type_0.additional_properties = d
        return opening_explorer_player_moves_item_opening_type_0

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
