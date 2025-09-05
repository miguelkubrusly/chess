from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.puzzle_dashboard_themes_additional_property_results import PuzzleDashboardThemesAdditionalPropertyResults





T = TypeVar("T", bound="PuzzleDashboardThemesAdditionalProperty")



@_attrs_define
class PuzzleDashboardThemesAdditionalProperty:
    """ 
        Attributes:
            results (PuzzleDashboardThemesAdditionalPropertyResults):
            theme (str):
     """

    results: 'PuzzleDashboardThemesAdditionalPropertyResults'
    theme: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.puzzle_dashboard_themes_additional_property_results import PuzzleDashboardThemesAdditionalPropertyResults
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
        from ..models.puzzle_dashboard_themes_additional_property_results import PuzzleDashboardThemesAdditionalPropertyResults
        d = dict(src_dict)
        results = PuzzleDashboardThemesAdditionalPropertyResults.from_dict(d.pop("results"))




        theme = d.pop("theme")

        puzzle_dashboard_themes_additional_property = cls(
            results=results,
            theme=theme,
        )


        puzzle_dashboard_themes_additional_property.additional_properties = d
        return puzzle_dashboard_themes_additional_property

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
