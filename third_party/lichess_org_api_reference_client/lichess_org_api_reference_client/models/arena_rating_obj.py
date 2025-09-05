from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.arena_rating_obj_perf import ArenaRatingObjPerf
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ArenaRatingObj")



@_attrs_define
class ArenaRatingObj:
    """ 
        Attributes:
            rating (int):  Example: 1700.
            perf (Union[Unset, ArenaRatingObjPerf]):
     """

    rating: int
    perf: Union[Unset, ArenaRatingObjPerf] = UNSET
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
        perf: Union[Unset, ArenaRatingObjPerf]
        if isinstance(_perf,  Unset):
            perf = UNSET
        else:
            perf = ArenaRatingObjPerf(_perf)




        arena_rating_obj = cls(
            rating=rating,
            perf=perf,
        )


        arena_rating_obj.additional_properties = d
        return arena_rating_obj

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
