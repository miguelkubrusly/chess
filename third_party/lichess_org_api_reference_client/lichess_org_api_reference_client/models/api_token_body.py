from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, Union, cast
from typing import Union






T = TypeVar("T", bound="ApiTokenBody")



@_attrs_define
class ApiTokenBody:
    """ 
        Attributes:
            grant_type (Union[Literal['authorization_code'], Unset]):
            code (Union[Unset, str]): The authorization code that was sent in the `code` parameter to your `redirect_uri`.
                Example: liu_iS1uOZg99Htmo58ex2jKgYziUfzsnAl0.
            code_verifier (Union[Unset, str]): A `code_challenge` was used to request the authorization code. This must be
                the `code_verifier` it was derived from. Example: Ry1rbGdOMTQtUjhOc0lmTnFKak1LTHV0NjlRMll2aXYtTThkQnlJRkRpaGwyQj
                h0ZDNFdzFPSG9KUlY4M1NrRzJ5ZHhUdjVZR08zLTZOT3dCN2xLfjZOXzU2WHk4SENP.
            redirect_uri (Union[Unset, str]): Must match the `redirect_uri` used to request the authorization code. Example:
                http://example.com/.
            client_id (Union[Unset, str]): Must match the `client_id` used to request the authorization code. Example:
                example.com.
     """

    grant_type: Union[Literal['authorization_code'], Unset] = UNSET
    code: Union[Unset, str] = UNSET
    code_verifier: Union[Unset, str] = UNSET
    redirect_uri: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type

        code = self.code

        code_verifier = self.code_verifier

        redirect_uri = self.redirect_uri

        client_id = self.client_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if code is not UNSET:
            field_dict["code"] = code
        if code_verifier is not UNSET:
            field_dict["code_verifier"] = code_verifier
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if client_id is not UNSET:
            field_dict["client_id"] = client_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = cast(Union[Literal['authorization_code'], Unset] , d.pop("grant_type", UNSET))
        if grant_type != 'authorization_code'and not isinstance(grant_type, Unset):
            raise ValueError(f"grant_type must match const 'authorization_code', got '{grant_type}'")

        code = d.pop("code", UNSET)

        code_verifier = d.pop("code_verifier", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        client_id = d.pop("client_id", UNSET)

        api_token_body = cls(
            grant_type=grant_type,
            code=code,
            code_verifier=code_verifier,
            redirect_uri=redirect_uri,
            client_id=client_id,
        )


        api_token_body.additional_properties = d
        return api_token_body

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
