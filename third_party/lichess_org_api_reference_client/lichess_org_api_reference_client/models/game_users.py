from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.game_users_white import GameUsersWhite
  from ..models.game_users_black import GameUsersBlack





T = TypeVar("T", bound="GameUsers")



@_attrs_define
class GameUsers:
    """ 
        Attributes:
            white (GameUsersWhite):
            black (GameUsersBlack):
     """

    white: 'GameUsersWhite'
    black: 'GameUsersBlack'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.game_users_white import GameUsersWhite
        from ..models.game_users_black import GameUsersBlack
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
        from ..models.game_users_white import GameUsersWhite
        from ..models.game_users_black import GameUsersBlack
        d = dict(src_dict)
        white = GameUsersWhite.from_dict(d.pop("white"))




        black = GameUsersBlack.from_dict(d.pop("black"))




        game_users = cls(
            white=white,
            black=black,
        )


        game_users.additional_properties = d
        return game_users

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
