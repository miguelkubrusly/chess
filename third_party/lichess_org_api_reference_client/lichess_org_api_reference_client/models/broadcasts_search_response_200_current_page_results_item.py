from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcasts_search_response_200_current_page_results_item_tour import BroadcastsSearchResponse200CurrentPageResultsItemTour
  from ..models.broadcasts_search_response_200_current_page_results_item_round import BroadcastsSearchResponse200CurrentPageResultsItemRound





T = TypeVar("T", bound="BroadcastsSearchResponse200CurrentPageResultsItem")



@_attrs_define
class BroadcastsSearchResponse200CurrentPageResultsItem:
    """ 
        Attributes:
            group (Union[Unset, str]):
            tour (Union[Unset, BroadcastsSearchResponse200CurrentPageResultsItemTour]):
            round_ (Union[Unset, BroadcastsSearchResponse200CurrentPageResultsItemRound]):
     """

    group: Union[Unset, str] = UNSET
    tour: Union[Unset, 'BroadcastsSearchResponse200CurrentPageResultsItemTour'] = UNSET
    round_: Union[Unset, 'BroadcastsSearchResponse200CurrentPageResultsItemRound'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcasts_search_response_200_current_page_results_item_tour import BroadcastsSearchResponse200CurrentPageResultsItemTour
        from ..models.broadcasts_search_response_200_current_page_results_item_round import BroadcastsSearchResponse200CurrentPageResultsItemRound
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
        from ..models.broadcasts_search_response_200_current_page_results_item_tour import BroadcastsSearchResponse200CurrentPageResultsItemTour
        from ..models.broadcasts_search_response_200_current_page_results_item_round import BroadcastsSearchResponse200CurrentPageResultsItemRound
        d = dict(src_dict)
        group = d.pop("group", UNSET)

        _tour = d.pop("tour", UNSET)
        tour: Union[Unset, BroadcastsSearchResponse200CurrentPageResultsItemTour]
        if isinstance(_tour,  Unset):
            tour = UNSET
        else:
            tour = BroadcastsSearchResponse200CurrentPageResultsItemTour.from_dict(_tour)




        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, BroadcastsSearchResponse200CurrentPageResultsItemRound]
        if isinstance(_round_,  Unset):
            round_ = UNSET
        else:
            round_ = BroadcastsSearchResponse200CurrentPageResultsItemRound.from_dict(_round_)




        broadcasts_search_response_200_current_page_results_item = cls(
            group=group,
            tour=tour,
            round_=round_,
        )


        broadcasts_search_response_200_current_page_results_item.additional_properties = d
        return broadcasts_search_response_200_current_page_results_item

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
