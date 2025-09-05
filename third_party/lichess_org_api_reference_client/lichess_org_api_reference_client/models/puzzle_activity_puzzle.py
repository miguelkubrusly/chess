from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PuzzleActivityPuzzle")



@_attrs_define
class PuzzleActivityPuzzle:
    """ 
        Attributes:
            fen (str):
            id (str):
            last_move (str):
            plays (int):
            rating (int):
            solution (list[str]):
            themes (list[str]):
     """

    fen: str
    id: str
    last_move: str
    plays: int
    rating: int
    solution: list[str]
    themes: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        fen = self.fen

        id = self.id

        last_move = self.last_move

        plays = self.plays

        rating = self.rating

        solution = self.solution



        themes = self.themes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fen": fen,
            "id": id,
            "lastMove": last_move,
            "plays": plays,
            "rating": rating,
            "solution": solution,
            "themes": themes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fen = d.pop("fen")

        id = d.pop("id")

        last_move = d.pop("lastMove")

        plays = d.pop("plays")

        rating = d.pop("rating")

        solution = cast(list[str], d.pop("solution"))


        themes = cast(list[str], d.pop("themes"))


        puzzle_activity_puzzle = cls(
            fen=fen,
            id=id,
            last_move=last_move,
            plays=plays,
            rating=rating,
            solution=solution,
            themes=themes,
        )


        puzzle_activity_puzzle.additional_properties = d
        return puzzle_activity_puzzle

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
