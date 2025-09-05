from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.teams_by_tournament_response_200_teams_item_players_item_user import TeamsByTournamentResponse200TeamsItemPlayersItemUser





T = TypeVar("T", bound="TeamsByTournamentResponse200TeamsItemPlayersItem")



@_attrs_define
class TeamsByTournamentResponse200TeamsItemPlayersItem:
    """ 
        Attributes:
            user (TeamsByTournamentResponse200TeamsItemPlayersItemUser):
            score (Union[Unset, float]):
     """

    user: 'TeamsByTournamentResponse200TeamsItemPlayersItemUser'
    score: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.teams_by_tournament_response_200_teams_item_players_item_user import TeamsByTournamentResponse200TeamsItemPlayersItemUser
        user = self.user.to_dict()

        score = self.score


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user": user,
        })
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teams_by_tournament_response_200_teams_item_players_item_user import TeamsByTournamentResponse200TeamsItemPlayersItemUser
        d = dict(src_dict)
        user = TeamsByTournamentResponse200TeamsItemPlayersItemUser.from_dict(d.pop("user"))




        score = d.pop("score", UNSET)

        teams_by_tournament_response_200_teams_item_players_item = cls(
            user=user,
            score=score,
        )


        teams_by_tournament_response_200_teams_item_players_item.additional_properties = d
        return teams_by_tournament_response_200_teams_item_players_item

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
