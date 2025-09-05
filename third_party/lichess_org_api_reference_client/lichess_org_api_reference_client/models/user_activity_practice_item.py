from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UserActivityPracticeItem")



@_attrs_define
class UserActivityPracticeItem:
    """ 
        Attributes:
            url (str):
            name (str):
            nb_positions (float):
     """

    url: str
    name: str
    nb_positions: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        name = self.name

        nb_positions = self.nb_positions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "url": url,
            "name": name,
            "nbPositions": nb_positions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        name = d.pop("name")

        nb_positions = d.pop("nbPositions")

        user_activity_practice_item = cls(
            url=url,
            name=name,
            nb_positions=nb_positions,
        )


        user_activity_practice_item.additional_properties = d
        return user_activity_practice_item

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
