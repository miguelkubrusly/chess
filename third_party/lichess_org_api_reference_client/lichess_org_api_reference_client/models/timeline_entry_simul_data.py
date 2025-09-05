from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TimelineEntrySimulData")



@_attrs_define
class TimelineEntrySimulData:
    """ 
        Attributes:
            user_id (str):
            simul_id (str):
            simul_name (str):
     """

    user_id: str
    simul_id: str
    simul_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        simul_id = self.simul_id

        simul_name = self.simul_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "userId": user_id,
            "simulId": simul_id,
            "simulName": simul_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        simul_id = d.pop("simulId")

        simul_name = d.pop("simulName")

        timeline_entry_simul_data = cls(
            user_id=user_id,
            simul_id=simul_id,
            simul_name=simul_name,
        )


        timeline_entry_simul_data.additional_properties = d
        return timeline_entry_simul_data

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
