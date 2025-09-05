from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_user_activity_response_200_item_correspondence_ends_games_item_color import ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemColor
from ..models.api_user_activity_response_200_item_correspondence_ends_games_item_variant import ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemVariant
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.api_user_activity_response_200_item_correspondence_ends_games_item_opponent import ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemOpponent





T = TypeVar("T", bound="ApiUserActivityResponse200ItemCorrespondenceEndsGamesItem")



@_attrs_define
class ApiUserActivityResponse200ItemCorrespondenceEndsGamesItem:
    """ 
        Attributes:
            id (str):
            color (ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemColor):
            url (str):
            variant (ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemVariant):  Default:
                ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemVariant.STANDARD. Example: standard.
            speed (Literal['correspondence']):
            perf (Literal['correspondence']):
            rated (bool):
            opponent (ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemOpponent):
     """

    id: str
    color: ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemColor
    url: str
    speed: Literal['correspondence']
    perf: Literal['correspondence']
    rated: bool
    opponent: 'ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemOpponent'
    variant: ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemVariant = ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemVariant.STANDARD
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_activity_response_200_item_correspondence_ends_games_item_opponent import ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemOpponent
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
        from ..models.api_user_activity_response_200_item_correspondence_ends_games_item_opponent import ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemOpponent
        d = dict(src_dict)
        id = d.pop("id")

        color = ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemColor(d.pop("color"))




        url = d.pop("url")

        variant = ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemVariant(d.pop("variant"))




        speed = cast(Literal['correspondence'] , d.pop("speed"))
        if speed != 'correspondence':
            raise ValueError(f"speed must match const 'correspondence', got '{speed}'")

        perf = cast(Literal['correspondence'] , d.pop("perf"))
        if perf != 'correspondence':
            raise ValueError(f"perf must match const 'correspondence', got '{perf}'")

        rated = d.pop("rated")

        opponent = ApiUserActivityResponse200ItemCorrespondenceEndsGamesItemOpponent.from_dict(d.pop("opponent"))




        api_user_activity_response_200_item_correspondence_ends_games_item = cls(
            id=id,
            color=color,
            url=url,
            variant=variant,
            speed=speed,
            perf=perf,
            rated=rated,
            opponent=opponent,
        )


        api_user_activity_response_200_item_correspondence_ends_games_item.additional_properties = d
        return api_user_activity_response_200_item_correspondence_ends_games_item

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
