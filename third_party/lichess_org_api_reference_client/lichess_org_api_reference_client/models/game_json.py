from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.game_json_speed import GameJsonSpeed
from ..models.game_json_status import GameJsonStatus
from ..models.game_json_variant import GameJsonVariant
from ..models.game_json_winner import GameJsonWinner
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.game_json_division import GameJsonDivision
  from ..models.game_json_analysis_item import GameJsonAnalysisItem
  from ..models.game_json_players import GameJsonPlayers
  from ..models.game_json_clock import GameJsonClock
  from ..models.game_json_opening import GameJsonOpening





T = TypeVar("T", bound="GameJson")



@_attrs_define
class GameJson:
    """ 
        Attributes:
            id (str):
            rated (bool):
            variant (GameJsonVariant):  Default: GameJsonVariant.STANDARD. Example: standard.
            speed (GameJsonSpeed):
            perf (str):
            created_at (int):
            last_move_at (int):
            status (GameJsonStatus):
            players (GameJsonPlayers):
            source (Union[Unset, str]):
            initial_fen (Union[Unset, str]):
            winner (Union[Unset, GameJsonWinner]):
            opening (Union[Unset, GameJsonOpening]):
            moves (Union[Unset, str]):
            pgn (Union[Unset, str]):
            days_per_turn (Union[Unset, int]):
            analysis (Union[Unset, list['GameJsonAnalysisItem']]):
            tournament (Union[Unset, str]):
            swiss (Union[Unset, str]):
            clock (Union[Unset, GameJsonClock]):
            clocks (Union[Unset, list[int]]):
            division (Union[Unset, GameJsonDivision]):
     """

    id: str
    rated: bool
    speed: GameJsonSpeed
    perf: str
    created_at: int
    last_move_at: int
    status: GameJsonStatus
    players: 'GameJsonPlayers'
    variant: GameJsonVariant = GameJsonVariant.STANDARD
    source: Union[Unset, str] = UNSET
    initial_fen: Union[Unset, str] = UNSET
    winner: Union[Unset, GameJsonWinner] = UNSET
    opening: Union[Unset, 'GameJsonOpening'] = UNSET
    moves: Union[Unset, str] = UNSET
    pgn: Union[Unset, str] = UNSET
    days_per_turn: Union[Unset, int] = UNSET
    analysis: Union[Unset, list['GameJsonAnalysisItem']] = UNSET
    tournament: Union[Unset, str] = UNSET
    swiss: Union[Unset, str] = UNSET
    clock: Union[Unset, 'GameJsonClock'] = UNSET
    clocks: Union[Unset, list[int]] = UNSET
    division: Union[Unset, 'GameJsonDivision'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.game_json_division import GameJsonDivision
        from ..models.game_json_analysis_item import GameJsonAnalysisItem
        from ..models.game_json_players import GameJsonPlayers
        from ..models.game_json_clock import GameJsonClock
        from ..models.game_json_opening import GameJsonOpening
        id = self.id

        rated = self.rated

        variant = self.variant.value

        speed = self.speed.value

        perf = self.perf

        created_at = self.created_at

        last_move_at = self.last_move_at

        status = self.status.value

        players = self.players.to_dict()

        source = self.source

        initial_fen = self.initial_fen

        winner: Union[Unset, str] = UNSET
        if not isinstance(self.winner, Unset):
            winner = self.winner.value


        opening: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.opening, Unset):
            opening = self.opening.to_dict()

        moves = self.moves

        pgn = self.pgn

        days_per_turn = self.days_per_turn

        analysis: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.analysis, Unset):
            analysis = []
            for analysis_item_data in self.analysis:
                analysis_item = analysis_item_data.to_dict()
                analysis.append(analysis_item)



        tournament = self.tournament

        swiss = self.swiss

        clock: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict()

        clocks: Union[Unset, list[int]] = UNSET
        if not isinstance(self.clocks, Unset):
            clocks = self.clocks



        division: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.division, Unset):
            division = self.division.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "rated": rated,
            "variant": variant,
            "speed": speed,
            "perf": perf,
            "createdAt": created_at,
            "lastMoveAt": last_move_at,
            "status": status,
            "players": players,
        })
        if source is not UNSET:
            field_dict["source"] = source
        if initial_fen is not UNSET:
            field_dict["initialFen"] = initial_fen
        if winner is not UNSET:
            field_dict["winner"] = winner
        if opening is not UNSET:
            field_dict["opening"] = opening
        if moves is not UNSET:
            field_dict["moves"] = moves
        if pgn is not UNSET:
            field_dict["pgn"] = pgn
        if days_per_turn is not UNSET:
            field_dict["daysPerTurn"] = days_per_turn
        if analysis is not UNSET:
            field_dict["analysis"] = analysis
        if tournament is not UNSET:
            field_dict["tournament"] = tournament
        if swiss is not UNSET:
            field_dict["swiss"] = swiss
        if clock is not UNSET:
            field_dict["clock"] = clock
        if clocks is not UNSET:
            field_dict["clocks"] = clocks
        if division is not UNSET:
            field_dict["division"] = division

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_json_division import GameJsonDivision
        from ..models.game_json_analysis_item import GameJsonAnalysisItem
        from ..models.game_json_players import GameJsonPlayers
        from ..models.game_json_clock import GameJsonClock
        from ..models.game_json_opening import GameJsonOpening
        d = dict(src_dict)
        id = d.pop("id")

        rated = d.pop("rated")

        variant = GameJsonVariant(d.pop("variant"))




        speed = GameJsonSpeed(d.pop("speed"))




        perf = d.pop("perf")

        created_at = d.pop("createdAt")

        last_move_at = d.pop("lastMoveAt")

        status = GameJsonStatus(d.pop("status"))




        players = GameJsonPlayers.from_dict(d.pop("players"))




        source = d.pop("source", UNSET)

        initial_fen = d.pop("initialFen", UNSET)

        _winner = d.pop("winner", UNSET)
        winner: Union[Unset, GameJsonWinner]
        if isinstance(_winner,  Unset):
            winner = UNSET
        else:
            winner = GameJsonWinner(_winner)




        _opening = d.pop("opening", UNSET)
        opening: Union[Unset, GameJsonOpening]
        if isinstance(_opening,  Unset):
            opening = UNSET
        else:
            opening = GameJsonOpening.from_dict(_opening)




        moves = d.pop("moves", UNSET)

        pgn = d.pop("pgn", UNSET)

        days_per_turn = d.pop("daysPerTurn", UNSET)

        analysis = []
        _analysis = d.pop("analysis", UNSET)
        for analysis_item_data in (_analysis or []):
            analysis_item = GameJsonAnalysisItem.from_dict(analysis_item_data)



            analysis.append(analysis_item)


        tournament = d.pop("tournament", UNSET)

        swiss = d.pop("swiss", UNSET)

        _clock = d.pop("clock", UNSET)
        clock: Union[Unset, GameJsonClock]
        if isinstance(_clock,  Unset):
            clock = UNSET
        else:
            clock = GameJsonClock.from_dict(_clock)




        clocks = cast(list[int], d.pop("clocks", UNSET))


        _division = d.pop("division", UNSET)
        division: Union[Unset, GameJsonDivision]
        if isinstance(_division,  Unset):
            division = UNSET
        else:
            division = GameJsonDivision.from_dict(_division)




        game_json = cls(
            id=id,
            rated=rated,
            variant=variant,
            speed=speed,
            perf=perf,
            created_at=created_at,
            last_move_at=last_move_at,
            status=status,
            players=players,
            source=source,
            initial_fen=initial_fen,
            winner=winner,
            opening=opening,
            moves=moves,
            pgn=pgn,
            days_per_turn=days_per_turn,
            analysis=analysis,
            tournament=tournament,
            swiss=swiss,
            clock=clock,
            clocks=clocks,
            division=division,
        )


        game_json.additional_properties = d
        return game_json

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
