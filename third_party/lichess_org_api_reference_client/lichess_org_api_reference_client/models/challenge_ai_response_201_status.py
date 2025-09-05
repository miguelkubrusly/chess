from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_ai_response_201_status_id import ChallengeAiResponse201StatusId
from ..models.challenge_ai_response_201_status_name import ChallengeAiResponse201StatusName






T = TypeVar("T", bound="ChallengeAiResponse201Status")



@_attrs_define
class ChallengeAiResponse201Status:
    """ 
        Attributes:
            id (ChallengeAiResponse201StatusId):
            name (ChallengeAiResponse201StatusName):
     """

    id: ChallengeAiResponse201StatusId
    name: ChallengeAiResponse201StatusName
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        name = self.name.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = ChallengeAiResponse201StatusId(d.pop("id"))




        name = ChallengeAiResponse201StatusName(d.pop("name"))




        challenge_ai_response_201_status = cls(
            id=id,
            name=name,
        )


        challenge_ai_response_201_status.additional_properties = d
        return challenge_ai_response_201_status

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
