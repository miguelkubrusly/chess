from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.study_import_pgn_chapters_chapters_item import StudyImportPgnChaptersChaptersItem





T = TypeVar("T", bound="StudyImportPgnChapters")



@_attrs_define
class StudyImportPgnChapters:
    """ 
        Example:
            {'chapters': [{'id': 'iBjmYBya', 'name': 'test 2', 'players': [{'name': 'Carlsen, Magnus', 'rating': 2837},
                {'name': 'Chadaev, Nikolay', 'rating': 2580}], 'status': '1-0'}]}

        Attributes:
            chapters (Union[Unset, list['StudyImportPgnChaptersChaptersItem']]):
     """

    chapters: Union[Unset, list['StudyImportPgnChaptersChaptersItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.study_import_pgn_chapters_chapters_item import StudyImportPgnChaptersChaptersItem
        chapters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.chapters, Unset):
            chapters = []
            for chapters_item_data in self.chapters:
                chapters_item = chapters_item_data.to_dict()
                chapters.append(chapters_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chapters is not UNSET:
            field_dict["chapters"] = chapters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.study_import_pgn_chapters_chapters_item import StudyImportPgnChaptersChaptersItem
        d = dict(src_dict)
        chapters = []
        _chapters = d.pop("chapters", UNSET)
        for chapters_item_data in (_chapters or []):
            chapters_item = StudyImportPgnChaptersChaptersItem.from_dict(chapters_item_data)



            chapters.append(chapters_item)


        study_import_pgn_chapters = cls(
            chapters=chapters,
        )


        study_import_pgn_chapters.additional_properties = d
        return study_import_pgn_chapters

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
