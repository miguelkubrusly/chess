from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.opening_explorer_master_response_200_top_games_item_winner_type_1 import OpeningExplorerMasterResponse200TopGamesItemWinnerType1
from ..models.opening_explorer_master_response_200_top_games_item_winner_type_2_type_1 import OpeningExplorerMasterResponse200TopGamesItemWinnerType2Type1
from ..models.opening_explorer_master_response_200_top_games_item_winner_type_3_type_1 import OpeningExplorerMasterResponse200TopGamesItemWinnerType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.opening_explorer_master_response_200_top_games_item_white import OpeningExplorerMasterResponse200TopGamesItemWhite
  from ..models.opening_explorer_master_response_200_top_games_item_black import OpeningExplorerMasterResponse200TopGamesItemBlack





T = TypeVar("T", bound="OpeningExplorerMasterResponse200TopGamesItem")



@_attrs_define
class OpeningExplorerMasterResponse200TopGamesItem:
    """ 
        Attributes:
            uci (str):
            id (str):
            winner (Union[None, OpeningExplorerMasterResponse200TopGamesItemWinnerType1,
                OpeningExplorerMasterResponse200TopGamesItemWinnerType2Type1,
                OpeningExplorerMasterResponse200TopGamesItemWinnerType3Type1]):
            white (OpeningExplorerMasterResponse200TopGamesItemWhite):
            black (OpeningExplorerMasterResponse200TopGamesItemBlack):
            year (float):
            month (Union[Unset, str]):
     """

    uci: str
    id: str
    winner: Union[None, OpeningExplorerMasterResponse200TopGamesItemWinnerType1, OpeningExplorerMasterResponse200TopGamesItemWinnerType2Type1, OpeningExplorerMasterResponse200TopGamesItemWinnerType3Type1]
    white: 'OpeningExplorerMasterResponse200TopGamesItemWhite'
    black: 'OpeningExplorerMasterResponse200TopGamesItemBlack'
    year: float
    month: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_master_response_200_top_games_item_white import OpeningExplorerMasterResponse200TopGamesItemWhite
        from ..models.opening_explorer_master_response_200_top_games_item_black import OpeningExplorerMasterResponse200TopGamesItemBlack
        uci = self.uci

        id = self.id

        winner: Union[None, str]
        if isinstance(self.winner, OpeningExplorerMasterResponse200TopGamesItemWinnerType1):
            winner = self.winner.value
        elif isinstance(self.winner, OpeningExplorerMasterResponse200TopGamesItemWinnerType2Type1):
            winner = self.winner.value
        elif isinstance(self.winner, OpeningExplorerMasterResponse200TopGamesItemWinnerType3Type1):
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
            "uci": uci,
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
        from ..models.opening_explorer_master_response_200_top_games_item_white import OpeningExplorerMasterResponse200TopGamesItemWhite
        from ..models.opening_explorer_master_response_200_top_games_item_black import OpeningExplorerMasterResponse200TopGamesItemBlack
        d = dict(src_dict)
        uci = d.pop("uci")

        id = d.pop("id")

        def _parse_winner(data: object) -> Union[None, OpeningExplorerMasterResponse200TopGamesItemWinnerType1, OpeningExplorerMasterResponse200TopGamesItemWinnerType2Type1, OpeningExplorerMasterResponse200TopGamesItemWinnerType3Type1]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_1 = OpeningExplorerMasterResponse200TopGamesItemWinnerType1(data)



                return winner_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_2_type_1 = OpeningExplorerMasterResponse200TopGamesItemWinnerType2Type1(data)



                return winner_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_3_type_1 = OpeningExplorerMasterResponse200TopGamesItemWinnerType3Type1(data)



                return winner_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[None, OpeningExplorerMasterResponse200TopGamesItemWinnerType1, OpeningExplorerMasterResponse200TopGamesItemWinnerType2Type1, OpeningExplorerMasterResponse200TopGamesItemWinnerType3Type1], data)

        winner = _parse_winner(d.pop("winner"))


        white = OpeningExplorerMasterResponse200TopGamesItemWhite.from_dict(d.pop("white"))




        black = OpeningExplorerMasterResponse200TopGamesItemBlack.from_dict(d.pop("black"))




        year = d.pop("year")

        month = d.pop("month", UNSET)

        opening_explorer_master_response_200_top_games_item = cls(
            uci=uci,
            id=id,
            winner=winner,
            white=white,
            black=black,
            year=year,
            month=month,
        )


        opening_explorer_master_response_200_top_games_item.additional_properties = d
        return opening_explorer_master_response_200_top_games_item

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
