from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_tournament_team_battle_post_response_200_schedule import ApiTournamentTeamBattlePostResponse200Schedule
  from ..models.api_tournament_team_battle_post_response_200_min_rated_games import ApiTournamentTeamBattlePostResponse200MinRatedGames
  from ..models.api_tournament_team_battle_post_response_200_perf import ApiTournamentTeamBattlePostResponse200Perf
  from ..models.api_tournament_team_battle_post_response_200_featured import ApiTournamentTeamBattlePostResponse200Featured
  from ..models.api_tournament_team_battle_post_response_200_spotlight import ApiTournamentTeamBattlePostResponse200Spotlight
  from ..models.api_tournament_team_battle_post_response_200_verdicts import ApiTournamentTeamBattlePostResponse200Verdicts
  from ..models.api_tournament_team_battle_post_response_200_podium_item import ApiTournamentTeamBattlePostResponse200PodiumItem
  from ..models.api_tournament_team_battle_post_response_200_great_player import ApiTournamentTeamBattlePostResponse200GreatPlayer
  from ..models.api_tournament_team_battle_post_response_200_stats import ApiTournamentTeamBattlePostResponse200Stats
  from ..models.api_tournament_team_battle_post_response_200_duels_item import ApiTournamentTeamBattlePostResponse200DuelsItem
  from ..models.api_tournament_team_battle_post_response_200_standing import ApiTournamentTeamBattlePostResponse200Standing
  from ..models.api_tournament_team_battle_post_response_200_max_rating import ApiTournamentTeamBattlePostResponse200MaxRating
  from ..models.api_tournament_team_battle_post_response_200_quote import ApiTournamentTeamBattlePostResponse200Quote
  from ..models.api_tournament_team_battle_post_response_200_min_rating import ApiTournamentTeamBattlePostResponse200MinRating
  from ..models.api_tournament_team_battle_post_response_200_clock import ApiTournamentTeamBattlePostResponse200Clock





T = TypeVar("T", bound="ApiTournamentTeamBattlePostResponse200")



