from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tv_channels_response_200_computer_color import TvChannelsResponse200ComputerColor
from typing import cast

if TYPE_CHECKING:
  from ..models.tv_channels_response_200_computer_user import TvChannelsResponse200ComputerUser





T = TypeVar("T", bound="TvChannelsResponse200Computer")



@_attrs_define
class TvChannelsResponse200Computer:
    """ 
        Attributes:
            user (TvChannelsResponse200ComputerUser):
            rating (float):
            game_id (str):
            color (TvChannelsResponse200ComputerColor):
     """

    user: 'TvChannelsResponse200ComputerUser'
    rating: float
    game_id: str
    color: TvChannelsResponse200ComputerColor
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tv_channels_response_200_computer_user import TvChannelsResponse200ComputerUser
        user = self.user.to_dict()

        rating = self.rating

        game_id = self.game_id

        color = self.color.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user": user,
            "rating": rating,
            "gameId": game_id,
            "color": color,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tv_channels_response_200_computer_user import TvChannelsResponse200ComputerUser
        d = dict(src_dict)
        user = TvChannelsResponse200ComputerUser.from_dict(d.pop("user"))




        rating = d.pop("rating")

        game_id = d.pop("gameId")

        color = TvChannelsResponse200ComputerColor(d.pop("color"))




        tv_channels_response_200_computer = cls(
            user=user,
            rating=rating,
            game_id=game_id,
            color=color,
        )


        tv_channels_response_200_computer.additional_properties = d
        return tv_channels_response_200_computer

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
