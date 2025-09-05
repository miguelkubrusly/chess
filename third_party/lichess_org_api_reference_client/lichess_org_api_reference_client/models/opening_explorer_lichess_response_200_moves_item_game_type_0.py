from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_speed import OpeningExplorerLichessResponse200MovesItemGameType0Speed
from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_winner_type_1 import OpeningExplorerLichessResponse200MovesItemGameType0WinnerType1
from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_winner_type_2_type_1 import OpeningExplorerLichessResponse200MovesItemGameType0WinnerType2Type1
from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_winner_type_3_type_1 import OpeningExplorerLichessResponse200MovesItemGameType0WinnerType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_white import OpeningExplorerLichessResponse200MovesItemGameType0White
  from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_black import OpeningExplorerLichessResponse200MovesItemGameType0Black





T = TypeVar("T", bound="OpeningExplorerLichessResponse200MovesItemGameType0")



@_attrs_define
class OpeningExplorerLichessResponse200MovesItemGameType0:
    """ 
        Attributes:
            id (str):
            winner (Union[None, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType1,
                OpeningExplorerLichessResponse200MovesItemGameType0WinnerType2Type1,
                OpeningExplorerLichessResponse200MovesItemGameType0WinnerType3Type1]):
            white (OpeningExplorerLichessResponse200MovesItemGameType0White):
            black (OpeningExplorerLichessResponse200MovesItemGameType0Black):
            year (float):
            month (Union[None, str]):
            speed (Union[Unset, OpeningExplorerLichessResponse200MovesItemGameType0Speed]):
     """

    id: str
    winner: Union[None, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType1, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType2Type1, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType3Type1]
    white: 'OpeningExplorerLichessResponse200MovesItemGameType0White'
    black: 'OpeningExplorerLichessResponse200MovesItemGameType0Black'
    year: float
    month: Union[None, str]
    speed: Union[Unset, OpeningExplorerLichessResponse200MovesItemGameType0Speed] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_white import OpeningExplorerLichessResponse200MovesItemGameType0White
        from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_black import OpeningExplorerLichessResponse200MovesItemGameType0Black
        id = self.id

        winner: Union[None, str]
        if isinstance(self.winner, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType1):
            winner = self.winner.value
        elif isinstance(self.winner, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType2Type1):
            winner = self.winner.value
        elif isinstance(self.winner, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType3Type1):
            winner = self.winner.value
        else:
            winner = self.winner

        white = self.white.to_dict()

        black = self.black.to_dict()

        year = self.year

        month: Union[None, str]
        month = self.month

        speed: Union[Unset, str] = UNSET
        if not isinstance(self.speed, Unset):
            speed = self.speed.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "winner": winner,
            "white": white,
            "black": black,
            "year": year,
            "month": month,
        })
        if speed is not UNSET:
            field_dict["speed"] = speed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_white import OpeningExplorerLichessResponse200MovesItemGameType0White
        from ..models.opening_explorer_lichess_response_200_moves_item_game_type_0_black import OpeningExplorerLichessResponse200MovesItemGameType0Black
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_winner(data: object) -> Union[None, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType1, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType2Type1, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType3Type1]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_1 = OpeningExplorerLichessResponse200MovesItemGameType0WinnerType1(data)



                return winner_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_2_type_1 = OpeningExplorerLichessResponse200MovesItemGameType0WinnerType2Type1(data)



                return winner_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_3_type_1 = OpeningExplorerLichessResponse200MovesItemGameType0WinnerType3Type1(data)



                return winner_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[None, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType1, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType2Type1, OpeningExplorerLichessResponse200MovesItemGameType0WinnerType3Type1], data)

        winner = _parse_winner(d.pop("winner"))


        white = OpeningExplorerLichessResponse200MovesItemGameType0White.from_dict(d.pop("white"))




        black = OpeningExplorerLichessResponse200MovesItemGameType0Black.from_dict(d.pop("black"))




        year = d.pop("year")

        def _parse_month(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        month = _parse_month(d.pop("month"))


        _speed = d.pop("speed", UNSET)
        speed: Union[Unset, OpeningExplorerLichessResponse200MovesItemGameType0Speed]
        if isinstance(_speed,  Unset):
            speed = UNSET
        else:
            speed = OpeningExplorerLichessResponse200MovesItemGameType0Speed(_speed)




        opening_explorer_lichess_response_200_moves_item_game_type_0 = cls(
            id=id,
            winner=winner,
            white=white,
            black=black,
            year=year,
            month=month,
            speed=speed,
        )


        opening_explorer_lichess_response_200_moves_item_game_type_0.additional_properties = d
        return opening_explorer_lichess_response_200_moves_item_game_type_0

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
