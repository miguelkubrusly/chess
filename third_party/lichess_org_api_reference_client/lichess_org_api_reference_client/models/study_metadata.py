from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="StudyMetadata")



@_attrs_define
class StudyMetadata:
    """ 
        Example:
            {'id': 'WTvnkWAL', 'name': 'Guess the move', 'createdAt': 1463756350225, 'updatedAt': 1469965025205}

        Attributes:
            id (str): The study ID
            name (str): The study name
            created_at (int): The study creation date
            updated_at (int): The study last update date
     """

    id: str
    name: str
    created_at: int
    updated_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        study_metadata = cls(
            id=id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
        )


        study_metadata.additional_properties = d
        return study_metadata

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
