from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="UserPerfsCrazyhouse")



@_attrs_define
class UserPerfsCrazyhouse:
    """ 
        Attributes:
            games (int):
            rating (int):
            rd (int): rating deviation
            prog (int):
            prov (Union[Unset, bool]): only appears if a user's perf rating are
                [provisional](https://lichess.org/faq#provisional)
     """

    games: int
    rating: int
    rd: int
    prog: int
    prov: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        games = self.games

        rating = self.rating

        rd = self.rd

        prog = self.prog

        prov = self.prov


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "games": games,
            "rating": rating,
            "rd": rd,
            "prog": prog,
        })
        if prov is not UNSET:
            field_dict["prov"] = prov

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        games = d.pop("games")

        rating = d.pop("rating")

        rd = d.pop("rd")

        prog = d.pop("prog")

        prov = d.pop("prov", UNSET)

        user_perfs_crazyhouse = cls(
            games=games,
            rating=rating,
            rd=rd,
            prog=prog,
            prov=prov,
        )


        user_perfs_crazyhouse.additional_properties = d
        return user_perfs_crazyhouse

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
