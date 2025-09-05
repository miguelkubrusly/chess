from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, Union, cast
from typing import Union

if TYPE_CHECKING:
  from ..models.game_finish_event_game import GameFinishEventGame





T = TypeVar("T", bound="GameFinishEvent")



@_attrs_define
class GameFinishEvent:
    """ 
        Attributes:
            type_ (Union[Literal['gameFinish'], Unset]):
            game (Union[Unset, GameFinishEventGame]):
     """

    type_: Union[Literal['gameFinish'], Unset] = UNSET
    game: Union[Unset, 'GameFinishEventGame'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.game_finish_event_game import GameFinishEventGame
        type_ = self.type_

        game: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.game, Unset):
            game = self.game.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if game is not UNSET:
            field_dict["game"] = game

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_finish_event_game import GameFinishEventGame
        d = dict(src_dict)
        type_ = cast(Union[Literal['gameFinish'], Unset] , d.pop("type", UNSET))
        if type_ != 'gameFinish'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'gameFinish', got '{type_}'")

        _game = d.pop("game", UNSET)
        game: Union[Unset, GameFinishEventGame]
        if isinstance(_game,  Unset):
            game = UNSET
        else:
            game = GameFinishEventGame.from_dict(_game)




        game_finish_event = cls(
            type_=type_,
            game=game,
        )


        game_finish_event.additional_properties = d
        return game_finish_event

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
