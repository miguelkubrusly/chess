from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_activity_correspondence_ends_games_item_color import UserActivityCorrespondenceEndsGamesItemColor
from ..models.user_activity_correspondence_ends_games_item_variant import UserActivityCorrespondenceEndsGamesItemVariant
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.user_activity_correspondence_ends_games_item_opponent import UserActivityCorrespondenceEndsGamesItemOpponent





T = TypeVar("T", bound="UserActivityCorrespondenceEndsGamesItem")



@_attrs_define
class UserActivityCorrespondenceEndsGamesItem:
    """ 
        Attributes:
            id (str):
            color (UserActivityCorrespondenceEndsGamesItemColor):
            url (str):
            variant (UserActivityCorrespondenceEndsGamesItemVariant):  Default:
                UserActivityCorrespondenceEndsGamesItemVariant.STANDARD. Example: standard.
            speed (Literal['correspondence']):
            perf (Literal['correspondence']):
            rated (bool):
            opponent (UserActivityCorrespondenceEndsGamesItemOpponent):
     """

    id: str
    color: UserActivityCorrespondenceEndsGamesItemColor
    url: str
    speed: Literal['correspondence']
    perf: Literal['correspondence']
    rated: bool
    opponent: 'UserActivityCorrespondenceEndsGamesItemOpponent'
    variant: UserActivityCorrespondenceEndsGamesItemVariant = UserActivityCorrespondenceEndsGamesItemVariant.STANDARD
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_activity_correspondence_ends_games_item_opponent import UserActivityCorrespondenceEndsGamesItemOpponent
        id = self.id

        color = self.color.value

        url = self.url

        variant = self.variant.value

        speed = self.speed

        perf = self.perf

        rated = self.rated

        opponent = self.opponent.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "color": color,
            "url": url,
            "variant": variant,
            "speed": speed,
            "perf": perf,
            "rated": rated,
            "opponent": opponent,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_activity_correspondence_ends_games_item_opponent import UserActivityCorrespondenceEndsGamesItemOpponent
        d = dict(src_dict)
        id = d.pop("id")

        color = UserActivityCorrespondenceEndsGamesItemColor(d.pop("color"))




        url = d.pop("url")

        variant = UserActivityCorrespondenceEndsGamesItemVariant(d.pop("variant"))




        speed = cast(Literal['correspondence'] , d.pop("speed"))
        if speed != 'correspondence':
            raise ValueError(f"speed must match const 'correspondence', got '{speed}'")

        perf = cast(Literal['correspondence'] , d.pop("perf"))
        if perf != 'correspondence':
            raise ValueError(f"perf must match const 'correspondence', got '{perf}'")

        rated = d.pop("rated")

        opponent = UserActivityCorrespondenceEndsGamesItemOpponent.from_dict(d.pop("opponent"))




        user_activity_correspondence_ends_games_item = cls(
            id=id,
            color=color,
            url=url,
            variant=variant,
            speed=speed,
            perf=perf,
            rated=rated,
            opponent=opponent,
        )


        user_activity_correspondence_ends_games_item.additional_properties = d
        return user_activity_correspondence_ends_games_item

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
