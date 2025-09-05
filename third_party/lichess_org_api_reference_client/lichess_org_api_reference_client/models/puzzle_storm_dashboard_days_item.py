from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PuzzleStormDashboardDaysItem")



@_attrs_define
class PuzzleStormDashboardDaysItem:
    """ 
        Attributes:
            field_id (str):
            combo (int):
            errors (int):
            highest (int):
            moves (int):
            runs (int):
            score (int):
            time (int):
     """

    field_id: str
    combo: int
    errors: int
    highest: int
    moves: int
    runs: int
    score: int
    time: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        combo = self.combo

        errors = self.errors

        highest = self.highest

        moves = self.moves

        runs = self.runs

        score = self.score

        time = self.time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "_id": field_id,
            "combo": combo,
            "errors": errors,
            "highest": highest,
            "moves": moves,
            "runs": runs,
            "score": score,
            "time": time,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("_id")

        combo = d.pop("combo")

        errors = d.pop("errors")

        highest = d.pop("highest")

        moves = d.pop("moves")

        runs = d.pop("runs")

        score = d.pop("score")

        time = d.pop("time")

        puzzle_storm_dashboard_days_item = cls(
            field_id=field_id,
            combo=combo,
            errors=errors,
            highest=highest,
            moves=moves,
            runs=runs,
            score=score,
            time=time,
        )


        puzzle_storm_dashboard_days_item.additional_properties = d
        return puzzle_storm_dashboard_days_item

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
