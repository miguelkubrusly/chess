from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_top_active_item_round import BroadcastTopActiveItemRound
  from ..models.broadcast_top_active_item_tour import BroadcastTopActiveItemTour





T = TypeVar("T", bound="BroadcastTopActiveItem")



@_attrs_define
class BroadcastTopActiveItem:
    """ 
        Attributes:
            group (Union[Unset, str]):
            tour (Union[Unset, BroadcastTopActiveItemTour]):
            round_ (Union[Unset, BroadcastTopActiveItemRound]):
     """

    group: Union[Unset, str] = UNSET
    tour: Union[Unset, 'BroadcastTopActiveItemTour'] = UNSET
    round_: Union[Unset, 'BroadcastTopActiveItemRound'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_top_active_item_round import BroadcastTopActiveItemRound
        from ..models.broadcast_top_active_item_tour import BroadcastTopActiveItemTour
        group = self.group

        tour: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tour, Unset):
            tour = self.tour.to_dict()

        round_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.round_, Unset):
            round_ = self.round_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if group is not UNSET:
            field_dict["group"] = group
        if tour is not UNSET:
            field_dict["tour"] = tour
        if round_ is not UNSET:
            field_dict["round"] = round_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_top_active_item_round import BroadcastTopActiveItemRound
        from ..models.broadcast_top_active_item_tour import BroadcastTopActiveItemTour
        d = dict(src_dict)
        group = d.pop("group", UNSET)

        _tour = d.pop("tour", UNSET)
        tour: Union[Unset, BroadcastTopActiveItemTour]
        if isinstance(_tour,  Unset):
            tour = UNSET
        else:
            tour = BroadcastTopActiveItemTour.from_dict(_tour)




        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, BroadcastTopActiveItemRound]
        if isinstance(_round_,  Unset):
            round_ = UNSET
        else:
            round_ = BroadcastTopActiveItemRound.from_dict(_round_)




        broadcast_top_active_item = cls(
            group=group,
            tour=tour,
            round_=round_,
        )


        broadcast_top_active_item.additional_properties = d
        return broadcast_top_active_item

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
