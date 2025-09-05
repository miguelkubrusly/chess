from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PuzzlePerformance")



@_attrs_define
class PuzzlePerformance:
    """ 
        Attributes:
            first_wins (int):
            nb (int):
            performance (int):
            puzzle_rating_avg (int):
            replay_wins (int):
     """

    first_wins: int
    nb: int
    performance: int
    puzzle_rating_avg: int
    replay_wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        first_wins = self.first_wins

        nb = self.nb

        performance = self.performance

        puzzle_rating_avg = self.puzzle_rating_avg

        replay_wins = self.replay_wins


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "firstWins": first_wins,
            "nb": nb,
            "performance": performance,
            "puzzleRatingAvg": puzzle_rating_avg,
            "replayWins": replay_wins,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_wins = d.pop("firstWins")

        nb = d.pop("nb")

        performance = d.pop("performance")

        puzzle_rating_avg = d.pop("puzzleRatingAvg")

        replay_wins = d.pop("replayWins")

        puzzle_performance = cls(
            first_wins=first_wins,
            nb=nb,
            performance=performance,
            puzzle_rating_avg=puzzle_rating_avg,
            replay_wins=replay_wins,
        )


        puzzle_performance.additional_properties = d
        return puzzle_performance

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
