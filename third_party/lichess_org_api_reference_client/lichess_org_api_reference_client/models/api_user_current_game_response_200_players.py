from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_user_current_game_response_200_players_black import ApiUserCurrentGameResponse200PlayersBlack
  from ..models.api_user_current_game_response_200_players_white import ApiUserCurrentGameResponse200PlayersWhite





T = TypeVar("T", bound="ApiUserCurrentGameResponse200Players")



@_attrs_define
class ApiUserCurrentGameResponse200Players:
    """ 
        Attributes:
            white (ApiUserCurrentGameResponse200PlayersWhite):
            black (ApiUserCurrentGameResponse200PlayersBlack):
     """

    white: 'ApiUserCurrentGameResponse200PlayersWhite'
    black: 'ApiUserCurrentGameResponse200PlayersBlack'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_current_game_response_200_players_black import ApiUserCurrentGameResponse200PlayersBlack
        from ..models.api_user_current_game_response_200_players_white import ApiUserCurrentGameResponse200PlayersWhite
        white = self.white.to_dict()

        black = self.black.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "white": white,
            "black": black,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_user_current_game_response_200_players_black import ApiUserCurrentGameResponse200PlayersBlack
        from ..models.api_user_current_game_response_200_players_white import ApiUserCurrentGameResponse200PlayersWhite
        d = dict(src_dict)
        white = ApiUserCurrentGameResponse200PlayersWhite.from_dict(d.pop("white"))




        black = ApiUserCurrentGameResponse200PlayersBlack.from_dict(d.pop("black"))




        api_user_current_game_response_200_players = cls(
            white=white,
            black=black,
        )


        api_user_current_game_response_200_players.additional_properties = d
        return api_user_current_game_response_200_players

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
