from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.board_game_chat_post_body_room import BoardGameChatPostBodyRoom






T = TypeVar("T", bound="BoardGameChatPostBody")



@_attrs_define
class BoardGameChatPostBody:
    """ 
        Attributes:
            room (BoardGameChatPostBodyRoom):
            text (str):  Example: Thank you for the game!.
     """

    room: BoardGameChatPostBodyRoom
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        room = self.room.value

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "room": room,
            "text": text,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room = BoardGameChatPostBodyRoom(d.pop("room"))




        text = d.pop("text")

        board_game_chat_post_body = cls(
            room=room,
            text=text,
        )


        board_game_chat_post_body.additional_properties = d
        return board_game_chat_post_body

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
