from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ArenaTournamentFullFeaturedC")



@_attrs_define
class ArenaTournamentFullFeaturedC:
    """ 
        Attributes:
            white (Union[Unset, float]): white's clock in seconds
            black (Union[Unset, float]): black's clock in seconds
     """

    white: Union[Unset, float] = UNSET
    black: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        white = self.white

        black = self.black


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if white is not UNSET:
            field_dict["white"] = white
        if black is not UNSET:
            field_dict["black"] = black

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        white = d.pop("white", UNSET)

        black = d.pop("black", UNSET)

        arena_tournament_full_featured_c = cls(
            white=white,
            black=black,
        )


        arena_tournament_full_featured_c.additional_properties = d
        return arena_tournament_full_featured_c

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
