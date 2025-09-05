from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_activity_correspondence_game_color import UserActivityCorrespondenceGameColor
from ..models.user_activity_correspondence_game_variant import UserActivityCorrespondenceGameVariant
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.user_activity_correspondence_game_opponent import UserActivityCorrespondenceGameOpponent





T = TypeVar("T", bound="UserActivityCorrespondenceGame")



@_attrs_define
class UserActivityCorrespondenceGame:
    """ 
        Attributes:
            id (str):
            color (UserActivityCorrespondenceGameColor):
            url (str):
            variant (UserActivityCorrespondenceGameVariant):  Default: UserActivityCorrespondenceGameVariant.STANDARD.
                Example: standard.
            speed (Literal['correspondence']):
            perf (Literal['correspondence']):
            rated (bool):
            opponent (UserActivityCorrespondenceGameOpponent):
     """

    id: str
    color: UserActivityCorrespondenceGameColor
    url: str
    speed: Literal['correspondence']
    perf: Literal['correspondence']
    rated: bool
    opponent: 'UserActivityCorrespondenceGameOpponent'
    variant: UserActivityCorrespondenceGameVariant = UserActivityCorrespondenceGameVariant.STANDARD
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_activity_correspondence_game_opponent import UserActivityCorrespondenceGameOpponent
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
        from ..models.user_activity_correspondence_game_opponent import UserActivityCorrespondenceGameOpponent
        d = dict(src_dict)
        id = d.pop("id")

        color = UserActivityCorrespondenceGameColor(d.pop("color"))




        url = d.pop("url")

        variant = UserActivityCorrespondenceGameVariant(d.pop("variant"))




        speed = cast(Literal['correspondence'] , d.pop("speed"))
        if speed != 'correspondence':
            raise ValueError(f"speed must match const 'correspondence', got '{speed}'")

        perf = cast(Literal['correspondence'] , d.pop("perf"))
        if perf != 'correspondence':
            raise ValueError(f"perf must match const 'correspondence', got '{perf}'")

        rated = d.pop("rated")

        opponent = UserActivityCorrespondenceGameOpponent.from_dict(d.pop("opponent"))




        user_activity_correspondence_game = cls(
            id=id,
            color=color,
            url=url,
            variant=variant,
            speed=speed,
            perf=perf,
            rated=rated,
            opponent=opponent,
        )


        user_activity_correspondence_game.additional_properties = d
        return user_activity_correspondence_game

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
