from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.game_users_white_user import GameUsersWhiteUser
  from ..models.game_users_white_analysis import GameUsersWhiteAnalysis





T = TypeVar("T", bound="GameUsersWhite")



@_attrs_define
class GameUsersWhite:
    """ 
        Attributes:
            user (GameUsersWhiteUser):
            rating (int):
            rating_diff (Union[Unset, int]):
            name (Union[Unset, str]):
            provisional (Union[Unset, bool]):
            ai_level (Union[Unset, int]):
            analysis (Union[Unset, GameUsersWhiteAnalysis]):
            team (Union[Unset, str]):
     """

    user: 'GameUsersWhiteUser'
    rating: int
    rating_diff: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    provisional: Union[Unset, bool] = UNSET
    ai_level: Union[Unset, int] = UNSET
    analysis: Union[Unset, 'GameUsersWhiteAnalysis'] = UNSET
    team: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.game_users_white_user import GameUsersWhiteUser
        from ..models.game_users_white_analysis import GameUsersWhiteAnalysis
        user = self.user.to_dict()

        rating = self.rating

        rating_diff = self.rating_diff

        name = self.name

        provisional = self.provisional

        ai_level = self.ai_level

        analysis: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.analysis, Unset):
            analysis = self.analysis.to_dict()

        team = self.team


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user": user,
            "rating": rating,
        })
        if rating_diff is not UNSET:
            field_dict["ratingDiff"] = rating_diff
        if name is not UNSET:
            field_dict["name"] = name
        if provisional is not UNSET:
            field_dict["provisional"] = provisional
        if ai_level is not UNSET:
            field_dict["aiLevel"] = ai_level
        if analysis is not UNSET:
            field_dict["analysis"] = analysis
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_users_white_user import GameUsersWhiteUser
        from ..models.game_users_white_analysis import GameUsersWhiteAnalysis
        d = dict(src_dict)
        user = GameUsersWhiteUser.from_dict(d.pop("user"))




        rating = d.pop("rating")

        rating_diff = d.pop("ratingDiff", UNSET)

        name = d.pop("name", UNSET)

        provisional = d.pop("provisional", UNSET)

        ai_level = d.pop("aiLevel", UNSET)

        _analysis = d.pop("analysis", UNSET)
        analysis: Union[Unset, GameUsersWhiteAnalysis]
        if isinstance(_analysis,  Unset):
            analysis = UNSET
        else:
            analysis = GameUsersWhiteAnalysis.from_dict(_analysis)




        team = d.pop("team", UNSET)

        game_users_white = cls(
            user=user,
            rating=rating,
            rating_diff=rating_diff,
            name=name,
            provisional=provisional,
            ai_level=ai_level,
            analysis=analysis,
            team=team,
        )


        game_users_white.additional_properties = d
        return game_users_white

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
