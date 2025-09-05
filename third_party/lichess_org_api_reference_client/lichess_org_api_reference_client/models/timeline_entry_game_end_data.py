from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.timeline_entry_game_end_data_perf import TimelineEntryGameEndDataPerf






T = TypeVar("T", bound="TimelineEntryGameEndData")



@_attrs_define
class TimelineEntryGameEndData:
    """ 
        Attributes:
            full_id (str):
            opponent (str):
            win (bool):
            perf (TimelineEntryGameEndDataPerf):
     """

    full_id: str
    opponent: str
    win: bool
    perf: TimelineEntryGameEndDataPerf
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        full_id = self.full_id

        opponent = self.opponent

        win = self.win

        perf = self.perf.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fullId": full_id,
            "opponent": opponent,
            "win": win,
            "perf": perf,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_id = d.pop("fullId")

        opponent = d.pop("opponent")

        win = d.pop("win")

        perf = TimelineEntryGameEndDataPerf(d.pop("perf"))




        timeline_entry_game_end_data = cls(
            full_id=full_id,
            opponent=opponent,
            win=win,
            perf=perf,
        )


        timeline_entry_game_end_data.additional_properties = d
        return timeline_entry_game_end_data

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
