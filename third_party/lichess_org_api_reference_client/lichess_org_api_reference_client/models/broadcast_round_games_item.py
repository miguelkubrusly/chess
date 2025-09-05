from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.broadcast_round_games_item_check import BroadcastRoundGamesItemCheck
from ..models.broadcast_round_games_item_status import BroadcastRoundGamesItemStatus
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_round_games_item_players_item import BroadcastRoundGamesItemPlayersItem





T = TypeVar("T", bound="BroadcastRoundGamesItem")



@_attrs_define
class BroadcastRoundGamesItem:
    """ 
        Attributes:
            id (str):
            name (str):
            fen (Union[Unset, str]):
            players (Union[Unset, list['BroadcastRoundGamesItemPlayersItem']]):
            last_move (Union[Unset, str]):
            check (Union[Unset, BroadcastRoundGamesItemCheck]):
            think_time (Union[Unset, int]):
            status (Union[Unset, BroadcastRoundGamesItemStatus]): The result of the game
     """

    id: str
    name: str
    fen: Union[Unset, str] = UNSET
    players: Union[Unset, list['BroadcastRoundGamesItemPlayersItem']] = UNSET
    last_move: Union[Unset, str] = UNSET
    check: Union[Unset, BroadcastRoundGamesItemCheck] = UNSET
    think_time: Union[Unset, int] = UNSET
    status: Union[Unset, BroadcastRoundGamesItemStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_round_games_item_players_item import BroadcastRoundGamesItemPlayersItem
        id = self.id

        name = self.name

        fen = self.fen

        players: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)



        last_move = self.last_move

        check: Union[Unset, str] = UNSET
        if not isinstance(self.check, Unset):
            check = self.check.value


        think_time = self.think_time

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })
        if fen is not UNSET:
            field_dict["fen"] = fen
        if players is not UNSET:
            field_dict["players"] = players
        if last_move is not UNSET:
            field_dict["lastMove"] = last_move
        if check is not UNSET:
            field_dict["check"] = check
        if think_time is not UNSET:
            field_dict["thinkTime"] = think_time
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_round_games_item_players_item import BroadcastRoundGamesItemPlayersItem
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        fen = d.pop("fen", UNSET)

        players = []
        _players = d.pop("players", UNSET)
        for players_item_data in (_players or []):
            players_item = BroadcastRoundGamesItemPlayersItem.from_dict(players_item_data)



            players.append(players_item)


        last_move = d.pop("lastMove", UNSET)

        _check = d.pop("check", UNSET)
        check: Union[Unset, BroadcastRoundGamesItemCheck]
        if isinstance(_check,  Unset):
            check = UNSET
        else:
            check = BroadcastRoundGamesItemCheck(_check)




        think_time = d.pop("thinkTime", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BroadcastRoundGamesItemStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BroadcastRoundGamesItemStatus(_status)




        broadcast_round_games_item = cls(
            id=id,
            name=name,
            fen=fen,
            players=players,
            last_move=last_move,
            check=check,
            think_time=think_time,
            status=status,
        )


        broadcast_round_games_item.additional_properties = d
        return broadcast_round_games_item

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
