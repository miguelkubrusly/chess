from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TournamentResponse200FeaturedBlack")



@_attrs_define
class TournamentResponse200FeaturedBlack:
    """ 
        Attributes:
            name (Union[Unset, str]):
            id (Union[Unset, str]):
            rank (Union[Unset, float]):
            rating (Union[Unset, float]):
     """

    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    rank: Union[Unset, float] = UNSET
    rating: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        rank = self.rank

        rating = self.rating


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        rank = d.pop("rank", UNSET)

        rating = d.pop("rating", UNSET)

        tournament_response_200_featured_black = cls(
            name=name,
            id=id,
            rank=rank,
            rating=rating,
        )


        tournament_response_200_featured_black.additional_properties = d
        return tournament_response_200_featured_black

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
