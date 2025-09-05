from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.arena_tournaments_finished_item_perf_key import ArenaTournamentsFinishedItemPerfKey
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ArenaTournamentsFinishedItemPerf")



@_attrs_define
class ArenaTournamentsFinishedItemPerf:
    """ 
        Attributes:
            key (ArenaTournamentsFinishedItemPerfKey):
            name (str):  Example: Blitz.
            position (int):  Example: 1.
            icon (Union[Unset, str]):  Example: ).
     """

    key: ArenaTournamentsFinishedItemPerfKey
    name: str
    position: int
    icon: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        name = self.name

        position = self.position

        icon = self.icon


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "name": name,
            "position": position,
        })
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = ArenaTournamentsFinishedItemPerfKey(d.pop("key"))




        name = d.pop("name")

        position = d.pop("position")

        icon = d.pop("icon", UNSET)

        arena_tournaments_finished_item_perf = cls(
            key=key,
            name=name,
            position=position,
            icon=icon,
        )


        arena_tournaments_finished_item_perf.additional_properties = d
        return arena_tournaments_finished_item_perf

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
