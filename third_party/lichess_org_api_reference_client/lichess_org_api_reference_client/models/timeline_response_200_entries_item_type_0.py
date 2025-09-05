from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.timeline_response_200_entries_item_type_0_type import TimelineResponse200EntriesItemType0Type
from typing import cast

if TYPE_CHECKING:
  from ..models.timeline_response_200_entries_item_type_0_data import TimelineResponse200EntriesItemType0Data





T = TypeVar("T", bound="TimelineResponse200EntriesItemType0")



@_attrs_define
class TimelineResponse200EntriesItemType0:
    """ 
        Attributes:
            type_ (TimelineResponse200EntriesItemType0Type):
            date (float):
            data (TimelineResponse200EntriesItemType0Data):
     """

    type_: TimelineResponse200EntriesItemType0Type
    date: float
    data: 'TimelineResponse200EntriesItemType0Data'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.timeline_response_200_entries_item_type_0_data import TimelineResponse200EntriesItemType0Data
        type_ = self.type_.value

        date = self.date

        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "date": date,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeline_response_200_entries_item_type_0_data import TimelineResponse200EntriesItemType0Data
        d = dict(src_dict)
        type_ = TimelineResponse200EntriesItemType0Type(d.pop("type"))




        date = d.pop("date")

        data = TimelineResponse200EntriesItemType0Data.from_dict(d.pop("data"))




        timeline_response_200_entries_item_type_0 = cls(
            type_=type_,
            date=date,
            data=data,
        )


        timeline_response_200_entries_item_type_0.additional_properties = d
        return timeline_response_200_entries_item_type_0

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
