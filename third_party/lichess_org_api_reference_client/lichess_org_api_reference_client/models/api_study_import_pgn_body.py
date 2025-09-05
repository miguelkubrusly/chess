from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_study_import_pgn_body_orientation import ApiStudyImportPGNBodyOrientation
from ..models.api_study_import_pgn_body_variant import ApiStudyImportPGNBodyVariant
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiStudyImportPGNBody")



@_attrs_define
class ApiStudyImportPGNBody:
    """ 
        Attributes:
            pgn (str): PGN to import. Can contain multiple games separated by 2 or more newlines.
            name (Union[Unset, str]): Name of the new chapter.
                If not specified, or if multiple chapters are created, the names will be inferred from the PGN tags.
            orientation (Union[Unset, ApiStudyImportPGNBodyOrientation]): Default board orientation. Default:
                ApiStudyImportPGNBodyOrientation.WHITE.
            variant (Union[Unset, ApiStudyImportPGNBodyVariant]):  Default: ApiStudyImportPGNBodyVariant.STANDARD. Example:
                standard.
     """

    pgn: str
    name: Union[Unset, str] = UNSET
    orientation: Union[Unset, ApiStudyImportPGNBodyOrientation] = ApiStudyImportPGNBodyOrientation.WHITE
    variant: Union[Unset, ApiStudyImportPGNBodyVariant] = ApiStudyImportPGNBodyVariant.STANDARD
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        pgn = self.pgn

        name = self.name

        orientation: Union[Unset, str] = UNSET
        if not isinstance(self.orientation, Unset):
            orientation = self.orientation.value


        variant: Union[Unset, str] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "pgn": pgn,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pgn = d.pop("pgn")

        name = d.pop("name", UNSET)

        _orientation = d.pop("orientation", UNSET)
        orientation: Union[Unset, ApiStudyImportPGNBodyOrientation]
        if isinstance(_orientation,  Unset):
            orientation = UNSET
        else:
            orientation = ApiStudyImportPGNBodyOrientation(_orientation)




        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, ApiStudyImportPGNBodyVariant]
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = ApiStudyImportPGNBodyVariant(_variant)




        api_study_import_pgn_body = cls(
            pgn=pgn,
            name=name,
            orientation=orientation,
            variant=variant,
        )


        api_study_import_pgn_body.additional_properties = d
        return api_study_import_pgn_body

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
