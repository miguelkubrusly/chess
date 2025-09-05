from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast
from typing import Union






T = TypeVar("T", bound="OpponentGoneEvent")



@_attrs_define
class OpponentGoneEvent:
    """ 
        Example:
            {'type': 'opponentGone', 'gone': True, 'claimWinInSeconds': 8}

        Attributes:
            type_ (Literal['opponentGone']):
            gone (bool):
            claim_win_in_seconds (Union[Unset, int]):
     """

    type_: Literal['opponentGone']
    gone: bool
    claim_win_in_seconds: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        gone = self.gone

        claim_win_in_seconds = self.claim_win_in_seconds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "gone": gone,
        })
        if claim_win_in_seconds is not UNSET:
            field_dict["claimWinInSeconds"] = claim_win_in_seconds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['opponentGone'] , d.pop("type"))
        if type_ != 'opponentGone':
            raise ValueError(f"type must match const 'opponentGone', got '{type_}'")

        gone = d.pop("gone")

        claim_win_in_seconds = d.pop("claimWinInSeconds", UNSET)

        opponent_gone_event = cls(
            type_=type_,
            gone=gone,
            claim_win_in_seconds=claim_win_in_seconds,
        )


        opponent_gone_event.additional_properties = d
        return opponent_gone_event

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
