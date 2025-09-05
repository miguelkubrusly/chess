from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PuzzleStormDashboardHigh")



@_attrs_define
class PuzzleStormDashboardHigh:
    """ 
        Attributes:
            all_time (int):
            day (int):
            month (int):
            week (int):
     """

    all_time: int
    day: int
    month: int
    week: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        all_time = self.all_time

        day = self.day

        month = self.month

        week = self.week


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "allTime": all_time,
            "day": day,
            "month": month,
            "week": week,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_time = d.pop("allTime")

        day = d.pop("day")

        month = d.pop("month")

        week = d.pop("week")

        puzzle_storm_dashboard_high = cls(
            all_time=all_time,
            day=day,
            month=month,
            week=week,
        )


        puzzle_storm_dashboard_high.additional_properties = d
        return puzzle_storm_dashboard_high

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
