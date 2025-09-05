from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcasts_top_response_200_past_current_page_results_item import BroadcastsTopResponse200PastCurrentPageResultsItem





T = TypeVar("T", bound="BroadcastsTopResponse200Past")



@_attrs_define
class BroadcastsTopResponse200Past:
    """ 
        Attributes:
            current_page (Union[Unset, int]):  Example: 4.
            max_per_page (Union[Unset, int]):  Example: 20.
            current_page_results (Union[Unset, list['BroadcastsTopResponse200PastCurrentPageResultsItem']]):
            previous_page (Union[None, Unset, float]):  Example: 3.
            next_page (Union[None, Unset, float]):  Example: 5.
     """

    current_page: Union[Unset, int] = UNSET
    max_per_page: Union[Unset, int] = UNSET
    current_page_results: Union[Unset, list['BroadcastsTopResponse200PastCurrentPageResultsItem']] = UNSET
    previous_page: Union[None, Unset, float] = UNSET
    next_page: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcasts_top_response_200_past_current_page_results_item import BroadcastsTopResponse200PastCurrentPageResultsItem
        current_page = self.current_page

        max_per_page = self.max_per_page

        current_page_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.current_page_results, Unset):
            current_page_results = []
            for current_page_results_item_data in self.current_page_results:
                current_page_results_item = current_page_results_item_data.to_dict()
                current_page_results.append(current_page_results_item)



        previous_page: Union[None, Unset, float]
        if isinstance(self.previous_page, Unset):
            previous_page = UNSET
        else:
            previous_page = self.previous_page

        next_page: Union[None, Unset, float]
        if isinstance(self.next_page, Unset):
            next_page = UNSET
        else:
            next_page = self.next_page


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if max_per_page is not UNSET:
            field_dict["maxPerPage"] = max_per_page
        if current_page_results is not UNSET:
            field_dict["currentPageResults"] = current_page_results
        if previous_page is not UNSET:
            field_dict["previousPage"] = previous_page
        if next_page is not UNSET:
            field_dict["nextPage"] = next_page

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcasts_top_response_200_past_current_page_results_item import BroadcastsTopResponse200PastCurrentPageResultsItem
        d = dict(src_dict)
        current_page = d.pop("currentPage", UNSET)

        max_per_page = d.pop("maxPerPage", UNSET)

        current_page_results = []
        _current_page_results = d.pop("currentPageResults", UNSET)
        for current_page_results_item_data in (_current_page_results or []):
            current_page_results_item = BroadcastsTopResponse200PastCurrentPageResultsItem.from_dict(current_page_results_item_data)



            current_page_results.append(current_page_results_item)


        def _parse_previous_page(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        previous_page = _parse_previous_page(d.pop("previousPage", UNSET))


        def _parse_next_page(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        next_page = _parse_next_page(d.pop("nextPage", UNSET))


        broadcasts_top_response_200_past = cls(
            current_page=current_page,
            max_per_page=max_per_page,
            current_page_results=current_page_results,
            previous_page=previous_page,
            next_page=next_page,
        )


        broadcasts_top_response_200_past.additional_properties = d
        return broadcasts_top_response_200_past

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
