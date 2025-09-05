from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.puzzle_storm_dashboard_days_item import PuzzleStormDashboardDaysItem
  from ..models.puzzle_storm_dashboard_high import PuzzleStormDashboardHigh





T = TypeVar("T", bound="PuzzleStormDashboard")



@_attrs_define
class PuzzleStormDashboard:
    """ 
        Attributes:
            days (list['PuzzleStormDashboardDaysItem']):
            high (PuzzleStormDashboardHigh):
     """

    days: list['PuzzleStormDashboardDaysItem']
    high: 'PuzzleStormDashboardHigh'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.puzzle_storm_dashboard_days_item import PuzzleStormDashboardDaysItem
        from ..models.puzzle_storm_dashboard_high import PuzzleStormDashboardHigh
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
        from ..models.puzzle_storm_dashboard_days_item import PuzzleStormDashboardDaysItem
        from ..models.puzzle_storm_dashboard_high import PuzzleStormDashboardHigh
        d = dict(src_dict)
        days = []
        _days = d.pop("days")
        for days_item_data in (_days):
            days_item = PuzzleStormDashboardDaysItem.from_dict(days_item_data)



            days.append(days_item)


        high = PuzzleStormDashboardHigh.from_dict(d.pop("high"))




        puzzle_storm_dashboard = cls(
            days=days,
            high=high,
        )


        puzzle_storm_dashboard.additional_properties = d
        return puzzle_storm_dashboard

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
