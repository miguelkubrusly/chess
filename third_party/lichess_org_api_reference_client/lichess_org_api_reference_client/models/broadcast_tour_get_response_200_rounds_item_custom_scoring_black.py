from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="BroadcastTourGetResponse200RoundsItemCustomScoringBlack")



@_attrs_define
class BroadcastTourGetResponse200RoundsItemCustomScoringBlack:
    """ 
        Attributes:
            win (float):
            draw (float):
     """

    win: float
    draw: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        win = self.win

        draw = self.draw


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "win": win,
            "draw": draw,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        win = d.pop("win")

        draw = d.pop("draw")

        broadcast_tour_get_response_200_rounds_item_custom_scoring_black = cls(
            win=win,
            draw=draw,
        )


        broadcast_tour_get_response_200_rounds_item_custom_scoring_black.additional_properties = d
        return broadcast_tour_get_response_200_rounds_item_custom_scoring_black

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
