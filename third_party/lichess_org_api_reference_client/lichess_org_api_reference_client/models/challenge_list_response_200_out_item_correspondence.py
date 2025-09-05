from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, Union, cast
from typing import Union






T = TypeVar("T", bound="ChallengeListResponse200OutItemCorrespondence")



@_attrs_define
class ChallengeListResponse200OutItemCorrespondence:
    """ 
        Attributes:
            type_ (Union[Literal['correspondence'], Unset]):
            days_per_turn (Union[Unset, float]):
     """

    type_: Union[Literal['correspondence'], Unset] = UNSET
    days_per_turn: Union[Unset, float] = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        days_per_turn = self.days_per_turn


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if days_per_turn is not UNSET:
            field_dict["daysPerTurn"] = days_per_turn

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Union[Literal['correspondence'], Unset] , d.pop("type", UNSET))
        if type_ != 'correspondence'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'correspondence', got '{type_}'")

        days_per_turn = d.pop("daysPerTurn", UNSET)

        challenge_list_response_200_out_item_correspondence = cls(
            type_=type_,
            days_per_turn=days_per_turn,
        )

        return challenge_list_response_200_out_item_correspondence

