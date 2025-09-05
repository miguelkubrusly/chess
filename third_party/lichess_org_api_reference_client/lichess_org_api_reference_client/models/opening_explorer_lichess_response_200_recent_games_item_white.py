from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="OpeningExplorerLichessResponse200RecentGamesItemWhite")



@_attrs_define
class OpeningExplorerLichessResponse200RecentGamesItemWhite:
    """ 
        Attributes:
            name (str):
            rating (int):
     """

    name: str
    rating: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        rating = self.rating


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "rating": rating,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        rating = d.pop("rating")

        opening_explorer_lichess_response_200_recent_games_item_white = cls(
            name=name,
            rating=rating,
        )


        opening_explorer_lichess_response_200_recent_games_item_white.additional_properties = d
        return opening_explorer_lichess_response_200_recent_games_item_white

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
