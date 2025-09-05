from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.opening_explorer_lichess_moves_item_opening_type_0 import OpeningExplorerLichessMovesItemOpeningType0
  from ..models.opening_explorer_lichess_moves_item_game_type_0 import OpeningExplorerLichessMovesItemGameType0





T = TypeVar("T", bound="OpeningExplorerLichessMovesItem")



@_attrs_define
class OpeningExplorerLichessMovesItem:
    """ 
        Attributes:
            uci (str):
            san (str):
            average_rating (float):
            white (float):
            draws (float):
            black (float):
            game (Union['OpeningExplorerLichessMovesItemGameType0', None]):
            opening (Union['OpeningExplorerLichessMovesItemOpeningType0', None]):
     """

    uci: str
    san: str
    average_rating: float
    white: float
    draws: float
    black: float
    game: Union['OpeningExplorerLichessMovesItemGameType0', None]
    opening: Union['OpeningExplorerLichessMovesItemOpeningType0', None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_lichess_moves_item_opening_type_0 import OpeningExplorerLichessMovesItemOpeningType0
        from ..models.opening_explorer_lichess_moves_item_game_type_0 import OpeningExplorerLichessMovesItemGameType0
        uci = self.uci

        san = self.san

        average_rating = self.average_rating

        white = self.white

        draws = self.draws

        black = self.black

        game: Union[None, dict[str, Any]]
        if isinstance(self.game, OpeningExplorerLichessMovesItemGameType0):
            game = self.game.to_dict()
        else:
            game = self.game

        opening: Union[None, dict[str, Any]]
        if isinstance(self.opening, OpeningExplorerLichessMovesItemOpeningType0):
            opening = self.opening.to_dict()
        else:
            opening = self.opening


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "uci": uci,
            "san": san,
            "averageRating": average_rating,
            "white": white,
            "draws": draws,
            "black": black,
            "game": game,
            "opening": opening,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opening_explorer_lichess_moves_item_opening_type_0 import OpeningExplorerLichessMovesItemOpeningType0
        from ..models.opening_explorer_lichess_moves_item_game_type_0 import OpeningExplorerLichessMovesItemGameType0
        d = dict(src_dict)
        uci = d.pop("uci")

        san = d.pop("san")

        average_rating = d.pop("averageRating")

        white = d.pop("white")

        draws = d.pop("draws")

        black = d.pop("black")

        def _parse_game(data: object) -> Union['OpeningExplorerLichessMovesItemGameType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                game_type_0 = OpeningExplorerLichessMovesItemGameType0.from_dict(data)



                return game_type_0
            except: # noqa: E722
                pass
            return cast(Union['OpeningExplorerLichessMovesItemGameType0', None], data)

        game = _parse_game(d.pop("game"))


        def _parse_opening(data: object) -> Union['OpeningExplorerLichessMovesItemOpeningType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                opening_type_0 = OpeningExplorerLichessMovesItemOpeningType0.from_dict(data)



                return opening_type_0
            except: # noqa: E722
                pass
            return cast(Union['OpeningExplorerLichessMovesItemOpeningType0', None], data)

        opening = _parse_opening(d.pop("opening"))


        opening_explorer_lichess_moves_item = cls(
            uci=uci,
            san=san,
            average_rating=average_rating,
            white=white,
            draws=draws,
            black=black,
            game=game,
            opening=opening,
        )


        opening_explorer_lichess_moves_item.additional_properties = d
        return opening_explorer_lichess_moves_item

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
