from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.token_test_response_200_additional_property_type_0 import TokenTestResponse200AdditionalPropertyType0





T = TypeVar("T", bound="TokenTestResponse200")



@_attrs_define
class TokenTestResponse200:
    """ 
     """

    additional_properties: dict[str, Union['TokenTestResponse200AdditionalPropertyType0', None]] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.token_test_response_200_additional_property_type_0 import TokenTestResponse200AdditionalPropertyType0
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            if isinstance(prop, TokenTestResponse200AdditionalPropertyType0):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_test_response_200_additional_property_type_0 import TokenTestResponse200AdditionalPropertyType0
        d = dict(src_dict)
        token_test_response_200 = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> Union['TokenTestResponse200AdditionalPropertyType0', None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = TokenTestResponse200AdditionalPropertyType0.from_dict(data)



                    return additional_property_type_0
                except: # noqa: E722
                    pass
                return cast(Union['TokenTestResponse200AdditionalPropertyType0', None], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        token_test_response_200.additional_properties = additional_properties
        return token_test_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union['TokenTestResponse200AdditionalPropertyType0', None]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union['TokenTestResponse200AdditionalPropertyType0', None]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
