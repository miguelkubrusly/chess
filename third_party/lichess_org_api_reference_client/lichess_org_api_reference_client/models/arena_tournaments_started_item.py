from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.arena_tournaments_started_item_status import ArenaTournamentsStartedItemStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Literal, cast
from typing import Union

if TYPE_CHECKING:
  from ..models.arena_tournaments_started_item_thematic import ArenaTournamentsStartedItemThematic
  from ..models.arena_tournaments_started_item_schedule import ArenaTournamentsStartedItemSchedule
  from ..models.arena_tournaments_started_item_perf import ArenaTournamentsStartedItemPerf
  from ..models.arena_tournaments_started_item_team_battle import ArenaTournamentsStartedItemTeamBattle
  from ..models.arena_tournaments_started_item_winner import ArenaTournamentsStartedItemWinner
  from ..models.arena_tournaments_started_item_min_rating import ArenaTournamentsStartedItemMinRating
  from ..models.arena_tournaments_started_item_clock import ArenaTournamentsStartedItemClock
  from ..models.arena_tournaments_started_item_min_rated_games import ArenaTournamentsStartedItemMinRatedGames
  from ..models.arena_tournaments_started_item_variant import ArenaTournamentsStartedItemVariant
  from ..models.arena_tournaments_started_item_max_rating import ArenaTournamentsStartedItemMaxRating
  from ..models.arena_tournaments_started_item_custom_position import ArenaTournamentsStartedItemCustomPosition





T = TypeVar("T", bound="ArenaTournamentsStartedItem")



