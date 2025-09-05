from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.puzzle_and_game_game import PuzzleAndGameGame
  from ..models.puzzle_and_game_puzzle import PuzzleAndGamePuzzle





T = TypeVar("T", bound="PuzzleAndGame")



@_attrs_define
class PuzzleAndGame:
    """ 
        Attributes:
            game (PuzzleAndGameGame):
            puzzle (PuzzleAndGamePuzzle):
     """

    game: 'PuzzleAndGameGame'
    puzzle: 'PuzzleAndGamePuzzle'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.puzzle_and_game_game import PuzzleAndGameGame
        from ..models.puzzle_and_game_puzzle import PuzzleAndGamePuzzle
        game = self.game.to_dict()

        puzzle = self.puzzle.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "game": game,
            "puzzle": puzzle,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.puzzle_and_game_game import PuzzleAndGameGame
        from ..models.puzzle_and_game_puzzle import PuzzleAndGamePuzzle
        d = dict(src_dict)
        game = PuzzleAndGameGame.from_dict(d.pop("game"))




        puzzle = PuzzleAndGamePuzzle.from_dict(d.pop("puzzle"))




        puzzle_and_game = cls(
            game=game,
            puzzle=puzzle,
        )


        puzzle_and_game.additional_properties = d
        return puzzle_and_game

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