@_attrs_define
class ApiTournamentTeamBattlePostResponse200:
    """ 
        Attributes:
            id (str):
            full_name (str):
            clock (ApiTournamentTeamBattlePostResponse200Clock):
            nb_players (float):
            rated (Union[Unset, bool]):
            spotlight (Union[Unset, ApiTournamentTeamBattlePostResponse200Spotlight]):
            berserkable (Union[Unset, bool]):
            only_titled (Union[Unset, bool]):
            minutes (Union[Unset, float]):
            created_by (Union[Unset, str]):
            system (Union[Unset, str]):
            seconds_to_start (Union[Unset, float]):
            seconds_to_finish (Union[Unset, float]):
            is_finished (Union[Unset, bool]):
            is_recently_finished (Union[Unset, bool]):
            pairings_closed (Union[Unset, bool]):
            starts_at (Union[Unset, str]):
            verdicts (Union[Unset, ApiTournamentTeamBattlePostResponse200Verdicts]):
            quote (Union[Unset, ApiTournamentTeamBattlePostResponse200Quote]): The quote displayed on the tournament page
            great_player (Union[Unset, ApiTournamentTeamBattlePostResponse200GreatPlayer]):
            allow_list (Union[Unset, list[str]]): List of usernames allowed to join the tournament
            has_max_rating (Union[Unset, bool]):
            max_rating (Union[Unset, ApiTournamentTeamBattlePostResponse200MaxRating]):
            min_rating (Union[Unset, ApiTournamentTeamBattlePostResponse200MinRating]):
            min_rated_games (Union[Unset, ApiTournamentTeamBattlePostResponse200MinRatedGames]):
            bots_allowed (Union[Unset, bool]):
            min_account_age_in_days (Union[Unset, int]):
            perf (Union[Unset, ApiTournamentTeamBattlePostResponse200Perf]):
            schedule (Union[Unset, ApiTournamentTeamBattlePostResponse200Schedule]):
            description (Union[Unset, str]):
            variant (Union[Unset, str]):
            duels (Union[Unset, list['ApiTournamentTeamBattlePostResponse200DuelsItem']]):
            standing (Union[Unset, ApiTournamentTeamBattlePostResponse200Standing]):
            featured (Union[Unset, ApiTournamentTeamBattlePostResponse200Featured]):
            podium (Union[Unset, list['ApiTournamentTeamBattlePostResponse200PodiumItem']]):
            stats (Union[Unset, ApiTournamentTeamBattlePostResponse200Stats]):
            my_username (Union[Unset, str]):
     """

    id: str
    full_name: str
    clock: 'ApiTournamentTeamBattlePostResponse200Clock'
    nb_players: float
    rated: Union[Unset, bool] = UNSET
    spotlight: Union[Unset, 'ApiTournamentTeamBattlePostResponse200Spotlight'] = UNSET
    berserkable: Union[Unset, bool] = UNSET
    only_titled: Union[Unset, bool] = UNSET
    minutes: Union[Unset, float] = UNSET
    created_by: Union[Unset, str] = UNSET
    system: Union[Unset, str] = UNSET
    seconds_to_start: Union[Unset, float] = UNSET
    seconds_to_finish: Union[Unset, float] = UNSET
    is_finished: Union[Unset, bool] = UNSET
    is_recently_finished: Union[Unset, bool] = UNSET
    pairings_closed: Union[Unset, bool] = UNSET
    starts_at: Union[Unset, str] = UNSET
    verdicts: Union[Unset, 'ApiTournamentTeamBattlePostResponse200Verdicts'] = UNSET
    quote: Union[Unset, 'ApiTournamentTeamBattlePostResponse200Quote'] = UNSET
    great_player: Union[Unset, 'ApiTournamentTeamBattlePostResponse200GreatPlayer'] = UNSET
    allow_list: Union[Unset, list[str]] = UNSET
    has_max_rating: Union[Unset, bool] = UNSET
    max_rating: Union[Unset, 'ApiTournamentTeamBattlePostResponse200MaxRating'] = UNSET
    min_rating: Union[Unset, 'ApiTournamentTeamBattlePostResponse200MinRating'] = UNSET
    min_rated_games: Union[Unset, 'ApiTournamentTeamBattlePostResponse200MinRatedGames'] = UNSET
    bots_allowed: Union[Unset, bool] = UNSET
    min_account_age_in_days: Union[Unset, int] = UNSET
    perf: Union[Unset, 'ApiTournamentTeamBattlePostResponse200Perf'] = UNSET
    schedule: Union[Unset, 'ApiTournamentTeamBattlePostResponse200Schedule'] = UNSET
    description: Union[Unset, str] = UNSET
    variant: Union[Unset, str] = UNSET
    duels: Union[Unset, list['ApiTournamentTeamBattlePostResponse200DuelsItem']] = UNSET
    standing: Union[Unset, 'ApiTournamentTeamBattlePostResponse200Standing'] = UNSET
    featured: Union[Unset, 'ApiTournamentTeamBattlePostResponse200Featured'] = UNSET
    podium: Union[Unset, list['ApiTournamentTeamBattlePostResponse200PodiumItem']] = UNSET
    stats: Union[Unset, 'ApiTournamentTeamBattlePostResponse200Stats'] = UNSET
    my_username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_tournament_team_battle_post_response_200_schedule import ApiTournamentTeamBattlePostResponse200Schedule
        from ..models.api_tournament_team_battle_post_response_200_min_rated_games import ApiTournamentTeamBattlePostResponse200MinRatedGames
        from ..models.api_tournament_team_battle_post_response_200_perf import ApiTournamentTeamBattlePostResponse200Perf
        from ..models.api_tournament_team_battle_post_response_200_featured import ApiTournamentTeamBattlePostResponse200Featured
        from ..models.api_tournament_team_battle_post_response_200_spotlight import ApiTournamentTeamBattlePostResponse200Spotlight
        from ..models.api_tournament_team_battle_post_response_200_verdicts import ApiTournamentTeamBattlePostResponse200Verdicts
        from ..models.api_tournament_team_battle_post_response_200_podium_item import ApiTournamentTeamBattlePostResponse200PodiumItem
        from ..models.api_tournament_team_battle_post_response_200_great_player import ApiTournamentTeamBattlePostResponse200GreatPlayer
        from ..models.api_tournament_team_battle_post_response_200_stats import ApiTournamentTeamBattlePostResponse200Stats
        from ..models.api_tournament_team_battle_post_response_200_duels_item import ApiTournamentTeamBattlePostResponse200DuelsItem
        from ..models.api_tournament_team_battle_post_response_200_standing import ApiTournamentTeamBattlePostResponse200Standing
        from ..models.api_tournament_team_battle_post_response_200_max_rating import ApiTournamentTeamBattlePostResponse200MaxRating
        from ..models.api_tournament_team_battle_post_response_200_quote import ApiTournamentTeamBattlePostResponse200Quote
        from ..models.api_tournament_team_battle_post_response_200_min_rating import ApiTournamentTeamBattlePostResponse200MinRating
        from ..models.api_tournament_team_battle_post_response_200_clock import ApiTournamentTeamBattlePostResponse200Clock
        id = self.id

        full_name = self.full_name

        clock = self.clock.to_dict()

        nb_players = self.nb_players

        rated = self.rated

        spotlight: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spotlight, Unset):
            spotlight = self.spotlight.to_dict()

        berserkable = self.berserkable

        only_titled = self.only_titled

        minutes = self.minutes

        created_by = self.created_by

        system = self.system

        seconds_to_start = self.seconds_to_start

        seconds_to_finish = self.seconds_to_finish

        is_finished = self.is_finished

        is_recently_finished = self.is_recently_finished

        pairings_closed = self.pairings_closed

        starts_at = self.starts_at

        verdicts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.verdicts, Unset):
            verdicts = self.verdicts.to_dict()

        quote: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quote, Unset):
            quote = self.quote.to_dict()

        great_player: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.great_player, Unset):
            great_player = self.great_player.to_dict()

        allow_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allow_list, Unset):
            allow_list = self.allow_list



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

        perf: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.perf, Unset):
            perf = self.perf.to_dict()

        schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        description = self.description

        variant = self.variant

        duels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.duels, Unset):
            duels = []
            for duels_item_data in self.duels:
                duels_item = duels_item_data.to_dict()
                duels.append(duels_item)



        standing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.standing, Unset):
            standing = self.standing.to_dict()

        featured: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.featured, Unset):
            featured = self.featured.to_dict()

        podium: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.podium, Unset):
            podium = []
            for podium_item_data in self.podium:
                podium_item = podium_item_data.to_dict()
                podium.append(podium_item)



        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        my_username = self.my_username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "fullName": full_name,
            "clock": clock,
            "nbPlayers": nb_players,
        })
        if rated is not UNSET:
            field_dict["rated"] = rated
        if spotlight is not UNSET:
            field_dict["spotlight"] = spotlight
        if berserkable is not UNSET:
            field_dict["berserkable"] = berserkable
        if only_titled is not UNSET:
            field_dict["onlyTitled"] = only_titled
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if system is not UNSET:
            field_dict["system"] = system
        if seconds_to_start is not UNSET:
            field_dict["secondsToStart"] = seconds_to_start
        if seconds_to_finish is not UNSET:
            field_dict["secondsToFinish"] = seconds_to_finish
        if is_finished is not UNSET:
            field_dict["isFinished"] = is_finished
        if is_recently_finished is not UNSET:
            field_dict["isRecentlyFinished"] = is_recently_finished
        if pairings_closed is not UNSET:
            field_dict["pairingsClosed"] = pairings_closed
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at
        if verdicts is not UNSET:
            field_dict["verdicts"] = verdicts
        if quote is not UNSET:
            field_dict["quote"] = quote
        if great_player is not UNSET:
            field_dict["greatPlayer"] = great_player
        if allow_list is not UNSET:
            field_dict["allowList"] = allow_list
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
        if perf is not UNSET:
            field_dict["perf"] = perf
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if description is not UNSET:
            field_dict["description"] = description
        if variant is not UNSET:
            field_dict["variant"] = variant
        if duels is not UNSET:
            field_dict["duels"] = duels
        if standing is not UNSET:
            field_dict["standing"] = standing
        if featured is not UNSET:
            field_dict["featured"] = featured
        if podium is not UNSET:
            field_dict["podium"] = podium
        if stats is not UNSET:
            field_dict["stats"] = stats
        if my_username is not UNSET:
            field_dict["myUsername"] = my_username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_tournament_team_battle_post_response_200_schedule import ApiTournamentTeamBattlePostResponse200Schedule
        from ..models.api_tournament_team_battle_post_response_200_min_rated_games import ApiTournamentTeamBattlePostResponse200MinRatedGames
        from ..models.api_tournament_team_battle_post_response_200_perf import ApiTournamentTeamBattlePostResponse200Perf
        from ..models.api_tournament_team_battle_post_response_200_featured import ApiTournamentTeamBattlePostResponse200Featured
        from ..models.api_tournament_team_battle_post_response_200_spotlight import ApiTournamentTeamBattlePostResponse200Spotlight
        from ..models.api_tournament_team_battle_post_response_200_verdicts import ApiTournamentTeamBattlePostResponse200Verdicts
        from ..models.api_tournament_team_battle_post_response_200_podium_item import ApiTournamentTeamBattlePostResponse200PodiumItem
        from ..models.api_tournament_team_battle_post_response_200_great_player import ApiTournamentTeamBattlePostResponse200GreatPlayer
        from ..models.api_tournament_team_battle_post_response_200_stats import ApiTournamentTeamBattlePostResponse200Stats
        from ..models.api_tournament_team_battle_post_response_200_duels_item import ApiTournamentTeamBattlePostResponse200DuelsItem
        from ..models.api_tournament_team_battle_post_response_200_standing import ApiTournamentTeamBattlePostResponse200Standing
        from ..models.api_tournament_team_battle_post_response_200_max_rating import ApiTournamentTeamBattlePostResponse200MaxRating
        from ..models.api_tournament_team_battle_post_response_200_quote import ApiTournamentTeamBattlePostResponse200Quote
        from ..models.api_tournament_team_battle_post_response_200_min_rating import ApiTournamentTeamBattlePostResponse200MinRating
        from ..models.api_tournament_team_battle_post_response_200_clock import ApiTournamentTeamBattlePostResponse200Clock
        d = dict(src_dict)
        id = d.pop("id")

        full_name = d.pop("fullName")

        clock = ApiTournamentTeamBattlePostResponse200Clock.from_dict(d.pop("clock"))




        nb_players = d.pop("nbPlayers")

        rated = d.pop("rated", UNSET)

        _spotlight = d.pop("spotlight", UNSET)
        spotlight: Union[Unset, ApiTournamentTeamBattlePostResponse200Spotlight]
        if isinstance(_spotlight,  Unset):
            spotlight = UNSET
        else:
            spotlight = ApiTournamentTeamBattlePostResponse200Spotlight.from_dict(_spotlight)




        berserkable = d.pop("berserkable", UNSET)

        only_titled = d.pop("onlyTitled", UNSET)

        minutes = d.pop("minutes", UNSET)

        created_by = d.pop("createdBy", UNSET)

        system = d.pop("system", UNSET)

        seconds_to_start = d.pop("secondsToStart", UNSET)

        seconds_to_finish = d.pop("secondsToFinish", UNSET)

        is_finished = d.pop("isFinished", UNSET)

        is_recently_finished = d.pop("isRecentlyFinished", UNSET)

        pairings_closed = d.pop("pairingsClosed", UNSET)

        starts_at = d.pop("startsAt", UNSET)

        _verdicts = d.pop("verdicts", UNSET)
        verdicts: Union[Unset, ApiTournamentTeamBattlePostResponse200Verdicts]
        if isinstance(_verdicts,  Unset):
            verdicts = UNSET
        else:
            verdicts = ApiTournamentTeamBattlePostResponse200Verdicts.from_dict(_verdicts)




        _quote = d.pop("quote", UNSET)
        quote: Union[Unset, ApiTournamentTeamBattlePostResponse200Quote]
        if isinstance(_quote,  Unset):
            quote = UNSET
        else:
            quote = ApiTournamentTeamBattlePostResponse200Quote.from_dict(_quote)




        _great_player = d.pop("greatPlayer", UNSET)
        great_player: Union[Unset, ApiTournamentTeamBattlePostResponse200GreatPlayer]
        if isinstance(_great_player,  Unset):
            great_player = UNSET
        else:
            great_player = ApiTournamentTeamBattlePostResponse200GreatPlayer.from_dict(_great_player)




        allow_list = cast(list[str], d.pop("allowList", UNSET))


        has_max_rating = d.pop("hasMaxRating", UNSET)

        _max_rating = d.pop("maxRating", UNSET)
        max_rating: Union[Unset, ApiTournamentTeamBattlePostResponse200MaxRating]
        if isinstance(_max_rating,  Unset):
            max_rating = UNSET
        else:
            max_rating = ApiTournamentTeamBattlePostResponse200MaxRating.from_dict(_max_rating)




        _min_rating = d.pop("minRating", UNSET)
        min_rating: Union[Unset, ApiTournamentTeamBattlePostResponse200MinRating]
        if isinstance(_min_rating,  Unset):
            min_rating = UNSET
        else:
            min_rating = ApiTournamentTeamBattlePostResponse200MinRating.from_dict(_min_rating)




        _min_rated_games = d.pop("minRatedGames", UNSET)
        min_rated_games: Union[Unset, ApiTournamentTeamBattlePostResponse200MinRatedGames]
        if isinstance(_min_rated_games,  Unset):
            min_rated_games = UNSET
        else:
            min_rated_games = ApiTournamentTeamBattlePostResponse200MinRatedGames.from_dict(_min_rated_games)




        bots_allowed = d.pop("botsAllowed", UNSET)

        min_account_age_in_days = d.pop("minAccountAgeInDays", UNSET)

        _perf = d.pop("perf", UNSET)
        perf: Union[Unset, ApiTournamentTeamBattlePostResponse200Perf]
        if isinstance(_perf,  Unset):
            perf = UNSET
        else:
            perf = ApiTournamentTeamBattlePostResponse200Perf.from_dict(_perf)




        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, ApiTournamentTeamBattlePostResponse200Schedule]
        if isinstance(_schedule,  Unset):
            schedule = UNSET
        else:
            schedule = ApiTournamentTeamBattlePostResponse200Schedule.from_dict(_schedule)




        description = d.pop("description", UNSET)

        variant = d.pop("variant", UNSET)

        duels = []
        _duels = d.pop("duels", UNSET)
        for duels_item_data in (_duels or []):
            duels_item = ApiTournamentTeamBattlePostResponse200DuelsItem.from_dict(duels_item_data)



            duels.append(duels_item)


        _standing = d.pop("standing", UNSET)
        standing: Union[Unset, ApiTournamentTeamBattlePostResponse200Standing]
        if isinstance(_standing,  Unset):
            standing = UNSET
        else:
            standing = ApiTournamentTeamBattlePostResponse200Standing.from_dict(_standing)




        _featured = d.pop("featured", UNSET)
        featured: Union[Unset, ApiTournamentTeamBattlePostResponse200Featured]
        if isinstance(_featured,  Unset):
            featured = UNSET
        else:
            featured = ApiTournamentTeamBattlePostResponse200Featured.from_dict(_featured)




        podium = []
        _podium = d.pop("podium", UNSET)
        for podium_item_data in (_podium or []):
            podium_item = ApiTournamentTeamBattlePostResponse200PodiumItem.from_dict(podium_item_data)



            podium.append(podium_item)


        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, ApiTournamentTeamBattlePostResponse200Stats]
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = ApiTournamentTeamBattlePostResponse200Stats.from_dict(_stats)




        my_username = d.pop("myUsername", UNSET)

        api_tournament_team_battle_post_response_200 = cls(
            id=id,
            full_name=full_name,
            clock=clock,
            nb_players=nb_players,
            rated=rated,
            spotlight=spotlight,
            berserkable=berserkable,
            only_titled=only_titled,
            minutes=minutes,
            created_by=created_by,
            system=system,
            seconds_to_start=seconds_to_start,
            seconds_to_finish=seconds_to_finish,
            is_finished=is_finished,
            is_recently_finished=is_recently_finished,
            pairings_closed=pairings_closed,
            starts_at=starts_at,
            verdicts=verdicts,
            quote=quote,
            great_player=great_player,
            allow_list=allow_list,
            has_max_rating=has_max_rating,
            max_rating=max_rating,
            min_rating=min_rating,
            min_rated_games=min_rated_games,
            bots_allowed=bots_allowed,
            min_account_age_in_days=min_account_age_in_days,
            perf=perf,
            schedule=schedule,
            description=description,
            variant=variant,
            duels=duels,
            standing=standing,
            featured=featured,
            podium=podium,
            stats=stats,
            my_username=my_username,
        )


        api_tournament_team_battle_post_response_200.additional_properties = d
        return api_tournament_team_battle_post_response_200

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
