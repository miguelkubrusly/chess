from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, Union, cast






T = TypeVar("T", bound="ChallengeDeclinedJsonUnlimited")



@_attrs_define
class ChallengeDeclinedJsonUnlimited:
    """ 
        Attributes:
            type_ (Union[Literal['unlimited'], Unset]):
     """

    type_: Union[Literal['unlimited'], Unset] = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Union[Literal['unlimited'], Unset] , d.pop("type", UNSET))
        if type_ != 'unlimited'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'unlimited', got '{type_}'")

        challenge_declined_json_unlimited = cls(
            type_=type_,
        )

        return challenge_declined_json_unlimited

