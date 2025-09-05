from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.game_full_event_speed import GameFullEventSpeed
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast
from typing import Union

if TYPE_CHECKING:
  from ..models.game_full_event_perf import GameFullEventPerf
  from ..models.game_full_event_black import GameFullEventBlack
  from ..models.game_full_event_state import GameFullEventState
  from ..models.game_full_event_variant import GameFullEventVariant
  from ..models.game_full_event_white import GameFullEventWhite
  from ..models.game_full_event_clock import GameFullEventClock





T = TypeVar("T", bound="GameFullEvent")



@_attrs_define
class GameFullEvent:
    """ 
        Example:
            {'id': 'BEOucQJo', 'variant': {'key': 'standard', 'name': 'Standard', 'short': 'Std'}, 'speed': 'rapid', 'perf':
                {'name': 'Rapid'}, 'rated': False, 'createdAt': 1745112707998, 'white': {'id': 'bobby', 'name': 'Bobby',
                'title': None, 'rating': 1751}, 'black': {'id': 'mary', 'name': 'Mary', 'title': None, 'rating': 1021},
                'initialFen': 'startpos', 'clock': {'initial': 900000, 'increment': 0}, 'type': 'gameFull', 'state': {'type':
                'gameState', 'moves': 'd2d3', 'wtime': 900000, 'btime': 900000, 'winc': 0, 'binc': 0, 'status': 'started'}}

        Attributes:
            type_ (Literal['gameFull']):
            id (str):
            variant (GameFullEventVariant):
            speed (GameFullEventSpeed):
            perf (GameFullEventPerf):
            rated (bool):
            created_at (int):
            white (GameFullEventWhite):
            black (GameFullEventBlack):
            initial_fen (str):  Default: 'startpos'.
            state (GameFullEventState):  Example: {'type': 'gameState', 'moves': 'e2e4 c7c5 f2f4 d7d6 g1f3 b8c6 f1c4 g8f6
                d2d3 g7g6 e1g1 f8g7 b1c3', 'wtime': 7598040, 'btime': 8395220, 'winc': 10000, 'binc': 10000, 'wdraw': False,
                'bdraw': False, 'wtakeback': False, 'btakeback': False, 'status': 'started'}.
            clock (Union[Unset, GameFullEventClock]):
            days_per_turn (Union[Unset, int]): If the game is correspondence
            tournament_id (Union[Unset, str]):
     """

    type_: Literal['gameFull']
    id: str
    variant: 'GameFullEventVariant'
    speed: GameFullEventSpeed
    perf: 'GameFullEventPerf'
    rated: bool
    created_at: int
    white: 'GameFullEventWhite'
    black: 'GameFullEventBlack'
    state: 'GameFullEventState'
    initial_fen: str = 'startpos'
    clock: Union[Unset, 'GameFullEventClock'] = UNSET
    days_per_turn: Union[Unset, int] = UNSET
    tournament_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.game_full_event_perf import GameFullEventPerf
        from ..models.game_full_event_black import GameFullEventBlack
        from ..models.game_full_event_state import GameFullEventState
        from ..models.game_full_event_variant import GameFullEventVariant
        from ..models.game_full_event_white import GameFullEventWhite
        from ..models.game_full_event_clock import GameFullEventClock
        type_ = self.type_

        id = self.id

        variant = self.variant.to_dict()

        speed = self.speed.value

        perf = self.perf.to_dict()

        rated = self.rated

        created_at = self.created_at

        white = self.white.to_dict()

        black = self.black.to_dict()

        initial_fen = self.initial_fen

        state = self.state.to_dict()

        clock: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict()

        days_per_turn = self.days_per_turn

        tournament_id = self.tournament_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "id": id,
            "variant": variant,
            "speed": speed,
            "perf": perf,
            "rated": rated,
            "createdAt": created_at,
            "white": white,
            "black": black,
            "initialFen": initial_fen,
            "state": state,
        })
        if clock is not UNSET:
            field_dict["clock"] = clock
        if days_per_turn is not UNSET:
            field_dict["daysPerTurn"] = days_per_turn
        if tournament_id is not UNSET:
            field_dict["tournamentId"] = tournament_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_full_event_perf import GameFullEventPerf
        from ..models.game_full_event_black import GameFullEventBlack
        from ..models.game_full_event_state import GameFullEventState
        from ..models.game_full_event_variant import GameFullEventVariant
        from ..models.game_full_event_white import GameFullEventWhite
        from ..models.game_full_event_clock import GameFullEventClock
        d = dict(src_dict)
        type_ = cast(Literal['gameFull'] , d.pop("type"))
        if type_ != 'gameFull':
            raise ValueError(f"type must match const 'gameFull', got '{type_}'")

        id = d.pop("id")

        variant = GameFullEventVariant.from_dict(d.pop("variant"))




        speed = GameFullEventSpeed(d.pop("speed"))




        perf = GameFullEventPerf.from_dict(d.pop("perf"))




        rated = d.pop("rated")

        created_at = d.pop("createdAt")

        white = GameFullEventWhite.from_dict(d.pop("white"))




        black = GameFullEventBlack.from_dict(d.pop("black"))




        initial_fen = d.pop("initialFen")

        state = GameFullEventState.from_dict(d.pop("state"))




        _clock = d.pop("clock", UNSET)
        clock: Union[Unset, GameFullEventClock]
        if isinstance(_clock,  Unset):
            clock = UNSET
        else:
            clock = GameFullEventClock.from_dict(_clock)




        days_per_turn = d.pop("daysPerTurn", UNSET)

        tournament_id = d.pop("tournamentId", UNSET)

        game_full_event = cls(
            type_=type_,
            id=id,
            variant=variant,
            speed=speed,
            perf=perf,
            rated=rated,
            created_at=created_at,
            white=white,
            black=black,
            initial_fen=initial_fen,
            state=state,
            clock=clock,
            days_per_turn=days_per_turn,
            tournament_id=tournament_id,
        )


        game_full_event.additional_properties = d
        return game_full_event

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
