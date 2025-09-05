from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.swiss_response_200_status import SwissResponse200Status
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.swiss_response_200_next_round import SwissResponse200NextRound
  from ..models.swiss_response_200_stats import SwissResponse200Stats
  from ..models.swiss_response_200_clock import SwissResponse200Clock
  from ..models.swiss_response_200_verdicts import SwissResponse200Verdicts





T = TypeVar("T", bound="SwissResponse200")



@_attrs_define
class SwissResponse200:
    """ 
        Attributes:
            id (str):
            created_by (str):
            starts_at (str):
            name (str):
            clock (SwissResponse200Clock):
            variant (str):
            round_ (float):
            nb_rounds (float):
            nb_players (float):
            nb_ongoing (float):
            status (SwissResponse200Status): The current state of the swiss tournament
            rated (bool):
            verdicts (SwissResponse200Verdicts):
            stats (Union[Unset, SwissResponse200Stats]):
            next_round (Union[Unset, SwissResponse200NextRound]):
     """

    id: str
    created_by: str
    starts_at: str
    name: str
    clock: 'SwissResponse200Clock'
    variant: str
    round_: float
    nb_rounds: float
    nb_players: float
    nb_ongoing: float
    status: SwissResponse200Status
    rated: bool
    verdicts: 'SwissResponse200Verdicts'
    stats: Union[Unset, 'SwissResponse200Stats'] = UNSET
    next_round: Union[Unset, 'SwissResponse200NextRound'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.swiss_response_200_next_round import SwissResponse200NextRound
        from ..models.swiss_response_200_stats import SwissResponse200Stats
        from ..models.swiss_response_200_clock import SwissResponse200Clock
        from ..models.swiss_response_200_verdicts import SwissResponse200Verdicts
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
        from ..models.swiss_response_200_next_round import SwissResponse200NextRound
        from ..models.swiss_response_200_stats import SwissResponse200Stats
        from ..models.swiss_response_200_clock import SwissResponse200Clock
        from ..models.swiss_response_200_verdicts import SwissResponse200Verdicts
        d = dict(src_dict)
        id = d.pop("id")

        created_by = d.pop("createdBy")

        starts_at = d.pop("startsAt")

        name = d.pop("name")

        clock = SwissResponse200Clock.from_dict(d.pop("clock"))




        variant = d.pop("variant")

        round_ = d.pop("round")

        nb_rounds = d.pop("nbRounds")

        nb_players = d.pop("nbPlayers")

        nb_ongoing = d.pop("nbOngoing")

        status = SwissResponse200Status(d.pop("status"))




        rated = d.pop("rated")

        verdicts = SwissResponse200Verdicts.from_dict(d.pop("verdicts"))




        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, SwissResponse200Stats]
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = SwissResponse200Stats.from_dict(_stats)




        _next_round = d.pop("nextRound", UNSET)
        next_round: Union[Unset, SwissResponse200NextRound]
        if isinstance(_next_round,  Unset):
            next_round = UNSET
        else:
            next_round = SwissResponse200NextRound.from_dict(_next_round)




        swiss_response_200 = cls(
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


        swiss_response_200.additional_properties = d
        return swiss_response_200

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
