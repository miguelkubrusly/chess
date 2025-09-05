from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.arena_tournaments_started_item_min_rating_perf import ArenaTournamentsStartedItemMinRatingPerf
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ArenaTournamentsStartedItemMinRating")



@_attrs_define
class ArenaTournamentsStartedItemMinRating:
    """ 
        Attributes:
            rating (int):  Example: 1700.
            perf (Union[Unset, ArenaTournamentsStartedItemMinRatingPerf]):
     """

    rating: int
    perf: Union[Unset, ArenaTournamentsStartedItemMinRatingPerf] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rating = self.rating

        perf: Union[Unset, str] = UNSET
        if not isinstance(self.perf, Unset):
            perf = self.perf.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rating": rating,
        })
        if perf is not UNSET:
            field_dict["perf"] = perf

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rating = d.pop("rating")

        _perf = d.pop("perf", UNSET)
        perf: Union[Unset, ArenaTournamentsStartedItemMinRatingPerf]
        if isinstance(_perf,  Unset):
            perf = UNSET
        else:
            perf = ArenaTournamentsStartedItemMinRatingPerf(_perf)




        arena_tournaments_started_item_min_rating = cls(
            rating=rating,
            perf=perf,
        )


        arena_tournaments_started_item_min_rating.additional_properties = d
        return arena_tournaments_started_item_min_rating

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
