from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.chat_line_event_room import ChatLineEventRoom
from typing import Literal, cast






T = TypeVar("T", bound="ChatLineEvent")



@_attrs_define
class ChatLineEvent:
    """ 
        Example:
            {'type': 'chatLine', 'username': 'thibault', 'text': 'Good luck, have fun', 'room': 'player'}

        Attributes:
            type_ (Literal['chatLine']):
            room (ChatLineEventRoom):
            username (str):
            text (str):
     """

    type_: Literal['chatLine']
    room: ChatLineEventRoom
    username: str
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        room = self.room.value

        username = self.username

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "room": room,
            "username": username,
            "text": text,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['chatLine'] , d.pop("type"))
        if type_ != 'chatLine':
            raise ValueError(f"type must match const 'chatLine', got '{type_}'")

        room = ChatLineEventRoom(d.pop("room"))




        username = d.pop("username")

        text = d.pop("text")

        chat_line_event = cls(
            type_=type_,
            room=room,
            username=username,
            text=text,
        )


        chat_line_event.additional_properties = d
        return chat_line_event

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
