from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_list_response_200_in_item import ChallengeListResponse200InItem
  from ..models.challenge_list_response_200_out_item import ChallengeListResponse200OutItem





T = TypeVar("T", bound="ChallengeListResponse200")



@_attrs_define
class ChallengeListResponse200:
    """ 
        Attributes:
            in_ (Union[Unset, list['ChallengeListResponse200InItem']]): Incoming challenges i.e. targeted at you
            out (Union[Unset, list['ChallengeListResponse200OutItem']]): Outgoing challenges i.e. created by you
     """

    in_: Union[Unset, list['ChallengeListResponse200InItem']] = UNSET
    out: Union[Unset, list['ChallengeListResponse200OutItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_list_response_200_in_item import ChallengeListResponse200InItem
        from ..models.challenge_list_response_200_out_item import ChallengeListResponse200OutItem
        in_: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.in_, Unset):
            in_ = []
            for in_item_data in self.in_:
                in_item = in_item_data.to_dict()
                in_.append(in_item)



        out: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.out, Unset):
            out = []
            for out_item_data in self.out:
                out_item = out_item_data.to_dict()
                out.append(out_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if in_ is not UNSET:
            field_dict["in"] = in_
        if out is not UNSET:
            field_dict["out"] = out

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge_list_response_200_in_item import ChallengeListResponse200InItem
        from ..models.challenge_list_response_200_out_item import ChallengeListResponse200OutItem
        d = dict(src_dict)
        in_ = []
        _in_ = d.pop("in", UNSET)
        for in_item_data in (_in_ or []):
            in_item = ChallengeListResponse200InItem.from_dict(in_item_data)



            in_.append(in_item)


        out = []
        _out = d.pop("out", UNSET)
        for out_item_data in (_out or []):
            out_item = ChallengeListResponse200OutItem.from_dict(out_item_data)



            out.append(out_item)


        challenge_list_response_200 = cls(
            in_=in_,
            out=out,
        )


        challenge_list_response_200.additional_properties = d
        return challenge_list_response_200

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
