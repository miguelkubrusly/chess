from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="GameFullEventClock")



@_attrs_define
class GameFullEventClock:
    """ 
        Attributes:
            initial (Union[Unset, int]): Initial time in milliseconds
            increment (Union[Unset, int]): Increment time in milliseconds
     """

    initial: Union[Unset, int] = UNSET
    increment: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        initial = self.initial

        increment = self.increment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if initial is not UNSET:
            field_dict["initial"] = initial
        if increment is not UNSET:
            field_dict["increment"] = increment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        initial = d.pop("initial", UNSET)

        increment = d.pop("increment", UNSET)

        game_full_event_clock = cls(
            initial=initial,
            increment=increment,
        )


        game_full_event_clock.additional_properties = d
        return game_full_event_clock

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
