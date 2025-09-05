from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="ArenaTournamentsFinishedItemTeamBattle")



@_attrs_define
class ArenaTournamentsFinishedItemTeamBattle:
    """ 
        Attributes:
            teams (Union[Unset, list[str]]):
            nb_leaders (Union[Unset, int]):
     """

    teams: Union[Unset, list[str]] = UNSET
    nb_leaders: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        teams: Union[Unset, list[str]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams



        nb_leaders = self.nb_leaders


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if teams is not UNSET:
            field_dict["teams"] = teams
        if nb_leaders is not UNSET:
            field_dict["nbLeaders"] = nb_leaders

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        teams = cast(list[str], d.pop("teams", UNSET))


        nb_leaders = d.pop("nbLeaders", UNSET)

        arena_tournaments_finished_item_team_battle = cls(
            teams=teams,
            nb_leaders=nb_leaders,
        )


        arena_tournaments_finished_item_team_battle.additional_properties = d
        return arena_tournaments_finished_item_team_battle

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
