from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.timeline_response_200_users_additional_property import TimelineResponse200UsersAdditionalProperty





T = TypeVar("T", bound="TimelineResponse200Users")



@_attrs_define
class TimelineResponse200Users:
    """ 
     """

    additional_properties: dict[str, 'TimelineResponse200UsersAdditionalProperty'] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.timeline_response_200_users_additional_property import TimelineResponse200UsersAdditionalProperty
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeline_response_200_users_additional_property import TimelineResponse200UsersAdditionalProperty
        d = dict(src_dict)
        timeline_response_200_users = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TimelineResponse200UsersAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        timeline_response_200_users.additional_properties = additional_properties
        return timeline_response_200_users

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> 'TimelineResponse200UsersAdditionalProperty':
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: 'TimelineResponse200UsersAdditionalProperty') -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
