from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TeamRequestWithUserRequest")



@_attrs_define
class TeamRequestWithUserRequest:
    """ 
        Attributes:
            team_id (str):  Example: coders.
            user_id (str):  Example: thibault.
            date (float):  Example: 1514505150384.
            message (Union[Unset, str]):  Example: Hello, I would like to join the team!.
     """

    team_id: str
    user_id: str
    date: float
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        user_id = self.user_id

        date = self.date

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "teamId": team_id,
            "userId": user_id,
            "date": date,
        })
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("teamId")

        user_id = d.pop("userId")

        date = d.pop("date")

        message = d.pop("message", UNSET)

        team_request_with_user_request = cls(
            team_id=team_id,
            user_id=user_id,
            date=date,
            message=message,
        )


        team_request_with_user_request.additional_properties = d
        return team_request_with_user_request

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
