from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.teams_by_tournament_response_200_teams_item import TeamsByTournamentResponse200TeamsItem





T = TypeVar("T", bound="TeamsByTournamentResponse200")



@_attrs_define
class TeamsByTournamentResponse200:
    """ 
        Attributes:
            id (str):
            teams (list['TeamsByTournamentResponse200TeamsItem']):
     """

    id: str
    teams: list['TeamsByTournamentResponse200TeamsItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.teams_by_tournament_response_200_teams_item import TeamsByTournamentResponse200TeamsItem
        id = self.id

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "teams": teams,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teams_by_tournament_response_200_teams_item import TeamsByTournamentResponse200TeamsItem
        d = dict(src_dict)
        id = d.pop("id")

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in (_teams):
            teams_item = TeamsByTournamentResponse200TeamsItem.from_dict(teams_item_data)



            teams.append(teams_item)


        teams_by_tournament_response_200 = cls(
            id=id,
            teams=teams,
        )


        teams_by_tournament_response_200.additional_properties = d
        return teams_by_tournament_response_200

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
