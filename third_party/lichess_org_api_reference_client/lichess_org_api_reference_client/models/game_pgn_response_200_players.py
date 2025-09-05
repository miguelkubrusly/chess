from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.game_pgn_response_200_players_white import GamePgnResponse200PlayersWhite
  from ..models.game_pgn_response_200_players_black import GamePgnResponse200PlayersBlack





T = TypeVar("T", bound="GamePgnResponse200Players")



@_attrs_define
class GamePgnResponse200Players:
    """ 
        Attributes:
            white (GamePgnResponse200PlayersWhite):
            black (GamePgnResponse200PlayersBlack):
     """

    white: 'GamePgnResponse200PlayersWhite'
    black: 'GamePgnResponse200PlayersBlack'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.game_pgn_response_200_players_white import GamePgnResponse200PlayersWhite
        from ..models.game_pgn_response_200_players_black import GamePgnResponse200PlayersBlack
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
        from ..models.game_pgn_response_200_players_white import GamePgnResponse200PlayersWhite
        from ..models.game_pgn_response_200_players_black import GamePgnResponse200PlayersBlack
        d = dict(src_dict)
        white = GamePgnResponse200PlayersWhite.from_dict(d.pop("white"))




        black = GamePgnResponse200PlayersBlack.from_dict(d.pop("black"))




        game_pgn_response_200_players = cls(
            white=white,
            black=black,
        )


        game_pgn_response_200_players.additional_properties = d
        return game_pgn_response_200_players

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
