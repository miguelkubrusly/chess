from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.broadcasts_by_user_response_200_current_page_results_item import BroadcastsByUserResponse200CurrentPageResultsItem





T = TypeVar("T", bound="BroadcastsByUserResponse200")



@_attrs_define
class BroadcastsByUserResponse200:
    """ 
        Attributes:
            current_page (float):  Example: 4.
            max_per_page (float):  Example: 15.
            current_page_results (list['BroadcastsByUserResponse200CurrentPageResultsItem']):
            nb_results (float):  Example: 205194.
            previous_page (Union[None, float]):  Example: 3.
            next_page (Union[None, float]):  Example: 5.
            nb_pages (float):  Example: 13680.
     """

    current_page: float
    max_per_page: float
    current_page_results: list['BroadcastsByUserResponse200CurrentPageResultsItem']
    nb_results: float
    previous_page: Union[None, float]
    next_page: Union[None, float]
    nb_pages: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcasts_by_user_response_200_current_page_results_item import BroadcastsByUserResponse200CurrentPageResultsItem
        current_page = self.current_page

        max_per_page = self.max_per_page

        current_page_results = []
        for current_page_results_item_data in self.current_page_results:
            current_page_results_item = current_page_results_item_data.to_dict()
            current_page_results.append(current_page_results_item)



        nb_results = self.nb_results

        previous_page: Union[None, float]
        previous_page = self.previous_page

        next_page: Union[None, float]
        next_page = self.next_page

        nb_pages = self.nb_pages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "currentPage": current_page,
            "maxPerPage": max_per_page,
            "currentPageResults": current_page_results,
            "nbResults": nb_results,
            "previousPage": previous_page,
            "nextPage": next_page,
            "nbPages": nb_pages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcasts_by_user_response_200_current_page_results_item import BroadcastsByUserResponse200CurrentPageResultsItem
        d = dict(src_dict)
        current_page = d.pop("currentPage")

        max_per_page = d.pop("maxPerPage")

        current_page_results = []
        _current_page_results = d.pop("currentPageResults")
        for current_page_results_item_data in (_current_page_results):
            current_page_results_item = BroadcastsByUserResponse200CurrentPageResultsItem.from_dict(current_page_results_item_data)



            current_page_results.append(current_page_results_item)


        nb_results = d.pop("nbResults")

        def _parse_previous_page(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        previous_page = _parse_previous_page(d.pop("previousPage"))


        def _parse_next_page(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        next_page = _parse_next_page(d.pop("nextPage"))


        nb_pages = d.pop("nbPages")

        broadcasts_by_user_response_200 = cls(
            current_page=current_page,
            max_per_page=max_per_page,
            current_page_results=current_page_results,
            nb_results=nb_results,
            previous_page=previous_page,
            next_page=next_page,
            nb_pages=nb_pages,
        )


        broadcasts_by_user_response_200.additional_properties = d
        return broadcasts_by_user_response_200

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
