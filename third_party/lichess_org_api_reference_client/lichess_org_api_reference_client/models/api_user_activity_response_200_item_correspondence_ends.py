from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_user_activity_response_200_item_correspondence_ends_score import ApiUserActivityResponse200ItemCorrespondenceEndsScore
  from ..models.api_user_activity_response_200_item_correspondence_ends_games_item import ApiUserActivityResponse200ItemCorrespondenceEndsGamesItem





T = TypeVar("T", bound="ApiUserActivityResponse200ItemCorrespondenceEnds")



@_attrs_define
class ApiUserActivityResponse200ItemCorrespondenceEnds:
    """ 
        Attributes:
            score (ApiUserActivityResponse200ItemCorrespondenceEndsScore):
            games (list['ApiUserActivityResponse200ItemCorrespondenceEndsGamesItem']):
     """

    score: 'ApiUserActivityResponse200ItemCorrespondenceEndsScore'
    games: list['ApiUserActivityResponse200ItemCorrespondenceEndsGamesItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_activity_response_200_item_correspondence_ends_score import ApiUserActivityResponse200ItemCorrespondenceEndsScore
        from ..models.api_user_activity_response_200_item_correspondence_ends_games_item import ApiUserActivityResponse200ItemCorrespondenceEndsGamesItem
        score = self.score.to_dict()

        games = []
        for games_item_data in self.games:
            games_item = games_item_data.to_dict()
            games.append(games_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "score": score,
            "games": games,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_user_activity_response_200_item_correspondence_ends_score import ApiUserActivityResponse200ItemCorrespondenceEndsScore
        from ..models.api_user_activity_response_200_item_correspondence_ends_games_item import ApiUserActivityResponse200ItemCorrespondenceEndsGamesItem
        d = dict(src_dict)
        score = ApiUserActivityResponse200ItemCorrespondenceEndsScore.from_dict(d.pop("score"))




        games = []
        _games = d.pop("games")
        for games_item_data in (_games):
            games_item = ApiUserActivityResponse200ItemCorrespondenceEndsGamesItem.from_dict(games_item_data)



            games.append(games_item)


        api_user_activity_response_200_item_correspondence_ends = cls(
            score=score,
            games=games,
        )


        api_user_activity_response_200_item_correspondence_ends.additional_properties = d
        return api_user_activity_response_200_item_correspondence_ends

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
