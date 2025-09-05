from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="OpeningExplorerLichessHistoryItem")



@_attrs_define
class OpeningExplorerLichessHistoryItem:
    """ 
        Attributes:
            month (str):
            white (float):
            draws (float):
            black (float):
     """

    month: str
    white: float
    draws: float
    black: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        month = self.month

        white = self.white

        draws = self.draws

        black = self.black


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "month": month,
            "white": white,
            "draws": draws,
            "black": black,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        white = d.pop("white")

        draws = d.pop("draws")

        black = d.pop("black")

        opening_explorer_lichess_history_item = cls(
            month=month,
            white=white,
            draws=draws,
            black=black,
        )


        opening_explorer_lichess_history_item.additional_properties = d
        return opening_explorer_lichess_history_item

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
