from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="StreamerLiveResponse200ItemStreamer")



@_attrs_define
class StreamerLiveResponse200ItemStreamer:
    """ 
        Attributes:
            name (Union[Unset, str]):
            headline (Union[Unset, str]):
            description (Union[Unset, str]):
            twitch (Union[Unset, str]):
            you_tube (Union[Unset, str]):
            image (Union[Unset, str]):
     """

    name: Union[Unset, str] = UNSET
    headline: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    twitch: Union[Unset, str] = UNSET
    you_tube: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        headline = self.headline

        description = self.description

        twitch = self.twitch

        you_tube = self.you_tube

        image = self.image


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description
        if twitch is not UNSET:
            field_dict["twitch"] = twitch
        if you_tube is not UNSET:
            field_dict["youTube"] = you_tube
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        headline = d.pop("headline", UNSET)

        description = d.pop("description", UNSET)

        twitch = d.pop("twitch", UNSET)

        you_tube = d.pop("youTube", UNSET)

        image = d.pop("image", UNSET)

        streamer_live_response_200_item_streamer = cls(
            name=name,
            headline=headline,
            description=description,
            twitch=twitch,
            you_tube=you_tube,
            image=image,
        )


        streamer_live_response_200_item_streamer.additional_properties = d
        return streamer_live_response_200_item_streamer

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
