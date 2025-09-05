from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="ChallengeOpenResponse200Open")



@_attrs_define
class ChallengeOpenResponse200Open:
    """ 
        Attributes:
            user_ids (Union[Unset, list[str]]): An optional array of two user ids. If set, only these users will be allowed
                to join the game. The first username gets the white pieces.
     """

    user_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_ids = cast(list[str], d.pop("userIds", UNSET))


        challenge_open_response_200_open = cls(
            user_ids=user_ids,
        )


        challenge_open_response_200_open.additional_properties = d
        return challenge_open_response_200_open

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
