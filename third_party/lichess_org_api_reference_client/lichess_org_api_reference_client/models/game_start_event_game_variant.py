from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.game_start_event_game_variant_key import GameStartEventGameVariantKey
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="GameStartEventGameVariant")



@_attrs_define
class GameStartEventGameVariant:
    """ 
        Attributes:
            key (GameStartEventGameVariantKey):  Default: GameStartEventGameVariantKey.STANDARD. Example: standard.
            name (str):
            short (Union[Unset, str]):
     """

    name: str
    key: GameStartEventGameVariantKey = GameStartEventGameVariantKey.STANDARD
    short: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        name = self.name

        short = self.short


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "name": name,
        })
        if short is not UNSET:
            field_dict["short"] = short

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = GameStartEventGameVariantKey(d.pop("key"))




        name = d.pop("name")

        short = d.pop("short", UNSET)

        game_start_event_game_variant = cls(
            key=key,
            name=name,
            short=short,
        )


        game_start_event_game_variant.additional_properties = d
        return game_start_event_game_variant

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
