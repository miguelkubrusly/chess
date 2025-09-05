from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.swiss_tournament_status import SwissTournamentStatus
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.swiss_tournament_next_round import SwissTournamentNextRound
  from ..models.swiss_tournament_stats import SwissTournamentStats
  from ..models.swiss_tournament_clock import SwissTournamentClock
  from ..models.swiss_tournament_verdicts import SwissTournamentVerdicts





T = TypeVar("T", bound="SwissTournament")



@_attrs_define
class SwissTournament:
    """ 
        Attributes:
            id (str):
            created_by (str):
            starts_at (str):
            name (str):
            clock (SwissTournamentClock):
            variant (str):
            round_ (float):
            nb_rounds (float):
            nb_players (float):
            nb_ongoing (float):
            status (SwissTournamentStatus): The current state of the swiss tournament
            rated (bool):
            verdicts (SwissTournamentVerdicts):
            stats (Union[Unset, SwissTournamentStats]):
            next_round (Union[Unset, SwissTournamentNextRound]):
     """

    id: str
    created_by: str
    starts_at: str
    name: str
    clock: 'SwissTournamentClock'
    variant: str
    round_: float
    nb_rounds: float
    nb_players: float
    nb_ongoing: float
    status: SwissTournamentStatus
    rated: bool
    verdicts: 'SwissTournamentVerdicts'
    stats: Union[Unset, 'SwissTournamentStats'] = UNSET
    next_round: Union[Unset, 'SwissTournamentNextRound'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.swiss_tournament_next_round import SwissTournamentNextRound
        from ..models.swiss_tournament_stats import SwissTournamentStats
        from ..models.swiss_tournament_clock import SwissTournamentClock
        from ..models.swiss_tournament_verdicts import SwissTournamentVerdicts
        id = self.id

        created_by = self.created_by

        starts_at = self.starts_at

        name = self.name

        clock = self.clock.to_dict()

        variant = self.variant

        round_ = self.round_

        nb_rounds = self.nb_rounds

        nb_players = self.nb_players

        nb_ongoing = self.nb_ongoing

        status = self.status.value

        rated = self.rated

        verdicts = self.verdicts.to_dict()

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        next_round: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_round, Unset):
            next_round = self.next_round.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "createdBy": created_by,
            "startsAt": starts_at,
            "name": name,
            "clock": clock,
            "variant": variant,
            "round": round_,
            "nbRounds": nb_rounds,
            "nbPlayers": nb_players,
            "nbOngoing": nb_ongoing,
            "status": status,
            "rated": rated,
            "verdicts": verdicts,
        })
        if stats is not UNSET:
            field_dict["stats"] = stats
        if next_round is not UNSET:
            field_dict["nextRound"] = next_round

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.swiss_tournament_next_round import SwissTournamentNextRound
        from ..models.swiss_tournament_stats import SwissTournamentStats
        from ..models.swiss_tournament_clock import SwissTournamentClock
        from ..models.swiss_tournament_verdicts import SwissTournamentVerdicts
        d = dict(src_dict)
        id = d.pop("id")

        created_by = d.pop("createdBy")

        starts_at = d.pop("startsAt")

        name = d.pop("name")

        clock = SwissTournamentClock.from_dict(d.pop("clock"))




        variant = d.pop("variant")

        round_ = d.pop("round")

        nb_rounds = d.pop("nbRounds")

        nb_players = d.pop("nbPlayers")

        nb_ongoing = d.pop("nbOngoing")

        status = SwissTournamentStatus(d.pop("status"))




        rated = d.pop("rated")

        verdicts = SwissTournamentVerdicts.from_dict(d.pop("verdicts"))




        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, SwissTournamentStats]
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = SwissTournamentStats.from_dict(_stats)




        _next_round = d.pop("nextRound", UNSET)
        next_round: Union[Unset, SwissTournamentNextRound]
        if isinstance(_next_round,  Unset):
            next_round = UNSET
        else:
            next_round = SwissTournamentNextRound.from_dict(_next_round)




        swiss_tournament = cls(
            id=id,
            created_by=created_by,
            starts_at=starts_at,
            name=name,
            clock=clock,
            variant=variant,
            round_=round_,
            nb_rounds=nb_rounds,
            nb_players=nb_players,
            nb_ongoing=nb_ongoing,
            status=status,
            rated=rated,
            verdicts=verdicts,
            stats=stats,
            next_round=next_round,
        )


        swiss_tournament.additional_properties = d
        return swiss_tournament

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
