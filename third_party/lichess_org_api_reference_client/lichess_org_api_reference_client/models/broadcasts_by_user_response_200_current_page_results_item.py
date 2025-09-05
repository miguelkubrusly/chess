from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.broadcasts_by_user_response_200_current_page_results_item_tour import BroadcastsByUserResponse200CurrentPageResultsItemTour





T = TypeVar("T", bound="BroadcastsByUserResponse200CurrentPageResultsItem")



@_attrs_define
class BroadcastsByUserResponse200CurrentPageResultsItem:
    """ 
        Attributes:
            tour (BroadcastsByUserResponse200CurrentPageResultsItemTour):
     """

    tour: 'BroadcastsByUserResponse200CurrentPageResultsItemTour'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcasts_by_user_response_200_current_page_results_item_tour import BroadcastsByUserResponse200CurrentPageResultsItemTour
        tour = self.tour.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tour": tour,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcasts_by_user_response_200_current_page_results_item_tour import BroadcastsByUserResponse200CurrentPageResultsItemTour
        d = dict(src_dict)
        tour = BroadcastsByUserResponse200CurrentPageResultsItemTour.from_dict(d.pop("tour"))




        broadcasts_by_user_response_200_current_page_results_item = cls(
            tour=tour,
        )


        broadcasts_by_user_response_200_current_page_results_item.additional_properties = d
        return broadcasts_by_user_response_200_current_page_results_item

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
