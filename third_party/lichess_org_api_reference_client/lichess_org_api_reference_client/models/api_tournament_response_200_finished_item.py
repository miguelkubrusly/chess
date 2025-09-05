from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_tournament_response_200_finished_item_status import ApiTournamentResponse200FinishedItemStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Literal, cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_tournament_response_200_finished_item_min_rating import ApiTournamentResponse200FinishedItemMinRating
  from ..models.api_tournament_response_200_finished_item_variant import ApiTournamentResponse200FinishedItemVariant
  from ..models.api_tournament_response_200_finished_item_thematic import ApiTournamentResponse200FinishedItemThematic
  from ..models.api_tournament_response_200_finished_item_perf import ApiTournamentResponse200FinishedItemPerf
  from ..models.api_tournament_response_200_finished_item_winner import ApiTournamentResponse200FinishedItemWinner
  from ..models.api_tournament_response_200_finished_item_clock import ApiTournamentResponse200FinishedItemClock
  from ..models.api_tournament_response_200_finished_item_custom_position import ApiTournamentResponse200FinishedItemCustomPosition
  from ..models.api_tournament_response_200_finished_item_team_battle import ApiTournamentResponse200FinishedItemTeamBattle
  from ..models.api_tournament_response_200_finished_item_min_rated_games import ApiTournamentResponse200FinishedItemMinRatedGames
  from ..models.api_tournament_response_200_finished_item_schedule import ApiTournamentResponse200FinishedItemSchedule
  from ..models.api_tournament_response_200_finished_item_max_rating import ApiTournamentResponse200FinishedItemMaxRating





T = TypeVar("T", bound="ApiTournamentResponse200FinishedItem")



