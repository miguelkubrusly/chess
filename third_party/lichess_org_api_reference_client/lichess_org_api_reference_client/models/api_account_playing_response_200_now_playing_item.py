from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_account_playing_response_200_now_playing_item_color import ApiAccountPlayingResponse200NowPlayingItemColor
from ..models.api_account_playing_response_200_now_playing_item_perf import ApiAccountPlayingResponse200NowPlayingItemPerf
from ..models.api_account_playing_response_200_now_playing_item_source import ApiAccountPlayingResponse200NowPlayingItemSource
from ..models.api_account_playing_response_200_now_playing_item_speed import ApiAccountPlayingResponse200NowPlayingItemSpeed
from ..models.api_account_playing_response_200_now_playing_item_status import ApiAccountPlayingResponse200NowPlayingItemStatus
from ..models.api_account_playing_response_200_now_playing_item_winner import ApiAccountPlayingResponse200NowPlayingItemWinner
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_account_playing_response_200_now_playing_item_opponent import ApiAccountPlayingResponse200NowPlayingItemOpponent
  from ..models.api_account_playing_response_200_now_playing_item_variant import ApiAccountPlayingResponse200NowPlayingItemVariant





T = TypeVar("T", bound="ApiAccountPlayingResponse200NowPlayingItem")



@_attrs_define
class ApiAccountPlayingResponse200NowPlayingItem:
    """ 
        Attributes:
            full_id (str):
            game_id (str):
            fen (str):
            color (ApiAccountPlayingResponse200NowPlayingItemColor):
            last_move (str):
            source (ApiAccountPlayingResponse200NowPlayingItemSource):
            variant (ApiAccountPlayingResponse200NowPlayingItemVariant):
            speed (ApiAccountPlayingResponse200NowPlayingItemSpeed):
            perf (ApiAccountPlayingResponse200NowPlayingItemPerf):
            rated (bool):
            has_moved (bool):
            opponent (ApiAccountPlayingResponse200NowPlayingItemOpponent):
            is_my_turn (bool):
            seconds_left (float):
            status (Union[Unset, ApiAccountPlayingResponse200NowPlayingItemStatus]):
            tournament_id (Union[Unset, str]):
            swiss_id (Union[Unset, str]):
            winner (Union[Unset, ApiAccountPlayingResponse200NowPlayingItemWinner]):
            rating_diff (Union[Unset, float]):
     """

    full_id: str
    game_id: str
    fen: str
    color: ApiAccountPlayingResponse200NowPlayingItemColor
    last_move: str
    source: ApiAccountPlayingResponse200NowPlayingItemSource
    variant: 'ApiAccountPlayingResponse200NowPlayingItemVariant'
    speed: ApiAccountPlayingResponse200NowPlayingItemSpeed
    perf: ApiAccountPlayingResponse200NowPlayingItemPerf
    rated: bool
    has_moved: bool
    opponent: 'ApiAccountPlayingResponse200NowPlayingItemOpponent'
    is_my_turn: bool
    seconds_left: float
    status: Union[Unset, ApiAccountPlayingResponse200NowPlayingItemStatus] = UNSET
    tournament_id: Union[Unset, str] = UNSET
    swiss_id: Union[Unset, str] = UNSET
    winner: Union[Unset, ApiAccountPlayingResponse200NowPlayingItemWinner] = UNSET
    rating_diff: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_account_playing_response_200_now_playing_item_opponent import ApiAccountPlayingResponse200NowPlayingItemOpponent
        from ..models.api_account_playing_response_200_now_playing_item_variant import ApiAccountPlayingResponse200NowPlayingItemVariant
        full_id = self.full_id

        game_id = self.game_id

        fen = self.fen

        color = self.color.value

        last_move = self.last_move

        source = self.source.value

        variant = self.variant.to_dict()

        speed = self.speed.value

        perf = self.perf.value

        rated = self.rated

        has_moved = self.has_moved

        opponent = self.opponent.to_dict()

        is_my_turn = self.is_my_turn

        seconds_left = self.seconds_left

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        tournament_id = self.tournament_id

        swiss_id = self.swiss_id

        winner: Union[Unset, str] = UNSET
        if not isinstance(self.winner, Unset):
            winner = self.winner.value


        rating_diff = self.rating_diff


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fullId": full_id,
            "gameId": game_id,
            "fen": fen,
            "color": color,
            "lastMove": last_move,
            "source": source,
            "variant": variant,
            "speed": speed,
            "perf": perf,
            "rated": rated,
            "hasMoved": has_moved,
            "opponent": opponent,
            "isMyTurn": is_my_turn,
            "secondsLeft": seconds_left,
        })
        if status is not UNSET:
            field_dict["status"] = status
        if tournament_id is not UNSET:
            field_dict["tournamentId"] = tournament_id
        if swiss_id is not UNSET:
            field_dict["swissId"] = swiss_id
        if winner is not UNSET:
            field_dict["winner"] = winner
        if rating_diff is not UNSET:
            field_dict["ratingDiff"] = rating_diff

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_account_playing_response_200_now_playing_item_opponent import ApiAccountPlayingResponse200NowPlayingItemOpponent
        from ..models.api_account_playing_response_200_now_playing_item_variant import ApiAccountPlayingResponse200NowPlayingItemVariant
        d = dict(src_dict)
        full_id = d.pop("fullId")

        game_id = d.pop("gameId")

        fen = d.pop("fen")

        color = ApiAccountPlayingResponse200NowPlayingItemColor(d.pop("color"))




        last_move = d.pop("lastMove")

        source = ApiAccountPlayingResponse200NowPlayingItemSource(d.pop("source"))




        variant = ApiAccountPlayingResponse200NowPlayingItemVariant.from_dict(d.pop("variant"))




        speed = ApiAccountPlayingResponse200NowPlayingItemSpeed(d.pop("speed"))




        perf = ApiAccountPlayingResponse200NowPlayingItemPerf(d.pop("perf"))




        rated = d.pop("rated")

        has_moved = d.pop("hasMoved")

        opponent = ApiAccountPlayingResponse200NowPlayingItemOpponent.from_dict(d.pop("opponent"))




        is_my_turn = d.pop("isMyTurn")

        seconds_left = d.pop("secondsLeft")

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApiAccountPlayingResponse200NowPlayingItemStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ApiAccountPlayingResponse200NowPlayingItemStatus(_status)




        tournament_id = d.pop("tournamentId", UNSET)

        swiss_id = d.pop("swissId", UNSET)

        _winner = d.pop("winner", UNSET)
        winner: Union[Unset, ApiAccountPlayingResponse200NowPlayingItemWinner]
        if isinstance(_winner,  Unset):
            winner = UNSET
        else:
            winner = ApiAccountPlayingResponse200NowPlayingItemWinner(_winner)




        rating_diff = d.pop("ratingDiff", UNSET)

        api_account_playing_response_200_now_playing_item = cls(
            full_id=full_id,
            game_id=game_id,
            fen=fen,
            color=color,
            last_move=last_move,
            source=source,
            variant=variant,
            speed=speed,
            perf=perf,
            rated=rated,
            has_moved=has_moved,
            opponent=opponent,
            is_my_turn=is_my_turn,
            seconds_left=seconds_left,
            status=status,
            tournament_id=tournament_id,
            swiss_id=swiss_id,
            winner=winner,
            rating_diff=rating_diff,
        )


        api_account_playing_response_200_now_playing_item.additional_properties = d
        return api_account_playing_response_200_now_playing_item

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
