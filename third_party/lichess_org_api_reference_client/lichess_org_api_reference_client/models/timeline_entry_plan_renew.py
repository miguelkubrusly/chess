from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.timeline_entry_plan_renew_type import TimelineEntryPlanRenewType
from typing import cast

if TYPE_CHECKING:
  from ..models.timeline_entry_plan_renew_data import TimelineEntryPlanRenewData





T = TypeVar("T", bound="TimelineEntryPlanRenew")



@_attrs_define
class TimelineEntryPlanRenew:
    """ 
        Attributes:
            type_ (TimelineEntryPlanRenewType):
            date (float):
            data (TimelineEntryPlanRenewData):
     """

    type_: TimelineEntryPlanRenewType
    date: float
    data: 'TimelineEntryPlanRenewData'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.timeline_entry_plan_renew_data import TimelineEntryPlanRenewData
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
        from ..models.timeline_entry_plan_renew_data import TimelineEntryPlanRenewData
        d = dict(src_dict)
        type_ = TimelineEntryPlanRenewType(d.pop("type"))




        date = d.pop("date")

        data = TimelineEntryPlanRenewData.from_dict(d.pop("data"))




        timeline_entry_plan_renew = cls(
            type_=type_,
            date=date,
            data=data,
        )


        timeline_entry_plan_renew.additional_properties = d
        return timeline_entry_plan_renew

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
