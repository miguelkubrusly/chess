from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="ApiUserActivityResponse200ItemFollowsOut")



@_attrs_define
class ApiUserActivityResponse200ItemFollowsOut:
    """ 
        Attributes:
            ids (list[str]):
            nb (Union[Unset, float]):
     """

    ids: list[str]
    nb: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ids = self.ids



        nb = self.nb


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ids": ids,
        })
        if nb is not UNSET:
            field_dict["nb"] = nb

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))


        nb = d.pop("nb", UNSET)

        api_user_activity_response_200_item_follows_out = cls(
            ids=ids,
            nb=nb,
        )


        api_user_activity_response_200_item_follows_out.additional_properties = d
        return api_user_activity_response_200_item_follows_out

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
