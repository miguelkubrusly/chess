from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_puzzle_dashboard_response_200_global import ApiPuzzleDashboardResponse200Global
  from ..models.api_puzzle_dashboard_response_200_themes import ApiPuzzleDashboardResponse200Themes





T = TypeVar("T", bound="ApiPuzzleDashboardResponse200")



@_attrs_define
class ApiPuzzleDashboardResponse200:
    """ 
        Attributes:
            days (int):
            global_ (ApiPuzzleDashboardResponse200Global):
            themes (ApiPuzzleDashboardResponse200Themes):
     """

    days: int
    global_: 'ApiPuzzleDashboardResponse200Global'
    themes: 'ApiPuzzleDashboardResponse200Themes'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_puzzle_dashboard_response_200_global import ApiPuzzleDashboardResponse200Global
        from ..models.api_puzzle_dashboard_response_200_themes import ApiPuzzleDashboardResponse200Themes
        days = self.days

        global_ = self.global_.to_dict()

        themes = self.themes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "days": days,
            "global": global_,
            "themes": themes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_puzzle_dashboard_response_200_global import ApiPuzzleDashboardResponse200Global
        from ..models.api_puzzle_dashboard_response_200_themes import ApiPuzzleDashboardResponse200Themes
        d = dict(src_dict)
        days = d.pop("days")

        global_ = ApiPuzzleDashboardResponse200Global.from_dict(d.pop("global"))




        themes = ApiPuzzleDashboardResponse200Themes.from_dict(d.pop("themes"))




        api_puzzle_dashboard_response_200 = cls(
            days=days,
            global_=global_,
            themes=themes,
        )


        api_puzzle_dashboard_response_200.additional_properties = d
        return api_puzzle_dashboard_response_200

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
