from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_puzzle_id_response_200_game_perf import ApiPuzzleIdResponse200GamePerf
  from ..models.api_puzzle_id_response_200_game_players_item import ApiPuzzleIdResponse200GamePlayersItem





T = TypeVar("T", bound="ApiPuzzleIdResponse200Game")



@_attrs_define
class ApiPuzzleIdResponse200Game:
    """ 
        Attributes:
            clock (str):
            id (str):
            perf (ApiPuzzleIdResponse200GamePerf):
            pgn (str):
            players (list['ApiPuzzleIdResponse200GamePlayersItem']):
            rated (bool):
     """

    clock: str
    id: str
    perf: 'ApiPuzzleIdResponse200GamePerf'
    pgn: str
    players: list['ApiPuzzleIdResponse200GamePlayersItem']
    rated: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_puzzle_id_response_200_game_perf import ApiPuzzleIdResponse200GamePerf
        from ..models.api_puzzle_id_response_200_game_players_item import ApiPuzzleIdResponse200GamePlayersItem
        clock = self.clock

        id = self.id

        perf = self.perf.to_dict()

        pgn = self.pgn

        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)



        rated = self.rated


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "clock": clock,
            "id": id,
            "perf": perf,
            "pgn": pgn,
            "players": players,
            "rated": rated,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_puzzle_id_response_200_game_perf import ApiPuzzleIdResponse200GamePerf
        from ..models.api_puzzle_id_response_200_game_players_item import ApiPuzzleIdResponse200GamePlayersItem
        d = dict(src_dict)
        clock = d.pop("clock")

        id = d.pop("id")

        perf = ApiPuzzleIdResponse200GamePerf.from_dict(d.pop("perf"))




        pgn = d.pop("pgn")

        players = []
        _players = d.pop("players")
        for players_item_data in (_players):
            players_item = ApiPuzzleIdResponse200GamePlayersItem.from_dict(players_item_data)



            players.append(players_item)


        rated = d.pop("rated")

        api_puzzle_id_response_200_game = cls(
            clock=clock,
            id=id,
            perf=perf,
            pgn=pgn,
            players=players,
            rated=rated,
        )

        return api_puzzle_id_response_200_game

