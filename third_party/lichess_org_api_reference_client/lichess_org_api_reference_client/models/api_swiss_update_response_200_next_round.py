from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="ApiSwissUpdateResponse200NextRound")



@_attrs_define
class ApiSwissUpdateResponse200NextRound:
    """ 
        Attributes:
            at (Union[Unset, datetime.datetime]):
            in_ (Union[Unset, int]): The number of seconds until the next round starts.
     """

    at: Union[Unset, datetime.datetime] = UNSET
    in_: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        at: Union[Unset, str] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        in_ = self.in_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if at is not UNSET:
            field_dict["at"] = at
        if in_ is not UNSET:
            field_dict["in"] = in_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _at = d.pop("at", UNSET)
        at: Union[Unset, datetime.datetime]
        if isinstance(_at,  Unset):
            at = UNSET
        else:
            at = isoparse(_at)




        in_ = d.pop("in", UNSET)

        api_swiss_update_response_200_next_round = cls(
            at=at,
            in_=in_,
        )


        api_swiss_update_response_200_next_round.additional_properties = d
        return api_swiss_update_response_200_next_round

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