@_attrs_define
class ArenaTournamentsStartedItem:
    """ 
        Attributes:
            id (str):
            created_by (str):
            system (Literal['arena']):
            minutes (int):
            clock (ArenaTournamentsStartedItemClock):
            rated (bool):
            full_name (str):
            nb_players (int):
            variant (ArenaTournamentsStartedItemVariant):
            starts_at (int):
            finishes_at (int):
            status (ArenaTournamentsStartedItemStatus): 10: created, 20: started, 30: finished
            perf (ArenaTournamentsStartedItemPerf):
            seconds_to_start (Union[Unset, int]):
            has_max_rating (Union[Unset, bool]):
            max_rating (Union[Unset, ArenaTournamentsStartedItemMaxRating]):
            min_rating (Union[Unset, ArenaTournamentsStartedItemMinRating]):
            min_rated_games (Union[Unset, ArenaTournamentsStartedItemMinRatedGames]):
            bots_allowed (Union[Unset, bool]):
            min_account_age_in_days (Union[Unset, int]):
            only_titled (Union[Unset, bool]):
            team_member (Union[Unset, str]):
            private (Union[Unset, bool]):
            position (Union['ArenaTournamentsStartedItemCustomPosition', 'ArenaTournamentsStartedItemThematic', Unset]):
            schedule (Union[Unset, ArenaTournamentsStartedItemSchedule]):
            team_battle (Union[Unset, ArenaTournamentsStartedItemTeamBattle]):
            winner (Union[Unset, ArenaTournamentsStartedItemWinner]):
     """

    id: str
    created_by: str
    system: Literal['arena']
    minutes: int
    clock: 'ArenaTournamentsStartedItemClock'
    rated: bool
    full_name: str
    nb_players: int
    variant: 'ArenaTournamentsStartedItemVariant'
    starts_at: int
    finishes_at: int
    status: ArenaTournamentsStartedItemStatus
    perf: 'ArenaTournamentsStartedItemPerf'
    seconds_to_start: Union[Unset, int] = UNSET
    has_max_rating: Union[Unset, bool] = UNSET
    max_rating: Union[Unset, 'ArenaTournamentsStartedItemMaxRating'] = UNSET
    min_rating: Union[Unset, 'ArenaTournamentsStartedItemMinRating'] = UNSET
    min_rated_games: Union[Unset, 'ArenaTournamentsStartedItemMinRatedGames'] = UNSET
    bots_allowed: Union[Unset, bool] = UNSET
    min_account_age_in_days: Union[Unset, int] = UNSET
    only_titled: Union[Unset, bool] = UNSET
    team_member: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = UNSET
    position: Union['ArenaTournamentsStartedItemCustomPosition', 'ArenaTournamentsStartedItemThematic', Unset] = UNSET
    schedule: Union[Unset, 'ArenaTournamentsStartedItemSchedule'] = UNSET
    team_battle: Union[Unset, 'ArenaTournamentsStartedItemTeamBattle'] = UNSET
    winner: Union[Unset, 'ArenaTournamentsStartedItemWinner'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.arena_tournaments_started_item_thematic import ArenaTournamentsStartedItemThematic
        from ..models.arena_tournaments_started_item_schedule import ArenaTournamentsStartedItemSchedule
        from ..models.arena_tournaments_started_item_perf import ArenaTournamentsStartedItemPerf
        from ..models.arena_tournaments_started_item_team_battle import ArenaTournamentsStartedItemTeamBattle
        from ..models.arena_tournaments_started_item_winner import ArenaTournamentsStartedItemWinner
        from ..models.arena_tournaments_started_item_min_rating import ArenaTournamentsStartedItemMinRating
        from ..models.arena_tournaments_started_item_clock import ArenaTournamentsStartedItemClock
        from ..models.arena_tournaments_started_item_min_rated_games import ArenaTournamentsStartedItemMinRatedGames
        from ..models.arena_tournaments_started_item_variant import ArenaTournamentsStartedItemVariant
        from ..models.arena_tournaments_started_item_max_rating import ArenaTournamentsStartedItemMaxRating
        from ..models.arena_tournaments_started_item_custom_position import ArenaTournamentsStartedItemCustomPosition
        id = self.id

        created_by = self.created_by

        system = self.system

        minutes = self.minutes

        clock = self.clock.to_dict()

        rated = self.rated

        full_name = self.full_name

        nb_players = self.nb_players

        variant = self.variant.to_dict()

        starts_at = self.starts_at

        finishes_at = self.finishes_at

        status = self.status.value

        perf = self.perf.to_dict()

        seconds_to_start = self.seconds_to_start

        has_max_rating = self.has_max_rating

        max_rating: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.max_rating, Unset):
            max_rating = self.max_rating.to_dict()

        min_rating: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.min_rating, Unset):
            min_rating = self.min_rating.to_dict()

        min_rated_games: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.min_rated_games, Unset):
            min_rated_games = self.min_rated_games.to_dict()

        bots_allowed = self.bots_allowed

        min_account_age_in_days = self.min_account_age_in_days

        only_titled = self.only_titled

        team_member = self.team_member

        private = self.private

        position: Union[Unset, dict[str, Any]]
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, ArenaTournamentsStartedItemThematic):
            position = self.position.to_dict()
        else:
            position = self.position.to_dict()


        schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        team_battle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.team_battle, Unset):
            team_battle = self.team_battle.to_dict()

        winner: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.winner, Unset):
            winner = self.winner.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "createdBy": created_by,
            "system": system,
            "minutes": minutes,
            "clock": clock,
            "rated": rated,
            "fullName": full_name,
            "nbPlayers": nb_players,
            "variant": variant,
            "startsAt": starts_at,
            "finishesAt": finishes_at,
            "status": status,
            "perf": perf,
        })
        if seconds_to_start is not UNSET:
            field_dict["secondsToStart"] = seconds_to_start
        if has_max_rating is not UNSET:
            field_dict["hasMaxRating"] = has_max_rating
        if max_rating is not UNSET:
            field_dict["maxRating"] = max_rating
        if min_rating is not UNSET:
            field_dict["minRating"] = min_rating
        if min_rated_games is not UNSET:
            field_dict["minRatedGames"] = min_rated_games
        if bots_allowed is not UNSET:
            field_dict["botsAllowed"] = bots_allowed
        if min_account_age_in_days is not UNSET:
            field_dict["minAccountAgeInDays"] = min_account_age_in_days
        if only_titled is not UNSET:
            field_dict["onlyTitled"] = only_titled
        if team_member is not UNSET:
            field_dict["teamMember"] = team_member
        if private is not UNSET:
            field_dict["private"] = private
        if position is not UNSET:
            field_dict["position"] = position
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if team_battle is not UNSET:
            field_dict["teamBattle"] = team_battle
        if winner is not UNSET:
            field_dict["winner"] = winner

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.arena_tournaments_started_item_thematic import ArenaTournamentsStartedItemThematic
        from ..models.arena_tournaments_started_item_schedule import ArenaTournamentsStartedItemSchedule
        from ..models.arena_tournaments_started_item_perf import ArenaTournamentsStartedItemPerf
        from ..models.arena_tournaments_started_item_team_battle import ArenaTournamentsStartedItemTeamBattle
        from ..models.arena_tournaments_started_item_winner import ArenaTournamentsStartedItemWinner
        from ..models.arena_tournaments_started_item_min_rating import ArenaTournamentsStartedItemMinRating
        from ..models.arena_tournaments_started_item_clock import ArenaTournamentsStartedItemClock
        from ..models.arena_tournaments_started_item_min_rated_games import ArenaTournamentsStartedItemMinRatedGames
        from ..models.arena_tournaments_started_item_variant import ArenaTournamentsStartedItemVariant
        from ..models.arena_tournaments_started_item_max_rating import ArenaTournamentsStartedItemMaxRating
        from ..models.arena_tournaments_started_item_custom_position import ArenaTournamentsStartedItemCustomPosition
        d = dict(src_dict)
        id = d.pop("id")

        created_by = d.pop("createdBy")

        system = cast(Literal['arena'] , d.pop("system"))
        if system != 'arena':
            raise ValueError(f"system must match const 'arena', got '{system}'")

        minutes = d.pop("minutes")

        clock = ArenaTournamentsStartedItemClock.from_dict(d.pop("clock"))




        rated = d.pop("rated")

        full_name = d.pop("fullName")

        nb_players = d.pop("nbPlayers")

        variant = ArenaTournamentsStartedItemVariant.from_dict(d.pop("variant"))




        starts_at = d.pop("startsAt")

        finishes_at = d.pop("finishesAt")

        status = ArenaTournamentsStartedItemStatus(d.pop("status"))




        perf = ArenaTournamentsStartedItemPerf.from_dict(d.pop("perf"))




        seconds_to_start = d.pop("secondsToStart", UNSET)

        has_max_rating = d.pop("hasMaxRating", UNSET)

        _max_rating = d.pop("maxRating", UNSET)
        max_rating: Union[Unset, ArenaTournamentsStartedItemMaxRating]
        if isinstance(_max_rating,  Unset):
            max_rating = UNSET
        else:
            max_rating = ArenaTournamentsStartedItemMaxRating.from_dict(_max_rating)




        _min_rating = d.pop("minRating", UNSET)
        min_rating: Union[Unset, ArenaTournamentsStartedItemMinRating]
        if isinstance(_min_rating,  Unset):
            min_rating = UNSET
        else:
            min_rating = ArenaTournamentsStartedItemMinRating.from_dict(_min_rating)




        _min_rated_games = d.pop("minRatedGames", UNSET)
        min_rated_games: Union[Unset, ArenaTournamentsStartedItemMinRatedGames]
        if isinstance(_min_rated_games,  Unset):
            min_rated_games = UNSET
        else:
            min_rated_games = ArenaTournamentsStartedItemMinRatedGames.from_dict(_min_rated_games)




        bots_allowed = d.pop("botsAllowed", UNSET)

        min_account_age_in_days = d.pop("minAccountAgeInDays", UNSET)

        only_titled = d.pop("onlyTitled", UNSET)

        team_member = d.pop("teamMember", UNSET)

        private = d.pop("private", UNSET)

        def _parse_position(data: object) -> Union['ArenaTournamentsStartedItemCustomPosition', 'ArenaTournamentsStartedItemThematic', Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                position_thematic = ArenaTournamentsStartedItemThematic.from_dict(data)



                return position_thematic
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            position_custom_position = ArenaTournamentsStartedItemCustomPosition.from_dict(data)



            return position_custom_position

        position = _parse_position(d.pop("position", UNSET))


        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, ArenaTournamentsStartedItemSchedule]
        if isinstance(_schedule,  Unset):
            schedule = UNSET
        else:
            schedule = ArenaTournamentsStartedItemSchedule.from_dict(_schedule)




        _team_battle = d.pop("teamBattle", UNSET)
        team_battle: Union[Unset, ArenaTournamentsStartedItemTeamBattle]
        if isinstance(_team_battle,  Unset):
            team_battle = UNSET
        else:
            team_battle = ArenaTournamentsStartedItemTeamBattle.from_dict(_team_battle)




        _winner = d.pop("winner", UNSET)
        winner: Union[Unset, ArenaTournamentsStartedItemWinner]
        if isinstance(_winner,  Unset):
            winner = UNSET
        else:
            winner = ArenaTournamentsStartedItemWinner.from_dict(_winner)




        arena_tournaments_started_item = cls(
            id=id,
            created_by=created_by,
            system=system,
            minutes=minutes,
            clock=clock,
            rated=rated,
            full_name=full_name,
            nb_players=nb_players,
            variant=variant,
            starts_at=starts_at,
            finishes_at=finishes_at,
            status=status,
            perf=perf,
            seconds_to_start=seconds_to_start,
            has_max_rating=has_max_rating,
            max_rating=max_rating,
            min_rating=min_rating,
            min_rated_games=min_rated_games,
            bots_allowed=bots_allowed,
            min_account_age_in_days=min_account_age_in_days,
            only_titled=only_titled,
            team_member=team_member,
            private=private,
            position=position,
            schedule=schedule,
            team_battle=team_battle,
            winner=winner,
        )


        arena_tournaments_started_item.additional_properties = d
        return arena_tournaments_started_item

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
