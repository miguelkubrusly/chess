from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiTokenResponse400")



@_attrs_define
class ApiTokenResponse400:
    """ 
        Example:
            {'error': 'invalid_grant', 'error_description': 'hash of code_verifier does not match code_challenge'}

        Attributes:
            error (Union[Unset, str]): The cause of the error.
            error_description (Union[Unset, str]): The reason why the request was rejected.
     """

    error: Union[Unset, str] = UNSET
    error_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        error = self.error

        error_description = self.error_description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if error_description is not UNSET:
            field_dict["error_description"] = error_description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        error_description = d.pop("error_description", UNSET)

        api_token_response_400 = cls(
            error=error,
            error_description=error_description,
        )


        api_token_response_400.additional_properties = d
        return api_token_response_400

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
