from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiTournamentJoinBody")



@_attrs_define
class ApiTournamentJoinBody:
    """ 
        Attributes:
            password (Union[Unset, str]): The tournament password, if one is required.
                Can also be a [user-specific entry code](https://github.com/lichess-org/api/tree/master/example/tournament-
                entry-code)
                generated and shared by the organizer.
            team (Union[Unset, str]): The team to join the tournament with, for team battle tournaments
            pair_me_asap (Union[Unset, bool]): If the tournament is started, attempt to pair the user,
                even if they are not connected to the tournament page.
                This expires after one minute, to avoid pairing a user who is long gone.
                You may call "join" again to extend the waiting.
                 Default: False.
     """

    password: Union[Unset, str] = UNSET
    team: Union[Unset, str] = UNSET
    pair_me_asap: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        password = self.password

        team = self.team

        pair_me_asap = self.pair_me_asap


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if password is not UNSET:
            field_dict["password"] = password
        if team is not UNSET:
            field_dict["team"] = team
        if pair_me_asap is not UNSET:
            field_dict["pairMeAsap"] = pair_me_asap

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        team = d.pop("team", UNSET)

        pair_me_asap = d.pop("pairMeAsap", UNSET)

        api_tournament_join_body = cls(
            password=password,
            team=team,
            pair_me_asap=pair_me_asap,
        )


        api_tournament_join_body.additional_properties = d
        return api_tournament_join_body

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
