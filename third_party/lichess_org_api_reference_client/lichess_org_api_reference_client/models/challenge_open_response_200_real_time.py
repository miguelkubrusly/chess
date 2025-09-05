from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, Union, cast
from typing import Union






T = TypeVar("T", bound="ChallengeOpenResponse200RealTime")



@_attrs_define
class ChallengeOpenResponse200RealTime:
    """ 
        Attributes:
            type_ (Union[Literal['clock'], Unset]):
            limit (Union[Unset, float]):
            increment (Union[Unset, float]):
            show (Union[Unset, str]):  Example: 5+2.
     """

    type_: Union[Literal['clock'], Unset] = UNSET
    limit: Union[Unset, float] = UNSET
    increment: Union[Unset, float] = UNSET
    show: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        limit = self.limit

        increment = self.increment

        show = self.show


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if limit is not UNSET:
            field_dict["limit"] = limit
        if increment is not UNSET:
            field_dict["increment"] = increment
        if show is not UNSET:
            field_dict["show"] = show

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Union[Literal['clock'], Unset] , d.pop("type", UNSET))
        if type_ != 'clock'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'clock', got '{type_}'")

        limit = d.pop("limit", UNSET)

        increment = d.pop("increment", UNSET)

        show = d.pop("show", UNSET)

        challenge_open_response_200_real_time = cls(
            type_=type_,
            limit=limit,
            increment=increment,
            show=show,
        )

        return challenge_open_response_200_real_time

