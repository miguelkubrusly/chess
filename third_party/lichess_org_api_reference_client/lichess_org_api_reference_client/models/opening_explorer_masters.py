from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.opening_explorer_masters_opening_type_0 import OpeningExplorerMastersOpeningType0
  from ..models.opening_explorer_masters_top_games_item import OpeningExplorerMastersTopGamesItem
  from ..models.opening_explorer_masters_moves_item import OpeningExplorerMastersMovesItem





T = TypeVar("T", bound="OpeningExplorerMasters")



@_attrs_define
class OpeningExplorerMasters:
    """ 
        Attributes:
            opening (Union['OpeningExplorerMastersOpeningType0', None]):
            white (float):
            draws (float):
            black (float):
            moves (list['OpeningExplorerMastersMovesItem']):
            top_games (list['OpeningExplorerMastersTopGamesItem']):
     """

    opening: Union['OpeningExplorerMastersOpeningType0', None]
    white: float
    draws: float
    black: float
    moves: list['OpeningExplorerMastersMovesItem']
    top_games: list['OpeningExplorerMastersTopGamesItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_masters_opening_type_0 import OpeningExplorerMastersOpeningType0
        from ..models.opening_explorer_masters_top_games_item import OpeningExplorerMastersTopGamesItem
        from ..models.opening_explorer_masters_moves_item import OpeningExplorerMastersMovesItem
        opening: Union[None, dict[str, Any]]
        if isinstance(self.opening, OpeningExplorerMastersOpeningType0):
            opening = self.opening.to_dict()
        else:
            opening = self.opening

        white = self.white

        draws = self.draws

        black = self.black

        moves = []
        for moves_item_data in self.moves:
            moves_item = moves_item_data.to_dict()
            moves.append(moves_item)



        top_games = []
        for top_games_item_data in self.top_games:
            top_games_item = top_games_item_data.to_dict()
            top_games.append(top_games_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "opening": opening,
            "white": white,
            "draws": draws,
            "black": black,
            "moves": moves,
            "topGames": top_games,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opening_explorer_masters_opening_type_0 import OpeningExplorerMastersOpeningType0
        from ..models.opening_explorer_masters_top_games_item import OpeningExplorerMastersTopGamesItem
        from ..models.opening_explorer_masters_moves_item import OpeningExplorerMastersMovesItem
        d = dict(src_dict)
        def _parse_opening(data: object) -> Union['OpeningExplorerMastersOpeningType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                opening_type_0 = OpeningExplorerMastersOpeningType0.from_dict(data)



                return opening_type_0
            except: # noqa: E722
                pass
            return cast(Union['OpeningExplorerMastersOpeningType0', None], data)

        opening = _parse_opening(d.pop("opening"))


        white = d.pop("white")

        draws = d.pop("draws")

        black = d.pop("black")

        moves = []
        _moves = d.pop("moves")
        for moves_item_data in (_moves):
            moves_item = OpeningExplorerMastersMovesItem.from_dict(moves_item_data)



            moves.append(moves_item)


        top_games = []
        _top_games = d.pop("topGames")
        for top_games_item_data in (_top_games):
            top_games_item = OpeningExplorerMastersTopGamesItem.from_dict(top_games_item_data)



            top_games.append(top_games_item)


        opening_explorer_masters = cls(
            opening=opening,
            white=white,
            draws=draws,
            black=black,
            moves=moves,
            top_games=top_games,
        )


        opening_explorer_masters.additional_properties = d
        return opening_explorer_masters

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
