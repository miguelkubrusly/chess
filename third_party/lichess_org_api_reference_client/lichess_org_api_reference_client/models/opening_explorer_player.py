from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.opening_explorer_player_moves_item import OpeningExplorerPlayerMovesItem
  from ..models.opening_explorer_player_opening_type_0 import OpeningExplorerPlayerOpeningType0
  from ..models.opening_explorer_player_recent_games_item import OpeningExplorerPlayerRecentGamesItem





T = TypeVar("T", bound="OpeningExplorerPlayer")



@_attrs_define
class OpeningExplorerPlayer:
    """ 
        Example:
            {'opening': {'eco': 'D00', 'name': "Queen's Pawn Game"}, 'queuePosition': 25, 'white': 366, 'draws': 23,
                'black': 279, 'moves': [{'uci': 'c2c4', 'san': 'c4', 'averageOpponentRating': 1695, 'performance': 1744,
                'white': 361, 'draws': 23, 'black': 272, 'game': None, 'opening': {'eco': 'D06', 'name': "Queen's Gambit"}},
                {'uci': 'c2c3', 'san': 'c3', 'averageOpponentRating': 1797, 'performance': 1797, 'white': 2, 'draws': 0,
                'black': 2, 'game': None, 'opening': None}, {'uci': 'e2e4', 'san': 'e4', 'averageOpponentRating': 1762,
                'performance': 1640, 'white': 1, 'draws': 0, 'black': 2, 'game': None, 'opening': {'eco': 'D00', 'name':
                'Blackmar-Diemer Gambit'}}, {'uci': 'g1f3', 'san': 'Nf3', 'averageOpponentRating': 1497, 'performance': 1374,
                'white': 1, 'draws': 0, 'black': 2, 'game': None, 'opening': {'eco': 'D02', 'name': "Queen's Pawn Game:
                Zukertort Variation"}}, {'uci': 'h2h4', 'san': 'h4', 'averageOpponentRating': 1674, 'performance': 874, 'white':
                0, 'draws': 0, 'black': 1, 'game': {'id': '9vA24xBn', 'winner': 'black', 'speed': 'bullet', 'mode': 'rated',
                'black': {'name': 'MentalBlood', 'rating': 1674}, 'white': {'name': 'revoof', 'rating': 1657}, 'year': 2020,
                'month': '2020-06'}, 'opening': None}], 'recentGames': [{'uci': 'c2c4', 'id': 'ycZbWQZO', 'winner': 'white',
                'speed': 'bullet', 'mode': 'rated', 'black': {'name': 'Winavesh', 'rating': 1700}, 'white': {'name': 'revoof',
                'rating': 1700}, 'year': 2024, 'month': '2024-11'}]}

        Attributes:
            opening (Union['OpeningExplorerPlayerOpeningType0', None]):
            queue_position (float): Waiting for other players to be indexed first
            white (float):
            draws (float):
            black (float):
            moves (list['OpeningExplorerPlayerMovesItem']):
            recent_games (list['OpeningExplorerPlayerRecentGamesItem']):
     """

    opening: Union['OpeningExplorerPlayerOpeningType0', None]
    queue_position: float
    white: float
    draws: float
    black: float
    moves: list['OpeningExplorerPlayerMovesItem']
    recent_games: list['OpeningExplorerPlayerRecentGamesItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.opening_explorer_player_moves_item import OpeningExplorerPlayerMovesItem
        from ..models.opening_explorer_player_opening_type_0 import OpeningExplorerPlayerOpeningType0
        from ..models.opening_explorer_player_recent_games_item import OpeningExplorerPlayerRecentGamesItem
        opening: Union[None, dict[str, Any]]
        if isinstance(self.opening, OpeningExplorerPlayerOpeningType0):
            opening = self.opening.to_dict()
        else:
            opening = self.opening

        queue_position = self.queue_position

        white = self.white

        draws = self.draws

        black = self.black

        moves = []
        for moves_item_data in self.moves:
            moves_item = moves_item_data.to_dict()
            moves.append(moves_item)



        recent_games = []
        for recent_games_item_data in self.recent_games:
            recent_games_item = recent_games_item_data.to_dict()
            recent_games.append(recent_games_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "opening": opening,
            "queuePosition": queue_position,
            "white": white,
            "draws": draws,
            "black": black,
            "moves": moves,
            "recentGames": recent_games,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opening_explorer_player_moves_item import OpeningExplorerPlayerMovesItem
        from ..models.opening_explorer_player_opening_type_0 import OpeningExplorerPlayerOpeningType0
        from ..models.opening_explorer_player_recent_games_item import OpeningExplorerPlayerRecentGamesItem
        d = dict(src_dict)
        def _parse_opening(data: object) -> Union['OpeningExplorerPlayerOpeningType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                opening_type_0 = OpeningExplorerPlayerOpeningType0.from_dict(data)



                return opening_type_0
            except: # noqa: E722
                pass
            return cast(Union['OpeningExplorerPlayerOpeningType0', None], data)

        opening = _parse_opening(d.pop("opening"))


        queue_position = d.pop("queuePosition")

        white = d.pop("white")

        draws = d.pop("draws")

        black = d.pop("black")

        moves = []
        _moves = d.pop("moves")
        for moves_item_data in (_moves):
            moves_item = OpeningExplorerPlayerMovesItem.from_dict(moves_item_data)



            moves.append(moves_item)


        recent_games = []
        _recent_games = d.pop("recentGames")
        for recent_games_item_data in (_recent_games):
            recent_games_item = OpeningExplorerPlayerRecentGamesItem.from_dict(recent_games_item_data)



            recent_games.append(recent_games_item)


        opening_explorer_player = cls(
            opening=opening,
            queue_position=queue_position,
            white=white,
            draws=draws,
            black=black,
            moves=moves,
            recent_games=recent_games,
        )


        opening_explorer_player.additional_properties = d
        return opening_explorer_player

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
