from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_storm_dashboard_response_200_days_item import ApiStormDashboardResponse200DaysItem
  from ..models.api_storm_dashboard_response_200_high import ApiStormDashboardResponse200High





T = TypeVar("T", bound="ApiStormDashboardResponse200")



@_attrs_define
class ApiStormDashboardResponse200:
    """ 
        Attributes:
            days (list['ApiStormDashboardResponse200DaysItem']):
            high (ApiStormDashboardResponse200High):
     """

    days: list['ApiStormDashboardResponse200DaysItem']
    high: 'ApiStormDashboardResponse200High'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_storm_dashboard_response_200_days_item import ApiStormDashboardResponse200DaysItem
        from ..models.api_storm_dashboard_response_200_high import ApiStormDashboardResponse200High
        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)



        high = self.high.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "days": days,
            "high": high,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_storm_dashboard_response_200_days_item import ApiStormDashboardResponse200DaysItem
        from ..models.api_storm_dashboard_response_200_high import ApiStormDashboardResponse200High
        d = dict(src_dict)
        days = []
        _days = d.pop("days")
        for days_item_data in (_days):
            days_item = ApiStormDashboardResponse200DaysItem.from_dict(days_item_data)



            days.append(days_item)


        high = ApiStormDashboardResponse200High.from_dict(d.pop("high"))




        api_storm_dashboard_response_200 = cls(
            days=days,
            high=high,
        )


        api_storm_dashboard_response_200.additional_properties = d
        return api_storm_dashboard_response_200

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
