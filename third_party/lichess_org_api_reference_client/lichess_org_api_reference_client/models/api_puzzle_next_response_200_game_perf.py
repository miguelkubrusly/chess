from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_puzzle_next_response_200_game_perf_key import ApiPuzzleNextResponse200GamePerfKey






T = TypeVar("T", bound="ApiPuzzleNextResponse200GamePerf")



@_attrs_define
class ApiPuzzleNextResponse200GamePerf:
    """ 
        Attributes:
            key (ApiPuzzleNextResponse200GamePerfKey):
            name (str):
     """

    key: ApiPuzzleNextResponse200GamePerfKey
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = ApiPuzzleNextResponse200GamePerfKey(d.pop("key"))




        name = d.pop("name")

        api_puzzle_next_response_200_game_perf = cls(
            key=key,
            name=name,
        )


        api_puzzle_next_response_200_game_perf.additional_properties = d
        return api_puzzle_next_response_200_game_perf

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
