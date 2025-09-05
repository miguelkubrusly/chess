from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ApiTournamentUpdateResponse200Perf")



@_attrs_define
class ApiTournamentUpdateResponse200Perf:
    """ 
        Attributes:
            icon (str):
            key (str):
            name (str):
     """

    icon: str
    key: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        icon = self.icon

        key = self.key

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "icon": icon,
            "key": key,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        icon = d.pop("icon")

        key = d.pop("key")

        name = d.pop("name")

        api_tournament_update_response_200_perf = cls(
            icon=icon,
            key=key,
            name=name,
        )


        api_tournament_update_response_200_perf.additional_properties = d
        return api_tournament_update_response_200_perf

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
