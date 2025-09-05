from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiAccountPlayingResponse200NowPlayingItemOpponent")



@_attrs_define
class ApiAccountPlayingResponse200NowPlayingItemOpponent:
    """ 
        Attributes:
            id (str):
            username (str):
            rating (Union[Unset, float]):
            rating_diff (Union[Unset, float]):
            ai (Union[Unset, float]):
     """

    id: str
    username: str
    rating: Union[Unset, float] = UNSET
    rating_diff: Union[Unset, float] = UNSET
    ai: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        rating = self.rating

        rating_diff = self.rating_diff

        ai = self.ai


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "username": username,
        })
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_diff is not UNSET:
            field_dict["ratingDiff"] = rating_diff
        if ai is not UNSET:
            field_dict["ai"] = ai

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        rating = d.pop("rating", UNSET)

        rating_diff = d.pop("ratingDiff", UNSET)

        ai = d.pop("ai", UNSET)

        api_account_playing_response_200_now_playing_item_opponent = cls(
            id=id,
            username=username,
            rating=rating,
            rating_diff=rating_diff,
            ai=ai,
        )


        api_account_playing_response_200_now_playing_item_opponent.additional_properties = d
        return api_account_playing_response_200_now_playing_item_opponent

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
