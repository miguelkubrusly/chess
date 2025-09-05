from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ApiPuzzleIdResponse200Puzzle")



@_attrs_define
class ApiPuzzleIdResponse200Puzzle:
    """ 
        Attributes:
            id (str):
            initial_ply (int):
            plays (int):
            rating (int):
            solution (list[str]):
            themes (list[str]):
     """

    id: str
    initial_ply: int
    plays: int
    rating: int
    solution: list[str]
    themes: list[str]





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        initial_ply = self.initial_ply

        plays = self.plays

        rating = self.rating

        solution = self.solution



        themes = self.themes




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "initialPly": initial_ply,
            "plays": plays,
            "rating": rating,
            "solution": solution,
            "themes": themes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        initial_ply = d.pop("initialPly")

        plays = d.pop("plays")

        rating = d.pop("rating")

        solution = cast(list[str], d.pop("solution"))


        themes = cast(list[str], d.pop("themes"))


        api_puzzle_id_response_200_puzzle = cls(
            id=id,
            initial_ply=initial_ply,
            plays=plays,
            rating=rating,
            solution=solution,
            themes=themes,
        )

        return api_puzzle_id_response_200_puzzle

