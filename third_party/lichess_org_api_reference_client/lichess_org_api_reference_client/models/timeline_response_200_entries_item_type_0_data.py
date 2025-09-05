from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TimelineResponse200EntriesItemType0Data")



@_attrs_define
class TimelineResponse200EntriesItemType0Data:
    """ 
        Attributes:
            u1 (str):
            u2 (str):
     """

    u1: str
    u2: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        u1 = self.u1

        u2 = self.u2


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "u1": u1,
            "u2": u2,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        u1 = d.pop("u1")

        u2 = d.pop("u2")

        timeline_response_200_entries_item_type_0_data = cls(
            u1=u1,
            u2=u2,
        )


        timeline_response_200_entries_item_type_0_data.additional_properties = d
        return timeline_response_200_entries_item_type_0_data

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
