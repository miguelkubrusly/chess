from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.user_activity_correspondence_moves_games_item import UserActivityCorrespondenceMovesGamesItem





T = TypeVar("T", bound="UserActivityCorrespondenceMoves")



@_attrs_define
class UserActivityCorrespondenceMoves:
    """ 
        Attributes:
            nb (float):
            games (list['UserActivityCorrespondenceMovesGamesItem']):
     """

    nb: float
    games: list['UserActivityCorrespondenceMovesGamesItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_activity_correspondence_moves_games_item import UserActivityCorrespondenceMovesGamesItem
        nb = self.nb

        games = []
        for games_item_data in self.games:
            games_item = games_item_data.to_dict()
            games.append(games_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "nb": nb,
            "games": games,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_activity_correspondence_moves_games_item import UserActivityCorrespondenceMovesGamesItem
        d = dict(src_dict)
        nb = d.pop("nb")

        games = []
        _games = d.pop("games")
        for games_item_data in (_games):
            games_item = UserActivityCorrespondenceMovesGamesItem.from_dict(games_item_data)



            games.append(games_item)


        user_activity_correspondence_moves = cls(
            nb=nb,
            games=games,
        )


        user_activity_correspondence_moves.additional_properties = d
        return user_activity_correspondence_moves

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
