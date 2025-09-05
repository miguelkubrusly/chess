from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ApiUserActivityResponse200ItemRacer")



@_attrs_define
class ApiUserActivityResponse200ItemRacer:
    """ 
        Attributes:
            runs (int):
            score (int):
     """

    runs: int
    score: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        runs = self.runs

        score = self.score


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "runs": runs,
            "score": score,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        runs = d.pop("runs")

        score = d.pop("score")

        api_user_activity_response_200_item_racer = cls(
            runs=runs,
            score=score,
        )


        api_user_activity_response_200_item_racer.additional_properties = d
        return api_user_activity_response_200_item_racer

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
