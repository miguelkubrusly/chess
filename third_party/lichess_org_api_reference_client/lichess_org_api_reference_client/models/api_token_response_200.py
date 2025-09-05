from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ApiTokenResponse200")



@_attrs_define
class ApiTokenResponse200:
    """ 
        Attributes:
            token_type (str):  Example: Bearer.
            access_token (str):  Example: lio_pLwAbN7lFPklzY2m8lTOI1DGApS84u57.
            expires_in (int):  Example: 31536000.
     """

    token_type: str
    access_token: str
    expires_in: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        token_type = self.token_type

        access_token = self.access_token

        expires_in = self.expires_in


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "token_type": token_type,
            "access_token": access_token,
            "expires_in": expires_in,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token_type = d.pop("token_type")

        access_token = d.pop("access_token")

        expires_in = d.pop("expires_in")

        api_token_response_200 = cls(
            token_type=token_type,
            access_token=access_token,
            expires_in=expires_in,
        )


        api_token_response_200.additional_properties = d
        return api_token_response_200

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
