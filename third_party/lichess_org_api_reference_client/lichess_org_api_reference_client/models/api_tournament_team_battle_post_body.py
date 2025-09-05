from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ApiTournamentTeamBattlePostBody")



@_attrs_define
class ApiTournamentTeamBattlePostBody:
    """ 
        Attributes:
            teams (str): All team IDs of the team battle, separated by commas.
                Make sure to always send the full list.
                Teams that are not in the list will be removed from the team battle.
                Example: `coders,zhigalko_sergei-fan-club,hhSwTKZv`
            nb_leaders (int): Number team leaders per team.
     """

    teams: str
    nb_leaders: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        teams = self.teams

        nb_leaders = self.nb_leaders


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "teams": teams,
            "nbLeaders": nb_leaders,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        teams = d.pop("teams")

        nb_leaders = d.pop("nbLeaders")

        api_tournament_team_battle_post_body = cls(
            teams=teams,
            nb_leaders=nb_leaders,
        )


        api_tournament_team_battle_post_body.additional_properties = d
        return api_tournament_team_battle_post_body

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
