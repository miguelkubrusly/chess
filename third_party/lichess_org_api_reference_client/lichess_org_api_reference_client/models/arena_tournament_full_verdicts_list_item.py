from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ArenaTournamentFullVerdictsListItem")



@_attrs_define
class ArenaTournamentFullVerdictsListItem:
    """ 
        Attributes:
            condition (str):
            verdict (str):
     """

    condition: str
    verdict: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        condition = self.condition

        verdict = self.verdict


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "condition": condition,
            "verdict": verdict,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition = d.pop("condition")

        verdict = d.pop("verdict")

        arena_tournament_full_verdicts_list_item = cls(
            condition=condition,
            verdict=verdict,
        )


        arena_tournament_full_verdicts_list_item.additional_properties = d
        return arena_tournament_full_verdicts_list_item

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
