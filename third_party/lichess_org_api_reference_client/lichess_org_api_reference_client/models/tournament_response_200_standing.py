from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.tournament_response_200_standing_players_item import TournamentResponse200StandingPlayersItem





T = TypeVar("T", bound="TournamentResponse200Standing")



@_attrs_define
class TournamentResponse200Standing:
    """ 
        Attributes:
            page (Union[Unset, float]):
            players (Union[Unset, list['TournamentResponse200StandingPlayersItem']]):
     """

    page: Union[Unset, float] = UNSET
    players: Union[Unset, list['TournamentResponse200StandingPlayersItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tournament_response_200_standing_players_item import TournamentResponse200StandingPlayersItem
        page = self.page

        players: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if page is not UNSET:
            field_dict["page"] = page
        if players is not UNSET:
            field_dict["players"] = players

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tournament_response_200_standing_players_item import TournamentResponse200StandingPlayersItem
        d = dict(src_dict)
        page = d.pop("page", UNSET)

        players = []
        _players = d.pop("players", UNSET)
        for players_item_data in (_players or []):
            players_item = TournamentResponse200StandingPlayersItem.from_dict(players_item_data)



            players.append(players_item)


        tournament_response_200_standing = cls(
            page=page,
            players=players,
        )


        tournament_response_200_standing.additional_properties = d
        return tournament_response_200_standing

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
