from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.account_response_200_prefs import AccountResponse200Prefs





T = TypeVar("T", bound="AccountResponse200")



@_attrs_define
class AccountResponse200:
    """ 
        Attributes:
            prefs (Union[Unset, AccountResponse200Prefs]):
            language (Union[Unset, str]):  Example: en-GB.
     """

    prefs: Union[Unset, 'AccountResponse200Prefs'] = UNSET
    language: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_response_200_prefs import AccountResponse200Prefs
        prefs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prefs, Unset):
            prefs = self.prefs.to_dict()

        language = self.language


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if prefs is not UNSET:
            field_dict["prefs"] = prefs
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_response_200_prefs import AccountResponse200Prefs
        d = dict(src_dict)
        _prefs = d.pop("prefs", UNSET)
        prefs: Union[Unset, AccountResponse200Prefs]
        if isinstance(_prefs,  Unset):
            prefs = UNSET
        else:
            prefs = AccountResponse200Prefs.from_dict(_prefs)




        language = d.pop("language", UNSET)

        account_response_200 = cls(
            prefs=prefs,
            language=language,
        )


        account_response_200.additional_properties = d
        return account_response_200

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
