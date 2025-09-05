from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcasts_top_response_200_past import BroadcastsTopResponse200Past
  from ..models.broadcasts_top_response_200_upcoming_item import BroadcastsTopResponse200UpcomingItem
  from ..models.broadcasts_top_response_200_active_item import BroadcastsTopResponse200ActiveItem





T = TypeVar("T", bound="BroadcastsTopResponse200")



@_attrs_define
class BroadcastsTopResponse200:
    """ 
        Attributes:
            active (Union[Unset, list['BroadcastsTopResponse200ActiveItem']]):
            upcoming (Union[Unset, list['BroadcastsTopResponse200UpcomingItem']]):
            past (Union[Unset, BroadcastsTopResponse200Past]):
     """

    active: Union[Unset, list['BroadcastsTopResponse200ActiveItem']] = UNSET
    upcoming: Union[Unset, list['BroadcastsTopResponse200UpcomingItem']] = UNSET
    past: Union[Unset, 'BroadcastsTopResponse200Past'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcasts_top_response_200_past import BroadcastsTopResponse200Past
        from ..models.broadcasts_top_response_200_upcoming_item import BroadcastsTopResponse200UpcomingItem
        from ..models.broadcasts_top_response_200_active_item import BroadcastsTopResponse200ActiveItem
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
        from ..models.broadcasts_top_response_200_past import BroadcastsTopResponse200Past
        from ..models.broadcasts_top_response_200_upcoming_item import BroadcastsTopResponse200UpcomingItem
        from ..models.broadcasts_top_response_200_active_item import BroadcastsTopResponse200ActiveItem
        d = dict(src_dict)
        active = []
        _active = d.pop("active", UNSET)
        for active_item_data in (_active or []):
            active_item = BroadcastsTopResponse200ActiveItem.from_dict(active_item_data)



            active.append(active_item)


        upcoming = []
        _upcoming = d.pop("upcoming", UNSET)
        for upcoming_item_data in (_upcoming or []):
            upcoming_item = BroadcastsTopResponse200UpcomingItem.from_dict(upcoming_item_data)



            upcoming.append(upcoming_item)


        _past = d.pop("past", UNSET)
        past: Union[Unset, BroadcastsTopResponse200Past]
        if isinstance(_past,  Unset):
            past = UNSET
        else:
            past = BroadcastsTopResponse200Past.from_dict(_past)




        broadcasts_top_response_200 = cls(
            active=active,
            upcoming=upcoming,
            past=past,
        )


        broadcasts_top_response_200.additional_properties = d
        return broadcasts_top_response_200

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
