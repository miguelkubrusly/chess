from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.broadcast_by_user_tour import BroadcastByUserTour





T = TypeVar("T", bound="BroadcastByUser")



@_attrs_define
class BroadcastByUser:
    """ 
        Attributes:
            tour (BroadcastByUserTour):
     """

    tour: 'BroadcastByUserTour'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_by_user_tour import BroadcastByUserTour
        tour = self.tour.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tour": tour,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_by_user_tour import BroadcastByUserTour
        d = dict(src_dict)
        tour = BroadcastByUserTour.from_dict(d.pop("tour"))




        broadcast_by_user = cls(
            tour=tour,
        )


        broadcast_by_user.additional_properties = d
        return broadcast_by_user

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
