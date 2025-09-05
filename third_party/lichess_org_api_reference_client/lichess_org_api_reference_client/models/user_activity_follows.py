from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.user_activity_follows_out import UserActivityFollowsOut
  from ..models.user_activity_follows_in import UserActivityFollowsIn





T = TypeVar("T", bound="UserActivityFollows")



@_attrs_define
class UserActivityFollows:
    """ 
        Attributes:
            in_ (Union[Unset, UserActivityFollowsIn]):
            out (Union[Unset, UserActivityFollowsOut]):
     """

    in_: Union[Unset, 'UserActivityFollowsIn'] = UNSET
    out: Union[Unset, 'UserActivityFollowsOut'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_activity_follows_out import UserActivityFollowsOut
        from ..models.user_activity_follows_in import UserActivityFollowsIn
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
        from ..models.user_activity_follows_out import UserActivityFollowsOut
        from ..models.user_activity_follows_in import UserActivityFollowsIn
        d = dict(src_dict)
        _in_ = d.pop("in", UNSET)
        in_: Union[Unset, UserActivityFollowsIn]
        if isinstance(_in_,  Unset):
            in_ = UNSET
        else:
            in_ = UserActivityFollowsIn.from_dict(_in_)




        _out = d.pop("out", UNSET)
        out: Union[Unset, UserActivityFollowsOut]
        if isinstance(_out,  Unset):
            out = UNSET
        else:
            out = UserActivityFollowsOut.from_dict(_out)




        user_activity_follows = cls(
            in_=in_,
            out=out,
        )


        user_activity_follows.additional_properties = d
        return user_activity_follows

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