@_attrs_define
class ApiTournamentResponse200FinishedItem:
    """ 
        Attributes:
            id (str):
            created_by (str):
            system (Literal['arena']):
            minutes (int):
            clock (ApiTournamentResponse200FinishedItemClock):
            rated (bool):
            full_name (str):
            nb_players (int):
            variant (ApiTournamentResponse200FinishedItemVariant):
            starts_at (int):
            finishes_at (int):
            status (ApiTournamentResponse200FinishedItemStatus): 10: created, 20: started, 30: finished
            perf (ApiTournamentResponse200FinishedItemPerf):
            seconds_to_start (Union[Unset, int]):
            has_max_rating (Union[Unset, bool]):
            max_rating (Union[Unset, ApiTournamentResponse200FinishedItemMaxRating]):
            min_rating (Union[Unset, ApiTournamentResponse200FinishedItemMinRating]):
            min_rated_games (Union[Unset, ApiTournamentResponse200FinishedItemMinRatedGames]):
            bots_allowed (Union[Unset, bool]):
            min_account_age_in_days (Union[Unset, int]):
            only_titled (Union[Unset, bool]):
            team_member (Union[Unset, str]):
            private (Union[Unset, bool]):
            position (Union['ApiTournamentResponse200FinishedItemCustomPosition',
                'ApiTournamentResponse200FinishedItemThematic', Unset]):
            schedule (Union[Unset, ApiTournamentResponse200FinishedItemSchedule]):
            team_battle (Union[Unset, ApiTournamentResponse200FinishedItemTeamBattle]):
            winner (Union[Unset, ApiTournamentResponse200FinishedItemWinner]):
     """

    id: str
    created_by: str
    system: Literal['arena']
    minutes: int
    clock: 'ApiTournamentResponse200FinishedItemClock'
    rated: bool
    full_name: str
    nb_players: int
    variant: 'ApiTournamentResponse200FinishedItemVariant'
    starts_at: int
    finishes_at: int
    status: ApiTournamentResponse200FinishedItemStatus
    perf: 'ApiTournamentResponse200FinishedItemPerf'
    seconds_to_start: Union[Unset, int] = UNSET
    has_max_rating: Union[Unset, bool] = UNSET
    max_rating: Union[Unset, 'ApiTournamentResponse200FinishedItemMaxRating'] = UNSET
    min_rating: Union[Unset, 'ApiTournamentResponse200FinishedItemMinRating'] = UNSET
    min_rated_games: Union[Unset, 'ApiTournamentResponse200FinishedItemMinRatedGames'] = UNSET
    bots_allowed: Union[Unset, bool] = UNSET
    min_account_age_in_days: Union[Unset, int] = UNSET
    only_titled: Union[Unset, bool] = UNSET
    team_member: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = UNSET
    position: Union['ApiTournamentResponse200FinishedItemCustomPosition', 'ApiTournamentResponse200FinishedItemThematic', Unset] = UNSET
    schedule: Union[Unset, 'ApiTournamentResponse200FinishedItemSchedule'] = UNSET
    team_battle: Union[Unset, 'ApiTournamentResponse200FinishedItemTeamBattle'] = UNSET
    winner: Union[Unset, 'ApiTournamentResponse200FinishedItemWinner'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_tournament_response_200_finished_item_min_rating import ApiTournamentResponse200FinishedItemMinRating
        from ..models.api_tournament_response_200_finished_item_variant import ApiTournamentResponse200FinishedItemVariant
        from ..models.api_tournament_response_200_finished_item_thematic import ApiTournamentResponse200FinishedItemThematic
        from ..models.api_tournament_response_200_finished_item_perf import ApiTournamentResponse200FinishedItemPerf
        from ..models.api_tournament_response_200_finished_item_winner import ApiTournamentResponse200FinishedItemWinner
        from ..models.api_tournament_response_200_finished_item_clock import ApiTournamentResponse200FinishedItemClock
        from ..models.api_tournament_response_200_finished_item_custom_position import ApiTournamentResponse200FinishedItemCustomPosition
        from ..models.api_tournament_response_200_finished_item_team_battle import ApiTournamentResponse200FinishedItemTeamBattle
        from ..models.api_tournament_response_200_finished_item_min_rated_games import ApiTournamentResponse200FinishedItemMinRatedGames
        from ..models.api_tournament_response_200_finished_item_schedule import ApiTournamentResponse200FinishedItemSchedule
        from ..models.api_tournament_response_200_finished_item_max_rating import ApiTournamentResponse200FinishedItemMaxRating
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
        elif isinstance(self.position, ApiTournamentResponse200FinishedItemThematic):
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
        from ..models.api_tournament_response_200_finished_item_min_rating import ApiTournamentResponse200FinishedItemMinRating
        from ..models.api_tournament_response_200_finished_item_variant import ApiTournamentResponse200FinishedItemVariant
        from ..models.api_tournament_response_200_finished_item_thematic import ApiTournamentResponse200FinishedItemThematic
        from ..models.api_tournament_response_200_finished_item_perf import ApiTournamentResponse200FinishedItemPerf
        from ..models.api_tournament_response_200_finished_item_winner import ApiTournamentResponse200FinishedItemWinner
        from ..models.api_tournament_response_200_finished_item_clock import ApiTournamentResponse200FinishedItemClock
        from ..models.api_tournament_response_200_finished_item_custom_position import ApiTournamentResponse200FinishedItemCustomPosition
        from ..models.api_tournament_response_200_finished_item_team_battle import ApiTournamentResponse200FinishedItemTeamBattle
        from ..models.api_tournament_response_200_finished_item_min_rated_games import ApiTournamentResponse200FinishedItemMinRatedGames
        from ..models.api_tournament_response_200_finished_item_schedule import ApiTournamentResponse200FinishedItemSchedule
        from ..models.api_tournament_response_200_finished_item_max_rating import ApiTournamentResponse200FinishedItemMaxRating
        d = dict(src_dict)
        id = d.pop("id")

        created_by = d.pop("createdBy")

        system = cast(Literal['arena'] , d.pop("system"))
        if system != 'arena':
            raise ValueError(f"system must match const 'arena', got '{system}'")

        minutes = d.pop("minutes")

        clock = ApiTournamentResponse200FinishedItemClock.from_dict(d.pop("clock"))




        rated = d.pop("rated")

        full_name = d.pop("fullName")

        nb_players = d.pop("nbPlayers")

        variant = ApiTournamentResponse200FinishedItemVariant.from_dict(d.pop("variant"))




        starts_at = d.pop("startsAt")

        finishes_at = d.pop("finishesAt")

        status = ApiTournamentResponse200FinishedItemStatus(d.pop("status"))




        perf = ApiTournamentResponse200FinishedItemPerf.from_dict(d.pop("perf"))




        seconds_to_start = d.pop("secondsToStart", UNSET)

        has_max_rating = d.pop("hasMaxRating", UNSET)

        _max_rating = d.pop("maxRating", UNSET)
        max_rating: Union[Unset, ApiTournamentResponse200FinishedItemMaxRating]
        if isinstance(_max_rating,  Unset):
            max_rating = UNSET
        else:
            max_rating = ApiTournamentResponse200FinishedItemMaxRating.from_dict(_max_rating)




        _min_rating = d.pop("minRating", UNSET)
        min_rating: Union[Unset, ApiTournamentResponse200FinishedItemMinRating]
        if isinstance(_min_rating,  Unset):
            min_rating = UNSET
        else:
            min_rating = ApiTournamentResponse200FinishedItemMinRating.from_dict(_min_rating)




        _min_rated_games = d.pop("minRatedGames", UNSET)
        min_rated_games: Union[Unset, ApiTournamentResponse200FinishedItemMinRatedGames]
        if isinstance(_min_rated_games,  Unset):
            min_rated_games = UNSET
        else:
            min_rated_games = ApiTournamentResponse200FinishedItemMinRatedGames.from_dict(_min_rated_games)




        bots_allowed = d.pop("botsAllowed", UNSET)

        min_account_age_in_days = d.pop("minAccountAgeInDays", UNSET)

        only_titled = d.pop("onlyTitled", UNSET)

        team_member = d.pop("teamMember", UNSET)

        private = d.pop("private", UNSET)

        def _parse_position(data: object) -> Union['ApiTournamentResponse200FinishedItemCustomPosition', 'ApiTournamentResponse200FinishedItemThematic', Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                position_thematic = ApiTournamentResponse200FinishedItemThematic.from_dict(data)



                return position_thematic
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            position_custom_position = ApiTournamentResponse200FinishedItemCustomPosition.from_dict(data)



            return position_custom_position

        position = _parse_position(d.pop("position", UNSET))


        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, ApiTournamentResponse200FinishedItemSchedule]
        if isinstance(_schedule,  Unset):
            schedule = UNSET
        else:
            schedule = ApiTournamentResponse200FinishedItemSchedule.from_dict(_schedule)




        _team_battle = d.pop("teamBattle", UNSET)
        team_battle: Union[Unset, ApiTournamentResponse200FinishedItemTeamBattle]
        if isinstance(_team_battle,  Unset):
            team_battle = UNSET
        else:
            team_battle = ApiTournamentResponse200FinishedItemTeamBattle.from_dict(_team_battle)




        _winner = d.pop("winner", UNSET)
        winner: Union[Unset, ApiTournamentResponse200FinishedItemWinner]
        if isinstance(_winner,  Unset):
            winner = UNSET
        else:
            winner = ApiTournamentResponse200FinishedItemWinner.from_dict(_winner)




        api_tournament_response_200_finished_item = cls(
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


        api_tournament_response_200_finished_item.additional_properties = d
        return api_tournament_response_200_finished_item

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
