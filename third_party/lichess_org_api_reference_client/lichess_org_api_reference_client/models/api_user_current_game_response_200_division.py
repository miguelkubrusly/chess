from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiUserCurrentGameResponse200Division")



@_attrs_define
class ApiUserCurrentGameResponse200Division:
    """ 
        Attributes:
            middle (Union[Unset, int]): Ply at which the middlegame begins
            end (Union[Unset, int]): Ply at which the endgame begins
     """

    middle: Union[Unset, int] = UNSET
    end: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        middle = self.middle

        end = self.end


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if middle is not UNSET:
            field_dict["middle"] = middle
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        middle = d.pop("middle", UNSET)

        end = d.pop("end", UNSET)

        api_user_current_game_response_200_division = cls(
            middle=middle,
            end=end,
        )


        api_user_current_game_response_200_division.additional_properties = d
        return api_user_current_game_response_200_division

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
