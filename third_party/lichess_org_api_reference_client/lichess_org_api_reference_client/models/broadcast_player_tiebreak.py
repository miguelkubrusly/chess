from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.broadcast_player_tiebreak_extended_code import BroadcastPlayerTiebreakExtendedCode
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="BroadcastPlayerTiebreak")



@_attrs_define
class BroadcastPlayerTiebreak:
    """ 
        Attributes:
            extended_code (Union[Unset, BroadcastPlayerTiebreakExtendedCode]): Extended tiebreak code
            description (Union[Unset, str]):  Example: Buchholz Cut 1.
            points (Union[Unset, float]):  Example: 45.5.
     """

    extended_code: Union[Unset, BroadcastPlayerTiebreakExtendedCode] = UNSET
    description: Union[Unset, str] = UNSET
    points: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        extended_code: Union[Unset, str] = UNSET
        if not isinstance(self.extended_code, Unset):
            extended_code = self.extended_code.value


        description = self.description

        points = self.points


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if extended_code is not UNSET:
            field_dict["extendedCode"] = extended_code
        if description is not UNSET:
            field_dict["description"] = description
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _extended_code = d.pop("extendedCode", UNSET)
        extended_code: Union[Unset, BroadcastPlayerTiebreakExtendedCode]
        if isinstance(_extended_code,  Unset):
            extended_code = UNSET
        else:
            extended_code = BroadcastPlayerTiebreakExtendedCode(_extended_code)




        description = d.pop("description", UNSET)

        points = d.pop("points", UNSET)

        broadcast_player_tiebreak = cls(
            extended_code=extended_code,
            description=description,
            points=points,
        )


        broadcast_player_tiebreak.additional_properties = d
        return broadcast_player_tiebreak

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
