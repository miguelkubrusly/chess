from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SwissResponse200Stats")



@_attrs_define
class SwissResponse200Stats:
    """ 
        Attributes:
            games (float):
            white_wins (float):
            black_wins (float):
            draws (float):
            byes (float):
            absences (float):
            average_rating (float):
     """

    games: float
    white_wins: float
    black_wins: float
    draws: float
    byes: float
    absences: float
    average_rating: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        games = self.games

        white_wins = self.white_wins

        black_wins = self.black_wins

        draws = self.draws

        byes = self.byes

        absences = self.absences

        average_rating = self.average_rating


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "games": games,
            "whiteWins": white_wins,
            "blackWins": black_wins,
            "draws": draws,
            "byes": byes,
            "absences": absences,
            "averageRating": average_rating,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        games = d.pop("games")

        white_wins = d.pop("whiteWins")

        black_wins = d.pop("blackWins")

        draws = d.pop("draws")

        byes = d.pop("byes")

        absences = d.pop("absences")

        average_rating = d.pop("averageRating")

        swiss_response_200_stats = cls(
            games=games,
            white_wins=white_wins,
            black_wins=black_wins,
            draws=draws,
            byes=byes,
            absences=absences,
            average_rating=average_rating,
        )


        swiss_response_200_stats.additional_properties = d
        return swiss_response_200_stats

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
