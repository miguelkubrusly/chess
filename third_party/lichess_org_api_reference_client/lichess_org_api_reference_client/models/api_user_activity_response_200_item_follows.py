from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_user_activity_response_200_item_follows_out import ApiUserActivityResponse200ItemFollowsOut
  from ..models.api_user_activity_response_200_item_follows_in import ApiUserActivityResponse200ItemFollowsIn





T = TypeVar("T", bound="ApiUserActivityResponse200ItemFollows")



@_attrs_define
class ApiUserActivityResponse200ItemFollows:
    """ 
        Attributes:
            in_ (Union[Unset, ApiUserActivityResponse200ItemFollowsIn]):
            out (Union[Unset, ApiUserActivityResponse200ItemFollowsOut]):
     """

    in_: Union[Unset, 'ApiUserActivityResponse200ItemFollowsIn'] = UNSET
    out: Union[Unset, 'ApiUserActivityResponse200ItemFollowsOut'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_activity_response_200_item_follows_out import ApiUserActivityResponse200ItemFollowsOut
        from ..models.api_user_activity_response_200_item_follows_in import ApiUserActivityResponse200ItemFollowsIn
        in_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.in_, Unset):
            in_ = self.in_.to_dict()

        out: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.out, Unset):
            out = self.out.to_dict()


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
        from ..models.api_user_activity_response_200_item_follows_out import ApiUserActivityResponse200ItemFollowsOut
        from ..models.api_user_activity_response_200_item_follows_in import ApiUserActivityResponse200ItemFollowsIn
        d = dict(src_dict)
        _in_ = d.pop("in", UNSET)
        in_: Union[Unset, ApiUserActivityResponse200ItemFollowsIn]
        if isinstance(_in_,  Unset):
            in_ = UNSET
        else:
            in_ = ApiUserActivityResponse200ItemFollowsIn.from_dict(_in_)




        _out = d.pop("out", UNSET)
        out: Union[Unset, ApiUserActivityResponse200ItemFollowsOut]
        if isinstance(_out,  Unset):
            out = UNSET
        else:
            out = ApiUserActivityResponse200ItemFollowsOut.from_dict(_out)




        api_user_activity_response_200_item_follows = cls(
            in_=in_,
            out=out,
        )


        api_user_activity_response_200_item_follows.additional_properties = d
        return api_user_activity_response_200_item_follows

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
