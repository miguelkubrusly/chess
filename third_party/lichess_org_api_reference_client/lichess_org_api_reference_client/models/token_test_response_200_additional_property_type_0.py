from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TokenTestResponse200AdditionalPropertyType0")



@_attrs_define
class TokenTestResponse200AdditionalPropertyType0:
    """ 
        Attributes:
            user_id (Union[Unset, str]):
            scopes (Union[Unset, str]): Comma-separated list of scopes. Empty string if the token has no scopes.
            expires (Union[None, Unset, int]): Unix-timestamp in milliseconds or null if the token never expires.
     """

    user_id: Union[Unset, str] = UNSET
    scopes: Union[Unset, str] = UNSET
    expires: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        scopes = self.scopes

        expires: Union[None, Unset, int]
        if isinstance(self.expires, Unset):
            expires = UNSET
        else:
            expires = self.expires


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        scopes = d.pop("scopes", UNSET)

        def _parse_expires(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        expires = _parse_expires(d.pop("expires", UNSET))


        token_test_response_200_additional_property_type_0 = cls(
            user_id=user_id,
            scopes=scopes,
            expires=expires,
        )


        token_test_response_200_additional_property_type_0.additional_properties = d
        return token_test_response_200_additional_property_type_0

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
