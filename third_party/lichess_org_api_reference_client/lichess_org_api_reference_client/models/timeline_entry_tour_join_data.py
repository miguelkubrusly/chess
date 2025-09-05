from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TimelineEntryTourJoinData")



@_attrs_define
class TimelineEntryTourJoinData:
    """ 
        Attributes:
            user_id (str):
            tour_id (str):
            tour_name (str):
     """

    user_id: str
    tour_id: str
    tour_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        tour_id = self.tour_id

        tour_name = self.tour_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "userId": user_id,
            "tourId": tour_id,
            "tourName": tour_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        tour_id = d.pop("tourId")

        tour_name = d.pop("tourName")

        timeline_entry_tour_join_data = cls(
            user_id=user_id,
            tour_id=tour_id,
            tour_name=tour_name,
        )


        timeline_entry_tour_join_data.additional_properties = d
        return timeline_entry_tour_join_data

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
