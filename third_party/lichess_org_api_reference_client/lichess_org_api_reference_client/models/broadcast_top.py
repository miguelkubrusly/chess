from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_top_active_item import BroadcastTopActiveItem
  from ..models.broadcast_top_upcoming_item import BroadcastTopUpcomingItem
  from ..models.broadcast_top_past import BroadcastTopPast





T = TypeVar("T", bound="BroadcastTop")



@_attrs_define
class BroadcastTop:
    """ 
        Attributes:
            active (Union[Unset, list['BroadcastTopActiveItem']]):
            upcoming (Union[Unset, list['BroadcastTopUpcomingItem']]):
            past (Union[Unset, BroadcastTopPast]):
     """

    active: Union[Unset, list['BroadcastTopActiveItem']] = UNSET
    upcoming: Union[Unset, list['BroadcastTopUpcomingItem']] = UNSET
    past: Union[Unset, 'BroadcastTopPast'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_top_active_item import BroadcastTopActiveItem
        from ..models.broadcast_top_upcoming_item import BroadcastTopUpcomingItem
        from ..models.broadcast_top_past import BroadcastTopPast
        active: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.active, Unset):
            active = []
            for active_item_data in self.active:
                active_item = active_item_data.to_dict()
                active.append(active_item)



        upcoming: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.upcoming, Unset):
            upcoming = []
            for upcoming_item_data in self.upcoming:
                upcoming_item = upcoming_item_data.to_dict()
                upcoming.append(upcoming_item)



        past: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.past, Unset):
            past = self.past.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if active is not UNSET:
            field_dict["active"] = active
        if upcoming is not UNSET:
            field_dict["upcoming"] = upcoming
        if past is not UNSET:
            field_dict["past"] = past

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_top_active_item import BroadcastTopActiveItem
        from ..models.broadcast_top_upcoming_item import BroadcastTopUpcomingItem
        from ..models.broadcast_top_past import BroadcastTopPast
        d = dict(src_dict)
        active = []
        _active = d.pop("active", UNSET)
        for active_item_data in (_active or []):
            active_item = BroadcastTopActiveItem.from_dict(active_item_data)



            active.append(active_item)


        upcoming = []
        _upcoming = d.pop("upcoming", UNSET)
        for upcoming_item_data in (_upcoming or []):
            upcoming_item = BroadcastTopUpcomingItem.from_dict(upcoming_item_data)



            upcoming.append(upcoming_item)


        _past = d.pop("past", UNSET)
        past: Union[Unset, BroadcastTopPast]
        if isinstance(_past,  Unset):
            past = UNSET
        else:
            past = BroadcastTopPast.from_dict(_past)




        broadcast_top = cls(
            active=active,
            upcoming=upcoming,
            past=past,
        )


        broadcast_top.additional_properties = d
        return broadcast_top

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
