from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.puzzle_and_game_game_players_item import PuzzleAndGameGamePlayersItem
  from ..models.puzzle_and_game_game_perf import PuzzleAndGameGamePerf





T = TypeVar("T", bound="PuzzleAndGameGame")



@_attrs_define
class PuzzleAndGameGame:
    """ 
        Attributes:
            clock (str):
            id (str):
            perf (PuzzleAndGameGamePerf):
            pgn (str):
            players (list['PuzzleAndGameGamePlayersItem']):
            rated (bool):
     """

    clock: str
    id: str
    perf: 'PuzzleAndGameGamePerf'
    pgn: str
    players: list['PuzzleAndGameGamePlayersItem']
    rated: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.puzzle_and_game_game_players_item import PuzzleAndGameGamePlayersItem
        from ..models.puzzle_and_game_game_perf import PuzzleAndGameGamePerf
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
        from ..models.puzzle_and_game_game_players_item import PuzzleAndGameGamePlayersItem
        from ..models.puzzle_and_game_game_perf import PuzzleAndGameGamePerf
        d = dict(src_dict)
        clock = d.pop("clock")

        id = d.pop("id")

        perf = PuzzleAndGameGamePerf.from_dict(d.pop("perf"))




        pgn = d.pop("pgn")

        players = []
        _players = d.pop("players")
        for players_item_data in (_players):
            players_item = PuzzleAndGameGamePlayersItem.from_dict(players_item_data)



            players.append(players_item)


        rated = d.pop("rated")

        puzzle_and_game_game = cls(
            clock=clock,
            id=id,
            perf=perf,
            pgn=pgn,
            players=players,
            rated=rated,
        )

        return puzzle_and_game_game

