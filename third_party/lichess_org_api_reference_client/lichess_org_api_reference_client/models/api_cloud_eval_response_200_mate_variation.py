from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ApiCloudEvalResponse200MateVariation")



@_attrs_define
class ApiCloudEvalResponse200MateVariation:
    """ 
        Attributes:
            mate (int): Evaluation in moves to mate, from White's point of view
            moves (str): Variation in UCI notation
     """

    mate: int
    moves: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        mate = self.mate

        moves = self.moves


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mate": mate,
            "moves": moves,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mate = d.pop("mate")

        moves = d.pop("moves")

        api_cloud_eval_response_200_mate_variation = cls(
            mate=mate,
            moves=moves,
        )


        api_cloud_eval_response_200_mate_variation.additional_properties = d
        return api_cloud_eval_response_200_mate_variation

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
