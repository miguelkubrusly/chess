from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, Union, cast
from typing import Union






T = TypeVar("T", bound="ArenaTournamentCustomPosition")



@_attrs_define
class ArenaTournamentCustomPosition:
    """ 
        Attributes:
            name (Union[Literal['Custom position'], Unset]):
            fen (Union[Unset, str]):  Example: rnbq1bnr/ppppkppp/8/4p3/4P3/8/PPPPKPPP/RNBQ1BNR w - - 2 3.
     """

    name: Union[Literal['Custom position'], Unset] = UNSET
    fen: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        fen = self.fen


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if fen is not UNSET:
            field_dict["fen"] = fen

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = cast(Union[Literal['Custom position'], Unset] , d.pop("name", UNSET))
        if name != 'Custom position'and not isinstance(name, Unset):
            raise ValueError(f"name must match const 'Custom position', got '{name}'")

        fen = d.pop("fen", UNSET)

        arena_tournament_custom_position = cls(
            name=name,
            fen=fen,
        )


        arena_tournament_custom_position.additional_properties = d
        return arena_tournament_custom_position

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
