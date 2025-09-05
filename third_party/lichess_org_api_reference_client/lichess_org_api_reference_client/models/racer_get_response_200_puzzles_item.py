from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RacerGetResponse200PuzzlesItem")



@_attrs_define
class RacerGetResponse200PuzzlesItem:
    """ 
        Attributes:
            id (str): Puzzle ID
            fen (str): FEN position of the puzzle
            line (str): Solution moves sequence
            rating (int): Puzzle Glicko2 rating
     """

    id: str
    fen: str
    line: str
    rating: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        fen = self.fen

        line = self.line

        rating = self.rating


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "fen": fen,
            "line": line,
            "rating": rating,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        fen = d.pop("fen")

        line = d.pop("line")

        rating = d.pop("rating")

        racer_get_response_200_puzzles_item = cls(
            id=id,
            fen=fen,
            line=line,
            rating=rating,
        )


        racer_get_response_200_puzzles_item.additional_properties = d
        return racer_get_response_200_puzzles_item

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
