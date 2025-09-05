from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiUserActivityResponse200ItemCorrespondenceEndsScoreRp")



@_attrs_define
class ApiUserActivityResponse200ItemCorrespondenceEndsScoreRp:
    """ 
        Attributes:
            before (Union[Unset, float]):
            after (Union[Unset, float]):
     """

    before: Union[Unset, float] = UNSET
    after: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        before = self.before

        after = self.after


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        before = d.pop("before", UNSET)

        after = d.pop("after", UNSET)

        api_user_activity_response_200_item_correspondence_ends_score_rp = cls(
            before=before,
            after=after,
        )


        api_user_activity_response_200_item_correspondence_ends_score_rp.additional_properties = d
        return api_user_activity_response_200_item_correspondence_ends_score_rp

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
