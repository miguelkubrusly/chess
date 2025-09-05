from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.game_full_event_state_status import GameFullEventStateStatus
from ..models.game_full_event_state_winner import GameFullEventStateWinner
from ..types import UNSET, Unset
from typing import Literal, cast
from typing import Union






T = TypeVar("T", bound="GameFullEventState")



@_attrs_define
class GameFullEventState:
    """ 
        Example:
            {'type': 'gameState', 'moves': 'e2e4 c7c5 f2f4 d7d6 g1f3 b8c6 f1c4 g8f6 d2d3 g7g6 e1g1 f8g7 b1c3', 'wtime':
                7598040, 'btime': 8395220, 'winc': 10000, 'binc': 10000, 'wdraw': False, 'bdraw': False, 'wtakeback': False,
                'btakeback': False, 'status': 'started'}

        Attributes:
            type_ (Literal['gameState']):
            moves (str): Current moves in UCI format
            wtime (int): Integer of milliseconds White has left on the clock
            btime (int): Integer of milliseconds Black has left on the clock
            winc (int): Integer of White Fisher increment.
            binc (int): Integer of Black Fisher increment.
            status (GameFullEventStateStatus):
            winner (Union[Unset, GameFullEventStateWinner]): Color of the winner, if any
            wdraw (Union[Unset, bool]): true if white is offering draw, else omitted
            bdraw (Union[Unset, bool]): true if black is offering draw, else omitted
            wtakeback (Union[Unset, bool]): true if white is proposing takeback, else omitted
            btakeback (Union[Unset, bool]): true if black is proposing takeback, else omitted
     """

    type_: Literal['gameState']
    moves: str
    wtime: int
    btime: int
    winc: int
    binc: int
    status: GameFullEventStateStatus
    winner: Union[Unset, GameFullEventStateWinner] = UNSET
    wdraw: Union[Unset, bool] = UNSET
    bdraw: Union[Unset, bool] = UNSET
    wtakeback: Union[Unset, bool] = UNSET
    btakeback: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        moves = self.moves

        wtime = self.wtime

        btime = self.btime

        winc = self.winc

        binc = self.binc

        status = self.status.value

        winner: Union[Unset, str] = UNSET
        if not isinstance(self.winner, Unset):
            winner = self.winner.value


        wdraw = self.wdraw

        bdraw = self.bdraw

        wtakeback = self.wtakeback

        btakeback = self.btakeback


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "moves": moves,
            "wtime": wtime,
            "btime": btime,
            "winc": winc,
            "binc": binc,
            "status": status,
        })
        if winner is not UNSET:
            field_dict["winner"] = winner
        if wdraw is not UNSET:
            field_dict["wdraw"] = wdraw
        if bdraw is not UNSET:
            field_dict["bdraw"] = bdraw
        if wtakeback is not UNSET:
            field_dict["wtakeback"] = wtakeback
        if btakeback is not UNSET:
            field_dict["btakeback"] = btakeback

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['gameState'] , d.pop("type"))
        if type_ != 'gameState':
            raise ValueError(f"type must match const 'gameState', got '{type_}'")

        moves = d.pop("moves")

        wtime = d.pop("wtime")

        btime = d.pop("btime")

        winc = d.pop("winc")

        binc = d.pop("binc")

        status = GameFullEventStateStatus(d.pop("status"))




        _winner = d.pop("winner", UNSET)
        winner: Union[Unset, GameFullEventStateWinner]
        if isinstance(_winner,  Unset):
            winner = UNSET
        else:
            winner = GameFullEventStateWinner(_winner)




        wdraw = d.pop("wdraw", UNSET)

        bdraw = d.pop("bdraw", UNSET)

        wtakeback = d.pop("wtakeback", UNSET)

        btakeback = d.pop("btakeback", UNSET)

        game_full_event_state = cls(
            type_=type_,
            moves=moves,
            wtime=wtime,
            btime=btime,
            winc=winc,
            binc=binc,
            status=status,
            winner=winner,
            wdraw=wdraw,
            bdraw=bdraw,
            wtakeback=wtakeback,
            btakeback=btakeback,
        )


        game_full_event_state.additional_properties = d
        return game_full_event_state

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
