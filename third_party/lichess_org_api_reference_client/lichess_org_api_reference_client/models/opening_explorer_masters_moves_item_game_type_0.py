from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.opening_explorer_masters_moves_item_game_type_0_winner_type_1 import OpeningExplorerMastersMovesItemGameType0WinnerType1
from ..models.opening_explorer_masters_moves_item_game_type_0_winner_type_2_type_1 import OpeningExplorerMastersMovesItemGameType0WinnerType2Type1
from ..models.opening_explorer_masters_moves_item_game_type_0_winner_type_3_type_1 import OpeningExplorerMastersMovesItemGameType0WinnerType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.opening_explorer_masters_moves_item_game_type_0_white import OpeningExplorerMastersMovesItemGameType0White
  from ..models.opening_explorer_masters_moves_item_game_type_0_black import OpeningExplorerMastersMovesItemGameType0Black





T = TypeVar("T", bound="OpeningExplorerMastersMovesItemGameType0")



@_attrs_define
class OpeningExplorerMastersMovesItemGameType0:
    """ 
        Attributes:
            id (str):
            winner (Union[None, OpeningExplorerMastersMovesItemGameType0WinnerType1,
                OpeningExplorerMastersMovesItemGameType0WinnerType2Type1,
                OpeningExplorerMastersMovesItemGameType0WinnerType3Type1]):
            white (OpeningExplorerMastersMovesItemGameType0White):
            black (OpeningExplorerMastersMovesItemGameType0Black):
            year (float):
            month (Union[Unset, str]):
     """

    id: str
    winner: Union[None, OpeningExplorerMastersMovesItemGameType0WinnerType1, OpeningExplorerMastersMovesItemGameType0WinnerType2Type1, OpeningExplorerMastersMovesItemGameType0WinnerType3Type1]
    white: 'OpeningExplorerMastersMovesItemGameType0White'
    black: 'OpeningExplorerMastersMovesItemGameType0Black'
    year: float
    month: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_masters_moves_item_game_type_0_white import OpeningExplorerMastersMovesItemGameType0White
        from ..models.opening_explorer_masters_moves_item_game_type_0_black import OpeningExplorerMastersMovesItemGameType0Black
        id = self.id

        winner: Union[None, str]
        if isinstance(self.winner, OpeningExplorerMastersMovesItemGameType0WinnerType1):
            winner = self.winner.value
        elif isinstance(self.winner, OpeningExplorerMastersMovesItemGameType0WinnerType2Type1):
            winner = self.winner.value
        elif isinstance(self.winner, OpeningExplorerMastersMovesItemGameType0WinnerType3Type1):
            winner = self.winner.value
        else:
            winner = self.winner

        white = self.white.to_dict()

        black = self.black.to_dict()

        year = self.year

        month = self.month


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "winner": winner,
            "white": white,
            "black": black,
            "year": year,
        })
        if month is not UNSET:
            field_dict["month"] = month

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opening_explorer_masters_moves_item_game_type_0_white import OpeningExplorerMastersMovesItemGameType0White
        from ..models.opening_explorer_masters_moves_item_game_type_0_black import OpeningExplorerMastersMovesItemGameType0Black
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_winner(data: object) -> Union[None, OpeningExplorerMastersMovesItemGameType0WinnerType1, OpeningExplorerMastersMovesItemGameType0WinnerType2Type1, OpeningExplorerMastersMovesItemGameType0WinnerType3Type1]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_1 = OpeningExplorerMastersMovesItemGameType0WinnerType1(data)



                return winner_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_2_type_1 = OpeningExplorerMastersMovesItemGameType0WinnerType2Type1(data)



                return winner_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_3_type_1 = OpeningExplorerMastersMovesItemGameType0WinnerType3Type1(data)



                return winner_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[None, OpeningExplorerMastersMovesItemGameType0WinnerType1, OpeningExplorerMastersMovesItemGameType0WinnerType2Type1, OpeningExplorerMastersMovesItemGameType0WinnerType3Type1], data)

        winner = _parse_winner(d.pop("winner"))


        white = OpeningExplorerMastersMovesItemGameType0White.from_dict(d.pop("white"))




        black = OpeningExplorerMastersMovesItemGameType0Black.from_dict(d.pop("black"))




        year = d.pop("year")

        month = d.pop("month", UNSET)

        opening_explorer_masters_moves_item_game_type_0 = cls(
            id=id,
            winner=winner,
            white=white,
            black=black,
            year=year,
            month=month,
        )


        opening_explorer_masters_moves_item_game_type_0.additional_properties = d
        return opening_explorer_masters_moves_item_game_type_0

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
