from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_puzzle_dashboard_response_200_themes_additional_property_results import ApiPuzzleDashboardResponse200ThemesAdditionalPropertyResults





T = TypeVar("T", bound="ApiPuzzleDashboardResponse200ThemesAdditionalProperty")



@_attrs_define
class ApiPuzzleDashboardResponse200ThemesAdditionalProperty:
    """ 
        Attributes:
            results (ApiPuzzleDashboardResponse200ThemesAdditionalPropertyResults):
            theme (str):
     """

    results: 'ApiPuzzleDashboardResponse200ThemesAdditionalPropertyResults'
    theme: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_puzzle_dashboard_response_200_themes_additional_property_results import ApiPuzzleDashboardResponse200ThemesAdditionalPropertyResults
        results = self.results.to_dict()

        theme = self.theme


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "results": results,
            "theme": theme,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_puzzle_dashboard_response_200_themes_additional_property_results import ApiPuzzleDashboardResponse200ThemesAdditionalPropertyResults
        d = dict(src_dict)
        results = ApiPuzzleDashboardResponse200ThemesAdditionalPropertyResults.from_dict(d.pop("results"))




        theme = d.pop("theme")

        api_puzzle_dashboard_response_200_themes_additional_property = cls(
            results=results,
            theme=theme,
        )


        api_puzzle_dashboard_response_200_themes_additional_property.additional_properties = d
        return api_puzzle_dashboard_response_200_themes_additional_property

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
