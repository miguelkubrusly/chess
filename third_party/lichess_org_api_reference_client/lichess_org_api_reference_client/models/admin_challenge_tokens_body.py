from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AdminChallengeTokensBody")



@_attrs_define
class AdminChallengeTokensBody:
    """ 
        Attributes:
            users (str): Usernames separated with commas Example: thibault,neio,lizen2,lizen3.
            description (str): User visible description of the token Example: FIDE tournament XYZ.
     """

    users: str
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        users = self.users

        description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "users": users,
            "description": description,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        users = d.pop("users")

        description = d.pop("description")

        admin_challenge_tokens_body = cls(
            users=users,
            description=description,
        )


        admin_challenge_tokens_body.additional_properties = d
        return admin_challenge_tokens_body

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
