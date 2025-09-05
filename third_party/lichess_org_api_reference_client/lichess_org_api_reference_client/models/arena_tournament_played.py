from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.arena_tournament_played_player import ArenaTournamentPlayedPlayer
  from ..models.arena_tournament_played_tournament import ArenaTournamentPlayedTournament





T = TypeVar("T", bound="ArenaTournamentPlayed")



@_attrs_define
class ArenaTournamentPlayed:
    """ 
        Attributes:
            tournament (Union[Unset, ArenaTournamentPlayedTournament]):
            player (Union[Unset, ArenaTournamentPlayedPlayer]):  Example: {'games': 10, 'score': 14, 'rank': 30,
                'performance': 1935}.
     """

    tournament: Union[Unset, 'ArenaTournamentPlayedTournament'] = UNSET
    player: Union[Unset, 'ArenaTournamentPlayedPlayer'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.arena_tournament_played_player import ArenaTournamentPlayedPlayer
        from ..models.arena_tournament_played_tournament import ArenaTournamentPlayedTournament
        tournament: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tournament, Unset):
            tournament = self.tournament.to_dict()

        player: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.player, Unset):
            player = self.player.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tournament is not UNSET:
            field_dict["tournament"] = tournament
        if player is not UNSET:
            field_dict["player"] = player

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.arena_tournament_played_player import ArenaTournamentPlayedPlayer
        from ..models.arena_tournament_played_tournament import ArenaTournamentPlayedTournament
        d = dict(src_dict)
        _tournament = d.pop("tournament", UNSET)
        tournament: Union[Unset, ArenaTournamentPlayedTournament]
        if isinstance(_tournament,  Unset):
            tournament = UNSET
        else:
            tournament = ArenaTournamentPlayedTournament.from_dict(_tournament)




        _player = d.pop("player", UNSET)
        player: Union[Unset, ArenaTournamentPlayedPlayer]
        if isinstance(_player,  Unset):
            player = UNSET
        else:
            player = ArenaTournamentPlayedPlayer.from_dict(_player)




        arena_tournament_played = cls(
            tournament=tournament,
            player=player,
        )


        arena_tournament_played.additional_properties = d
        return arena_tournament_played

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
