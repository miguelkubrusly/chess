from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.game_event_info_color import GameEventInfoColor
from ..models.game_event_info_source import GameEventInfoSource
from ..models.game_event_info_speed import GameEventInfoSpeed
from ..models.game_event_info_winner import GameEventInfoWinner
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.game_event_info_player import GameEventInfoPlayer
  from ..models.game_event_info_status import GameEventInfoStatus
  from ..models.game_event_info_compat import GameEventInfoCompat
  from ..models.game_event_info_variant import GameEventInfoVariant
  from ..models.game_event_info_ai_opponent import GameEventInfoAIOpponent





T = TypeVar("T", bound="GameEventInfo")



@_attrs_define
class GameEventInfo:
    """ 
        Attributes:
            full_id (str):
            game_id (str):
            fen (Union[Unset, str]):
            color (Union[Unset, GameEventInfoColor]):
            last_move (Union[Unset, str]):
            source (Union[Unset, GameEventInfoSource]):
            status (Union[Unset, GameEventInfoStatus]):
            variant (Union[Unset, GameEventInfoVariant]):
            speed (Union[Unset, GameEventInfoSpeed]):
            perf (Union[Unset, str]):
            rated (Union[Unset, bool]):
            has_moved (Union[Unset, bool]):
            opponent (Union['GameEventInfoAIOpponent', 'GameEventInfoPlayer', Unset]):
            is_my_turn (Union[Unset, bool]):
            seconds_left (Union[Unset, int]):
            winner (Union[Unset, GameEventInfoWinner]):
            rating_diff (Union[Unset, int]):
            compat (Union[Unset, GameEventInfoCompat]):
            id (Union[Unset, str]):
     """

    full_id: str
    game_id: str
    fen: Union[Unset, str] = UNSET
    color: Union[Unset, GameEventInfoColor] = UNSET
    last_move: Union[Unset, str] = UNSET
    source: Union[Unset, GameEventInfoSource] = UNSET
    status: Union[Unset, 'GameEventInfoStatus'] = UNSET
    variant: Union[Unset, 'GameEventInfoVariant'] = UNSET
    speed: Union[Unset, GameEventInfoSpeed] = UNSET
    perf: Union[Unset, str] = UNSET
    rated: Union[Unset, bool] = UNSET
    has_moved: Union[Unset, bool] = UNSET
    opponent: Union['GameEventInfoAIOpponent', 'GameEventInfoPlayer', Unset] = UNSET
    is_my_turn: Union[Unset, bool] = UNSET
    seconds_left: Union[Unset, int] = UNSET
    winner: Union[Unset, GameEventInfoWinner] = UNSET
    rating_diff: Union[Unset, int] = UNSET
    compat: Union[Unset, 'GameEventInfoCompat'] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.game_event_info_player import GameEventInfoPlayer
        from ..models.game_event_info_status import GameEventInfoStatus
        from ..models.game_event_info_compat import GameEventInfoCompat
        from ..models.game_event_info_variant import GameEventInfoVariant
        from ..models.game_event_info_ai_opponent import GameEventInfoAIOpponent
        full_id = self.full_id

        game_id = self.game_id

        fen = self.fen

        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value


        last_move = self.last_move

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        variant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.to_dict()

        speed: Union[Unset, str] = UNSET
        if not isinstance(self.speed, Unset):
            speed = self.speed.value


        perf = self.perf

        rated = self.rated

        has_moved = self.has_moved

        opponent: Union[Unset, dict[str, Any]]
        if isinstance(self.opponent, Unset):
            opponent = UNSET
        elif isinstance(self.opponent, GameEventInfoPlayer):
            opponent = self.opponent.to_dict()
        else:
            opponent = self.opponent.to_dict()


        is_my_turn = self.is_my_turn

        seconds_left = self.seconds_left

        winner: Union[Unset, str] = UNSET
        if not isinstance(self.winner, Unset):
            winner = self.winner.value


        rating_diff = self.rating_diff

        compat: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.compat, Unset):
            compat = self.compat.to_dict()

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fullId": full_id,
            "gameId": game_id,
        })
        if fen is not UNSET:
            field_dict["fen"] = fen
        if color is not UNSET:
            field_dict["color"] = color
        if last_move is not UNSET:
            field_dict["lastMove"] = last_move
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if variant is not UNSET:
            field_dict["variant"] = variant
        if speed is not UNSET:
            field_dict["speed"] = speed
        if perf is not UNSET:
            field_dict["perf"] = perf
        if rated is not UNSET:
            field_dict["rated"] = rated
        if has_moved is not UNSET:
            field_dict["hasMoved"] = has_moved
        if opponent is not UNSET:
            field_dict["opponent"] = opponent
        if is_my_turn is not UNSET:
            field_dict["isMyTurn"] = is_my_turn
        if seconds_left is not UNSET:
            field_dict["secondsLeft"] = seconds_left
        if winner is not UNSET:
            field_dict["winner"] = winner
        if rating_diff is not UNSET:
            field_dict["ratingDiff"] = rating_diff
        if compat is not UNSET:
            field_dict["compat"] = compat
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_event_info_player import GameEventInfoPlayer
        from ..models.game_event_info_status import GameEventInfoStatus
        from ..models.game_event_info_compat import GameEventInfoCompat
        from ..models.game_event_info_variant import GameEventInfoVariant
        from ..models.game_event_info_ai_opponent import GameEventInfoAIOpponent
        d = dict(src_dict)
        full_id = d.pop("fullId")

        game_id = d.pop("gameId")

        fen = d.pop("fen", UNSET)

        _color = d.pop("color", UNSET)
        color: Union[Unset, GameEventInfoColor]
        if isinstance(_color,  Unset):
            color = UNSET
        else:
            color = GameEventInfoColor(_color)




        last_move = d.pop("lastMove", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, GameEventInfoSource]
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = GameEventInfoSource(_source)




        _status = d.pop("status", UNSET)
        status: Union[Unset, GameEventInfoStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = GameEventInfoStatus.from_dict(_status)




        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, GameEventInfoVariant]
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = GameEventInfoVariant.from_dict(_variant)




        _speed = d.pop("speed", UNSET)
        speed: Union[Unset, GameEventInfoSpeed]
        if isinstance(_speed,  Unset):
            speed = UNSET
        else:
            speed = GameEventInfoSpeed(_speed)




        perf = d.pop("perf", UNSET)

        rated = d.pop("rated", UNSET)

        has_moved = d.pop("hasMoved", UNSET)

        def _parse_opponent(data: object) -> Union['GameEventInfoAIOpponent', 'GameEventInfoPlayer', Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                opponent_player = GameEventInfoPlayer.from_dict(data)



                return opponent_player
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            opponent_ai_opponent = GameEventInfoAIOpponent.from_dict(data)



            return opponent_ai_opponent

        opponent = _parse_opponent(d.pop("opponent", UNSET))


        is_my_turn = d.pop("isMyTurn", UNSET)

        seconds_left = d.pop("secondsLeft", UNSET)

        _winner = d.pop("winner", UNSET)
        winner: Union[Unset, GameEventInfoWinner]
        if isinstance(_winner,  Unset):
            winner = UNSET
        else:
            winner = GameEventInfoWinner(_winner)




        rating_diff = d.pop("ratingDiff", UNSET)

        _compat = d.pop("compat", UNSET)
        compat: Union[Unset, GameEventInfoCompat]
        if isinstance(_compat,  Unset):
            compat = UNSET
        else:
            compat = GameEventInfoCompat.from_dict(_compat)




        id = d.pop("id", UNSET)

        game_event_info = cls(
            full_id=full_id,
            game_id=game_id,
            fen=fen,
            color=color,
            last_move=last_move,
            source=source,
            status=status,
            variant=variant,
            speed=speed,
            perf=perf,
            rated=rated,
            has_moved=has_moved,
            opponent=opponent,
            is_my_turn=is_my_turn,
            seconds_left=seconds_left,
            winner=winner,
            rating_diff=rating_diff,
            compat=compat,
            id=id,
        )


        game_event_info.additional_properties = d
        return game_event_info

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
