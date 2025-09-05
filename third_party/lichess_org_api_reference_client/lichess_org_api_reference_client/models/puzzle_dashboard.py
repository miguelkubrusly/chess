from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.puzzle_dashboard_themes import PuzzleDashboardThemes
  from ..models.puzzle_dashboard_global import PuzzleDashboardGlobal





T = TypeVar("T", bound="PuzzleDashboard")



@_attrs_define
class PuzzleDashboard:
    """ 
        Attributes:
            days (int):
            global_ (PuzzleDashboardGlobal):
            themes (PuzzleDashboardThemes):
     """

    days: int
    global_: 'PuzzleDashboardGlobal'
    themes: 'PuzzleDashboardThemes'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.puzzle_dashboard_themes import PuzzleDashboardThemes
        from ..models.puzzle_dashboard_global import PuzzleDashboardGlobal
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
        from ..models.puzzle_dashboard_themes import PuzzleDashboardThemes
        from ..models.puzzle_dashboard_global import PuzzleDashboardGlobal
        d = dict(src_dict)
        days = d.pop("days")

        global_ = PuzzleDashboardGlobal.from_dict(d.pop("global"))




        themes = PuzzleDashboardThemes.from_dict(d.pop("themes"))




        puzzle_dashboard = cls(
            days=days,
            global_=global_,
            themes=themes,
        )


        puzzle_dashboard.additional_properties = d
        return puzzle_dashboard

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
