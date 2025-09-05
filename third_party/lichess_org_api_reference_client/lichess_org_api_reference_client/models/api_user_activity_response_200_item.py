from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_user_activity_response_200_item_teams_item import ApiUserActivityResponse200ItemTeamsItem
  from ..models.api_user_activity_response_200_item_practice_item import ApiUserActivityResponse200ItemPracticeItem
  from ..models.api_user_activity_response_200_item_posts_item import ApiUserActivityResponse200ItemPostsItem
  from ..models.api_user_activity_response_200_item_correspondence_moves import ApiUserActivityResponse200ItemCorrespondenceMoves
  from ..models.api_user_activity_response_200_item_puzzles import ApiUserActivityResponse200ItemPuzzles
  from ..models.api_user_activity_response_200_item_streak import ApiUserActivityResponse200ItemStreak
  from ..models.api_user_activity_response_200_item_tournaments import ApiUserActivityResponse200ItemTournaments
  from ..models.api_user_activity_response_200_item_racer import ApiUserActivityResponse200ItemRacer
  from ..models.api_user_activity_response_200_item_interval import ApiUserActivityResponse200ItemInterval
  from ..models.api_user_activity_response_200_item_games import ApiUserActivityResponse200ItemGames
  from ..models.api_user_activity_response_200_item_correspondence_ends import ApiUserActivityResponse200ItemCorrespondenceEnds
  from ..models.api_user_activity_response_200_item_studies import ApiUserActivityResponse200ItemStudies
  from ..models.api_user_activity_response_200_item_follows import ApiUserActivityResponse200ItemFollows
  from ..models.api_user_activity_response_200_item_patron import ApiUserActivityResponse200ItemPatron
  from ..models.api_user_activity_response_200_item_storm import ApiUserActivityResponse200ItemStorm





T = TypeVar("T", bound="ApiUserActivityResponse200Item")



