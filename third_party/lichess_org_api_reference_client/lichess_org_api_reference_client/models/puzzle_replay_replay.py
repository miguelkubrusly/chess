from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PuzzleReplayReplay")



@_attrs_define
class PuzzleReplayReplay:
    """ 
        Attributes:
            days (float):
            theme (str):
            nb (float):
            remaining (list[str]):
     """

    days: float
    theme: str
    nb: float
    remaining: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        days = self.days

        theme = self.theme

        nb = self.nb

        remaining = self.remaining




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "days": days,
            "theme": theme,
            "nb": nb,
            "remaining": remaining,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days = d.pop("days")

        theme = d.pop("theme")

        nb = d.pop("nb")

        remaining = cast(list[str], d.pop("remaining"))


        puzzle_replay_replay = cls(
            days=days,
            theme=theme,
            nb=nb,
            remaining=remaining,
        )


        puzzle_replay_replay.additional_properties = d
        return puzzle_replay_replay

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
