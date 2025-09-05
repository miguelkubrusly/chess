from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_user_activity_response_200_item_tournaments_best_item_tournament import ApiUserActivityResponse200ItemTournamentsBestItemTournament





T = TypeVar("T", bound="ApiUserActivityResponse200ItemTournamentsBestItem")



@_attrs_define
class ApiUserActivityResponse200ItemTournamentsBestItem:
    """ 
        Attributes:
            tournament (ApiUserActivityResponse200ItemTournamentsBestItemTournament):
            nb_games (float):
            score (float):
            rank (float):
            rank_percent (float):
     """

    tournament: 'ApiUserActivityResponse200ItemTournamentsBestItemTournament'
    nb_games: float
    score: float
    rank: float
    rank_percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_activity_response_200_item_tournaments_best_item_tournament import ApiUserActivityResponse200ItemTournamentsBestItemTournament
        tournament = self.tournament.to_dict()

        nb_games = self.nb_games

        score = self.score

        rank = self.rank

        rank_percent = self.rank_percent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tournament": tournament,
            "nbGames": nb_games,
            "score": score,
            "rank": rank,
            "rankPercent": rank_percent,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_user_activity_response_200_item_tournaments_best_item_tournament import ApiUserActivityResponse200ItemTournamentsBestItemTournament
        d = dict(src_dict)
        tournament = ApiUserActivityResponse200ItemTournamentsBestItemTournament.from_dict(d.pop("tournament"))




        nb_games = d.pop("nbGames")

        score = d.pop("score")

        rank = d.pop("rank")

        rank_percent = d.pop("rankPercent")

        api_user_activity_response_200_item_tournaments_best_item = cls(
            tournament=tournament,
            nb_games=nb_games,
            score=score,
            rank=rank,
            rank_percent=rank_percent,
        )


        api_user_activity_response_200_item_tournaments_best_item.additional_properties = d
        return api_user_activity_response_200_item_tournaments_best_item

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
