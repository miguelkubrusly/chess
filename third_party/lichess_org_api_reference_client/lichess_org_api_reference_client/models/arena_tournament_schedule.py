from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ArenaTournamentSchedule")



@_attrs_define
class ArenaTournamentSchedule:
    """ 
        Attributes:
            freq (Union[Unset, str]):
            speed (Union[Unset, str]):
     """

    freq: Union[Unset, str] = UNSET
    speed: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        freq = self.freq

        speed = self.speed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if freq is not UNSET:
            field_dict["freq"] = freq
        if speed is not UNSET:
            field_dict["speed"] = speed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        freq = d.pop("freq", UNSET)

        speed = d.pop("speed", UNSET)

        arena_tournament_schedule = cls(
            freq=freq,
            speed=speed,
        )


        arena_tournament_schedule.additional_properties = d
        return arena_tournament_schedule

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
