from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tv_feed_featured_players_item_color import TvFeedFeaturedPlayersItemColor
from typing import cast

if TYPE_CHECKING:
  from ..models.tv_feed_featured_players_item_user import TvFeedFeaturedPlayersItemUser





T = TypeVar("T", bound="TvFeedFeaturedPlayersItem")



@_attrs_define
class TvFeedFeaturedPlayersItem:
    """ 
        Attributes:
            color (TvFeedFeaturedPlayersItemColor):
            user (TvFeedFeaturedPlayersItemUser):
            rating (int):
            seconds (int): The player's remaining time in seconds
     """

    color: TvFeedFeaturedPlayersItemColor
    user: 'TvFeedFeaturedPlayersItemUser'
    rating: int
    seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tv_feed_featured_players_item_user import TvFeedFeaturedPlayersItemUser
        color = self.color.value

        user = self.user.to_dict()

        rating = self.rating

        seconds = self.seconds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "color": color,
            "user": user,
            "rating": rating,
            "seconds": seconds,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tv_feed_featured_players_item_user import TvFeedFeaturedPlayersItemUser
        d = dict(src_dict)
        color = TvFeedFeaturedPlayersItemColor(d.pop("color"))




        user = TvFeedFeaturedPlayersItemUser.from_dict(d.pop("user"))




        rating = d.pop("rating")

        seconds = d.pop("seconds")

        tv_feed_featured_players_item = cls(
            color=color,
            user=user,
            rating=rating,
            seconds=seconds,
        )


        tv_feed_featured_players_item.additional_properties = d
        return tv_feed_featured_players_item

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
