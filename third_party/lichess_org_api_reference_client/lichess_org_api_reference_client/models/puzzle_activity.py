from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.puzzle_activity_puzzle import PuzzleActivityPuzzle





T = TypeVar("T", bound="PuzzleActivity")



@_attrs_define
class PuzzleActivity:
    """ 
        Attributes:
            date (int):
            puzzle (PuzzleActivityPuzzle):
            win (bool):
     """

    date: int
    puzzle: 'PuzzleActivityPuzzle'
    win: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.puzzle_activity_puzzle import PuzzleActivityPuzzle
        date = self.date

        puzzle = self.puzzle.to_dict()

        win = self.win


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "date": date,
            "puzzle": puzzle,
            "win": win,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.puzzle_activity_puzzle import PuzzleActivityPuzzle
        d = dict(src_dict)
        date = d.pop("date")

        puzzle = PuzzleActivityPuzzle.from_dict(d.pop("puzzle"))




        win = d.pop("win")

        puzzle_activity = cls(
            date=date,
            puzzle=puzzle,
            win=win,
        )


        puzzle_activity.additional_properties = d
        return puzzle_activity

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
