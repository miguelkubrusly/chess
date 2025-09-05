from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.fide_player_title import FIDEPlayerTitle
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="FIDEPlayer")



@_attrs_define
class FIDEPlayer:
    """ 
        Attributes:
            id (int):
            name (str):
            federation (str):
            title (Union[Unset, FIDEPlayerTitle]): only appears if the user is a titled player or a bot user
            year (Union[None, Unset, float]):
            inactive (Union[Unset, int]):
            standard (Union[Unset, int]):
            rapid (Union[Unset, int]):
            blitz (Union[Unset, int]):
     """

    id: int
    name: str
    federation: str
    title: Union[Unset, FIDEPlayerTitle] = UNSET
    year: Union[None, Unset, float] = UNSET
    inactive: Union[Unset, int] = UNSET
    standard: Union[Unset, int] = UNSET
    rapid: Union[Unset, int] = UNSET
    blitz: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        federation = self.federation

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value


        year: Union[None, Unset, float]
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        inactive = self.inactive

        standard = self.standard

        rapid = self.rapid

        blitz = self.blitz


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "federation": federation,
        })
        if title is not UNSET:
            field_dict["title"] = title
        if year is not UNSET:
            field_dict["year"] = year
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if standard is not UNSET:
            field_dict["standard"] = standard
        if rapid is not UNSET:
            field_dict["rapid"] = rapid
        if blitz is not UNSET:
            field_dict["blitz"] = blitz

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        federation = d.pop("federation")

        _title = d.pop("title", UNSET)
        title: Union[Unset, FIDEPlayerTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = FIDEPlayerTitle(_title)




        def _parse_year(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        year = _parse_year(d.pop("year", UNSET))


        inactive = d.pop("inactive", UNSET)

        standard = d.pop("standard", UNSET)

        rapid = d.pop("rapid", UNSET)

        blitz = d.pop("blitz", UNSET)

        fide_player = cls(
            id=id,
            name=name,
            federation=federation,
            title=title,
            year=year,
            inactive=inactive,
            standard=standard,
            rapid=rapid,
            blitz=blitz,
        )


        fide_player.additional_properties = d
        return fide_player

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
