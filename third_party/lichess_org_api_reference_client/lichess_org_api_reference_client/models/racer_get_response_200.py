from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.racer_get_response_200_players_item import RacerGetResponse200PlayersItem
  from ..models.racer_get_response_200_puzzles_item import RacerGetResponse200PuzzlesItem





T = TypeVar("T", bound="RacerGetResponse200")



@_attrs_define
class RacerGetResponse200:
    """ 
        Attributes:
            id (str): Unique identifier of the puzzle race
            owner (str): Owner of the puzzle race
            players (list['RacerGetResponse200PlayersItem']): List of players participating in the race
            puzzles (list['RacerGetResponse200PuzzlesItem']): List of puzzles in the race
            finishes_at (int): Timestamp in milliseconds when the race finishes
            starts_at (int): Timestamp in milliseconds when the race started
     """

    id: str
    owner: str
    players: list['RacerGetResponse200PlayersItem']
    puzzles: list['RacerGetResponse200PuzzlesItem']
    finishes_at: int
    starts_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.racer_get_response_200_players_item import RacerGetResponse200PlayersItem
        from ..models.racer_get_response_200_puzzles_item import RacerGetResponse200PuzzlesItem
        id = self.id

        owner = self.owner

        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)



        puzzles = []
        for puzzles_item_data in self.puzzles:
            puzzles_item = puzzles_item_data.to_dict()
            puzzles.append(puzzles_item)



        finishes_at = self.finishes_at

        starts_at = self.starts_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "owner": owner,
            "players": players,
            "puzzles": puzzles,
            "finishesAt": finishes_at,
            "startsAt": starts_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.racer_get_response_200_players_item import RacerGetResponse200PlayersItem
        from ..models.racer_get_response_200_puzzles_item import RacerGetResponse200PuzzlesItem
        d = dict(src_dict)
        id = d.pop("id")

        owner = d.pop("owner")

        players = []
        _players = d.pop("players")
        for players_item_data in (_players):
            players_item = RacerGetResponse200PlayersItem.from_dict(players_item_data)



            players.append(players_item)


        puzzles = []
        _puzzles = d.pop("puzzles")
        for puzzles_item_data in (_puzzles):
            puzzles_item = RacerGetResponse200PuzzlesItem.from_dict(puzzles_item_data)



            puzzles.append(puzzles_item)


        finishes_at = d.pop("finishesAt")

        starts_at = d.pop("startsAt")

        racer_get_response_200 = cls(
            id=id,
            owner=owner,
            players=players,
            puzzles=puzzles,
            finishes_at=finishes_at,
            starts_at=starts_at,
        )


        racer_get_response_200.additional_properties = d
        return racer_get_response_200

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
