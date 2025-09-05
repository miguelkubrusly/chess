from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.teams_by_tournament_response_200_teams_item_players_item import TeamsByTournamentResponse200TeamsItemPlayersItem





T = TypeVar("T", bound="TeamsByTournamentResponse200TeamsItem")



@_attrs_define
class TeamsByTournamentResponse200TeamsItem:
    """ 
        Attributes:
            rank (float):
            id (str):
            score (float):
            players (list['TeamsByTournamentResponse200TeamsItemPlayersItem']):
     """

    rank: float
    id: str
    score: float
    players: list['TeamsByTournamentResponse200TeamsItemPlayersItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.teams_by_tournament_response_200_teams_item_players_item import TeamsByTournamentResponse200TeamsItemPlayersItem
        rank = self.rank

        id = self.id

        score = self.score

        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rank": rank,
            "id": id,
            "score": score,
            "players": players,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teams_by_tournament_response_200_teams_item_players_item import TeamsByTournamentResponse200TeamsItemPlayersItem
        d = dict(src_dict)
        rank = d.pop("rank")

        id = d.pop("id")

        score = d.pop("score")

        players = []
        _players = d.pop("players")
        for players_item_data in (_players):
            players_item = TeamsByTournamentResponse200TeamsItemPlayersItem.from_dict(players_item_data)



            players.append(players_item)


        teams_by_tournament_response_200_teams_item = cls(
            rank=rank,
            id=id,
            score=score,
            players=players,
        )


        teams_by_tournament_response_200_teams_item.additional_properties = d
        return teams_by_tournament_response_200_teams_item

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