@_attrs_define
class ApiUserActivityResponse200Item:
    """ 
        Attributes:
            interval (ApiUserActivityResponse200ItemInterval):
            games (Union[Unset, ApiUserActivityResponse200ItemGames]):
            puzzles (Union[Unset, ApiUserActivityResponse200ItemPuzzles]):
            storm (Union[Unset, ApiUserActivityResponse200ItemStorm]):
            racer (Union[Unset, ApiUserActivityResponse200ItemRacer]):
            streak (Union[Unset, ApiUserActivityResponse200ItemStreak]):
            tournaments (Union[Unset, ApiUserActivityResponse200ItemTournaments]):
            practice (Union[Unset, list['ApiUserActivityResponse200ItemPracticeItem']]):
            simuls (Union[Unset, list[str]]):
            correspondence_moves (Union[Unset, ApiUserActivityResponse200ItemCorrespondenceMoves]):
            correspondence_ends (Union[Unset, ApiUserActivityResponse200ItemCorrespondenceEnds]):
            follows (Union[Unset, ApiUserActivityResponse200ItemFollows]):
            studies (Union[Unset, ApiUserActivityResponse200ItemStudies]):
            teams (Union[Unset, list['ApiUserActivityResponse200ItemTeamsItem']]):
            posts (Union[Unset, list['ApiUserActivityResponse200ItemPostsItem']]):
            patron (Union[Unset, ApiUserActivityResponse200ItemPatron]):
            stream (Union[Unset, bool]):
     """

    interval: 'ApiUserActivityResponse200ItemInterval'
    games: Union[Unset, 'ApiUserActivityResponse200ItemGames'] = UNSET
    puzzles: Union[Unset, 'ApiUserActivityResponse200ItemPuzzles'] = UNSET
    storm: Union[Unset, 'ApiUserActivityResponse200ItemStorm'] = UNSET
    racer: Union[Unset, 'ApiUserActivityResponse200ItemRacer'] = UNSET
    streak: Union[Unset, 'ApiUserActivityResponse200ItemStreak'] = UNSET
    tournaments: Union[Unset, 'ApiUserActivityResponse200ItemTournaments'] = UNSET
    practice: Union[Unset, list['ApiUserActivityResponse200ItemPracticeItem']] = UNSET
    simuls: Union[Unset, list[str]] = UNSET
    correspondence_moves: Union[Unset, 'ApiUserActivityResponse200ItemCorrespondenceMoves'] = UNSET
    correspondence_ends: Union[Unset, 'ApiUserActivityResponse200ItemCorrespondenceEnds'] = UNSET
    follows: Union[Unset, 'ApiUserActivityResponse200ItemFollows'] = UNSET
    studies: Union[Unset, 'ApiUserActivityResponse200ItemStudies'] = UNSET
    teams: Union[Unset, list['ApiUserActivityResponse200ItemTeamsItem']] = UNSET
    posts: Union[Unset, list['ApiUserActivityResponse200ItemPostsItem']] = UNSET
    patron: Union[Unset, 'ApiUserActivityResponse200ItemPatron'] = UNSET
    stream: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_activity_response_200_item_teams_item import ApiUserActivityResponse200ItemTeamsItem
        from ..models.api_user_activity_response_200_item_practice_item import ApiUserActivityResponse200ItemPracticeItem
        from ..models.api_user_activity_response_200_item_posts_item import ApiUserActivityResponse200ItemPostsItem
        from ..models.api_user_activity_response_200_item_correspondence_moves import ApiUserActivityResponse200ItemCorrespondenceMoves
        from ..models.api_user_activity_response_200_item_puzzles import ApiUserActivityResponse200ItemPuzzles
        from ..models.api_user_activity_response_200_item_streak import ApiUserActivityResponse200ItemStreak
        from ..models.api_user_activity_response_200_item_tournaments import ApiUserActivityResponse200ItemTournaments
        from ..models.api_user_activity_response_200_item_racer import ApiUserActivityResponse200ItemRacer
        from ..models.api_user_activity_response_200_item_interval import ApiUserActivityResponse200ItemInterval
        from ..models.api_user_activity_response_200_item_games import ApiUserActivityResponse200ItemGames
        from ..models.api_user_activity_response_200_item_correspondence_ends import ApiUserActivityResponse200ItemCorrespondenceEnds
        from ..models.api_user_activity_response_200_item_studies import ApiUserActivityResponse200ItemStudies
        from ..models.api_user_activity_response_200_item_follows import ApiUserActivityResponse200ItemFollows
        from ..models.api_user_activity_response_200_item_patron import ApiUserActivityResponse200ItemPatron
        from ..models.api_user_activity_response_200_item_storm import ApiUserActivityResponse200ItemStorm
        interval = self.interval.to_dict()

        games: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.games, Unset):
            games = self.games.to_dict()

        puzzles: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.puzzles, Unset):
            puzzles = self.puzzles.to_dict()

        storm: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.storm, Unset):
            storm = self.storm.to_dict()

        racer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.racer, Unset):
            racer = self.racer.to_dict()

        streak: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.streak, Unset):
            streak = self.streak.to_dict()

        tournaments: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tournaments, Unset):
            tournaments = self.tournaments.to_dict()

        practice: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.practice, Unset):
            practice = []
            for practice_item_data in self.practice:
                practice_item = practice_item_data.to_dict()
                practice.append(practice_item)



        simuls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.simuls, Unset):
            simuls = self.simuls



        correspondence_moves: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.correspondence_moves, Unset):
            correspondence_moves = self.correspondence_moves.to_dict()

        correspondence_ends: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.correspondence_ends, Unset):
            correspondence_ends = self.correspondence_ends.to_dict()

        follows: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.follows, Unset):
            follows = self.follows.to_dict()

        studies: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.studies, Unset):
            studies = self.studies.to_dict()

        teams: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)



        posts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.posts, Unset):
            posts = []
            for posts_item_data in self.posts:
                posts_item = posts_item_data.to_dict()
                posts.append(posts_item)



        patron: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.patron, Unset):
            patron = self.patron.to_dict()

        stream = self.stream


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "interval": interval,
        })
        if games is not UNSET:
            field_dict["games"] = games
        if puzzles is not UNSET:
            field_dict["puzzles"] = puzzles
        if storm is not UNSET:
            field_dict["storm"] = storm
        if racer is not UNSET:
            field_dict["racer"] = racer
        if streak is not UNSET:
            field_dict["streak"] = streak
        if tournaments is not UNSET:
            field_dict["tournaments"] = tournaments
        if practice is not UNSET:
            field_dict["practice"] = practice
        if simuls is not UNSET:
            field_dict["simuls"] = simuls
        if correspondence_moves is not UNSET:
            field_dict["correspondenceMoves"] = correspondence_moves
        if correspondence_ends is not UNSET:
            field_dict["correspondenceEnds"] = correspondence_ends
        if follows is not UNSET:
            field_dict["follows"] = follows
        if studies is not UNSET:
            field_dict["studies"] = studies
        if teams is not UNSET:
            field_dict["teams"] = teams
        if posts is not UNSET:
            field_dict["posts"] = posts
        if patron is not UNSET:
            field_dict["patron"] = patron
        if stream is not UNSET:
            field_dict["stream"] = stream

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_user_activity_response_200_item_teams_item import ApiUserActivityResponse200ItemTeamsItem
        from ..models.api_user_activity_response_200_item_practice_item import ApiUserActivityResponse200ItemPracticeItem
        from ..models.api_user_activity_response_200_item_posts_item import ApiUserActivityResponse200ItemPostsItem
        from ..models.api_user_activity_response_200_item_correspondence_moves import ApiUserActivityResponse200ItemCorrespondenceMoves
        from ..models.api_user_activity_response_200_item_puzzles import ApiUserActivityResponse200ItemPuzzles
        from ..models.api_user_activity_response_200_item_streak import ApiUserActivityResponse200ItemStreak
        from ..models.api_user_activity_response_200_item_tournaments import ApiUserActivityResponse200ItemTournaments
        from ..models.api_user_activity_response_200_item_racer import ApiUserActivityResponse200ItemRacer
        from ..models.api_user_activity_response_200_item_interval import ApiUserActivityResponse200ItemInterval
        from ..models.api_user_activity_response_200_item_games import ApiUserActivityResponse200ItemGames
        from ..models.api_user_activity_response_200_item_correspondence_ends import ApiUserActivityResponse200ItemCorrespondenceEnds
        from ..models.api_user_activity_response_200_item_studies import ApiUserActivityResponse200ItemStudies
        from ..models.api_user_activity_response_200_item_follows import ApiUserActivityResponse200ItemFollows
        from ..models.api_user_activity_response_200_item_patron import ApiUserActivityResponse200ItemPatron
        from ..models.api_user_activity_response_200_item_storm import ApiUserActivityResponse200ItemStorm
        d = dict(src_dict)
        interval = ApiUserActivityResponse200ItemInterval.from_dict(d.pop("interval"))




        _games = d.pop("games", UNSET)
        games: Union[Unset, ApiUserActivityResponse200ItemGames]
        if isinstance(_games,  Unset):
            games = UNSET
        else:
            games = ApiUserActivityResponse200ItemGames.from_dict(_games)




        _puzzles = d.pop("puzzles", UNSET)
        puzzles: Union[Unset, ApiUserActivityResponse200ItemPuzzles]
        if isinstance(_puzzles,  Unset):
            puzzles = UNSET
        else:
            puzzles = ApiUserActivityResponse200ItemPuzzles.from_dict(_puzzles)




        _storm = d.pop("storm", UNSET)
        storm: Union[Unset, ApiUserActivityResponse200ItemStorm]
        if isinstance(_storm,  Unset):
            storm = UNSET
        else:
            storm = ApiUserActivityResponse200ItemStorm.from_dict(_storm)




        _racer = d.pop("racer", UNSET)
        racer: Union[Unset, ApiUserActivityResponse200ItemRacer]
        if isinstance(_racer,  Unset):
            racer = UNSET
        else:
            racer = ApiUserActivityResponse200ItemRacer.from_dict(_racer)




        _streak = d.pop("streak", UNSET)
        streak: Union[Unset, ApiUserActivityResponse200ItemStreak]
        if isinstance(_streak,  Unset):
            streak = UNSET
        else:
            streak = ApiUserActivityResponse200ItemStreak.from_dict(_streak)




        _tournaments = d.pop("tournaments", UNSET)
        tournaments: Union[Unset, ApiUserActivityResponse200ItemTournaments]
        if isinstance(_tournaments,  Unset):
            tournaments = UNSET
        else:
            tournaments = ApiUserActivityResponse200ItemTournaments.from_dict(_tournaments)




        practice = []
        _practice = d.pop("practice", UNSET)
        for practice_item_data in (_practice or []):
            practice_item = ApiUserActivityResponse200ItemPracticeItem.from_dict(practice_item_data)



            practice.append(practice_item)


        simuls = cast(list[str], d.pop("simuls", UNSET))


        _correspondence_moves = d.pop("correspondenceMoves", UNSET)
        correspondence_moves: Union[Unset, ApiUserActivityResponse200ItemCorrespondenceMoves]
        if isinstance(_correspondence_moves,  Unset):
            correspondence_moves = UNSET
        else:
            correspondence_moves = ApiUserActivityResponse200ItemCorrespondenceMoves.from_dict(_correspondence_moves)




        _correspondence_ends = d.pop("correspondenceEnds", UNSET)
        correspondence_ends: Union[Unset, ApiUserActivityResponse200ItemCorrespondenceEnds]
        if isinstance(_correspondence_ends,  Unset):
            correspondence_ends = UNSET
        else:
            correspondence_ends = ApiUserActivityResponse200ItemCorrespondenceEnds.from_dict(_correspondence_ends)




        _follows = d.pop("follows", UNSET)
        follows: Union[Unset, ApiUserActivityResponse200ItemFollows]
        if isinstance(_follows,  Unset):
            follows = UNSET
        else:
            follows = ApiUserActivityResponse200ItemFollows.from_dict(_follows)




        _studies = d.pop("studies", UNSET)
        studies: Union[Unset, ApiUserActivityResponse200ItemStudies]
        if isinstance(_studies,  Unset):
            studies = UNSET
        else:
            studies = ApiUserActivityResponse200ItemStudies.from_dict(_studies)




        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in (_teams or []):
            teams_item = ApiUserActivityResponse200ItemTeamsItem.from_dict(teams_item_data)



            teams.append(teams_item)


        posts = []
        _posts = d.pop("posts", UNSET)
        for posts_item_data in (_posts or []):
            posts_item = ApiUserActivityResponse200ItemPostsItem.from_dict(posts_item_data)



            posts.append(posts_item)


        _patron = d.pop("patron", UNSET)
        patron: Union[Unset, ApiUserActivityResponse200ItemPatron]
        if isinstance(_patron,  Unset):
            patron = UNSET
        else:
            patron = ApiUserActivityResponse200ItemPatron.from_dict(_patron)




        stream = d.pop("stream", UNSET)

        api_user_activity_response_200_item = cls(
            interval=interval,
            games=games,
            puzzles=puzzles,
            storm=storm,
            racer=racer,
            streak=streak,
            tournaments=tournaments,
            practice=practice,
            simuls=simuls,
            correspondence_moves=correspondence_moves,
            correspondence_ends=correspondence_ends,
            follows=follows,
            studies=studies,
            teams=teams,
            posts=posts,
            patron=patron,
            stream=stream,
        )


        api_user_activity_response_200_item.additional_properties = d
        return api_user_activity_response_200_item

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
