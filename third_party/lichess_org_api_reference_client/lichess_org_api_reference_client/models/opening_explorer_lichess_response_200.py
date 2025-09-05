from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.opening_explorer_lichess_response_200_recent_games_item import OpeningExplorerLichessResponse200RecentGamesItem
  from ..models.opening_explorer_lichess_response_200_history_item import OpeningExplorerLichessResponse200HistoryItem
  from ..models.opening_explorer_lichess_response_200_opening_type_0 import OpeningExplorerLichessResponse200OpeningType0
  from ..models.opening_explorer_lichess_response_200_moves_item import OpeningExplorerLichessResponse200MovesItem
  from ..models.opening_explorer_lichess_response_200_top_games_item import OpeningExplorerLichessResponse200TopGamesItem





T = TypeVar("T", bound="OpeningExplorerLichessResponse200")



@_attrs_define
class OpeningExplorerLichessResponse200:
    """ 
        Attributes:
            opening (Union['OpeningExplorerLichessResponse200OpeningType0', None]):
            white (float):
            draws (float):
            black (float):
            moves (list['OpeningExplorerLichessResponse200MovesItem']):
            top_games (list['OpeningExplorerLichessResponse200TopGamesItem']):
            recent_games (Union[Unset, list['OpeningExplorerLichessResponse200RecentGamesItem']]):
            history (Union[Unset, list['OpeningExplorerLichessResponse200HistoryItem']]):
     """

    opening: Union['OpeningExplorerLichessResponse200OpeningType0', None]
    white: float
    draws: float
    black: float
    moves: list['OpeningExplorerLichessResponse200MovesItem']
    top_games: list['OpeningExplorerLichessResponse200TopGamesItem']
    recent_games: Union[Unset, list['OpeningExplorerLichessResponse200RecentGamesItem']] = UNSET
    history: Union[Unset, list['OpeningExplorerLichessResponse200HistoryItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_lichess_response_200_recent_games_item import OpeningExplorerLichessResponse200RecentGamesItem
        from ..models.opening_explorer_lichess_response_200_history_item import OpeningExplorerLichessResponse200HistoryItem
        from ..models.opening_explorer_lichess_response_200_opening_type_0 import OpeningExplorerLichessResponse200OpeningType0
        from ..models.opening_explorer_lichess_response_200_moves_item import OpeningExplorerLichessResponse200MovesItem
        from ..models.opening_explorer_lichess_response_200_top_games_item import OpeningExplorerLichessResponse200TopGamesItem
        opening: Union[None, dict[str, Any]]
        if isinstance(self.opening, OpeningExplorerLichessResponse200OpeningType0):
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



        recent_games: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.recent_games, Unset):
            recent_games = []
            for recent_games_item_data in self.recent_games:
                recent_games_item = recent_games_item_data.to_dict()
                recent_games.append(recent_games_item)



        history: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)




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
        if recent_games is not UNSET:
            field_dict["recentGames"] = recent_games
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opening_explorer_lichess_response_200_recent_games_item import OpeningExplorerLichessResponse200RecentGamesItem
        from ..models.opening_explorer_lichess_response_200_history_item import OpeningExplorerLichessResponse200HistoryItem
        from ..models.opening_explorer_lichess_response_200_opening_type_0 import OpeningExplorerLichessResponse200OpeningType0
        from ..models.opening_explorer_lichess_response_200_moves_item import OpeningExplorerLichessResponse200MovesItem
        from ..models.opening_explorer_lichess_response_200_top_games_item import OpeningExplorerLichessResponse200TopGamesItem
        d = dict(src_dict)
        def _parse_opening(data: object) -> Union['OpeningExplorerLichessResponse200OpeningType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                opening_type_0 = OpeningExplorerLichessResponse200OpeningType0.from_dict(data)



                return opening_type_0
            except: # noqa: E722
                pass
            return cast(Union['OpeningExplorerLichessResponse200OpeningType0', None], data)

        opening = _parse_opening(d.pop("opening"))


        white = d.pop("white")

        draws = d.pop("draws")

        black = d.pop("black")

        moves = []
        _moves = d.pop("moves")
        for moves_item_data in (_moves):
            moves_item = OpeningExplorerLichessResponse200MovesItem.from_dict(moves_item_data)



            moves.append(moves_item)


        top_games = []
        _top_games = d.pop("topGames")
        for top_games_item_data in (_top_games):
            top_games_item = OpeningExplorerLichessResponse200TopGamesItem.from_dict(top_games_item_data)



            top_games.append(top_games_item)


        recent_games = []
        _recent_games = d.pop("recentGames", UNSET)
        for recent_games_item_data in (_recent_games or []):
            recent_games_item = OpeningExplorerLichessResponse200RecentGamesItem.from_dict(recent_games_item_data)



            recent_games.append(recent_games_item)


        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in (_history or []):
            history_item = OpeningExplorerLichessResponse200HistoryItem.from_dict(history_item_data)



            history.append(history_item)


        opening_explorer_lichess_response_200 = cls(
            opening=opening,
            white=white,
            draws=draws,
            black=black,
            moves=moves,
            top_games=top_games,
            recent_games=recent_games,
            history=history,
        )


        opening_explorer_lichess_response_200.additional_properties = d
        return opening_explorer_lichess_response_200

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
