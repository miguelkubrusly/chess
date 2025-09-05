from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.broadcast_round_create_response_200_study import BroadcastRoundCreateResponse200Study
  from ..models.broadcast_round_create_response_200_round import BroadcastRoundCreateResponse200Round
  from ..models.broadcast_round_create_response_200_tour import BroadcastRoundCreateResponse200Tour





T = TypeVar("T", bound="BroadcastRoundCreateResponse200")



@_attrs_define
class BroadcastRoundCreateResponse200:
    """ 
        Attributes:
            round_ (BroadcastRoundCreateResponse200Round):
            tour (BroadcastRoundCreateResponse200Tour):
            study (BroadcastRoundCreateResponse200Study):
     """

    round_: 'BroadcastRoundCreateResponse200Round'
    tour: 'BroadcastRoundCreateResponse200Tour'
    study: 'BroadcastRoundCreateResponse200Study'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_round_create_response_200_study import BroadcastRoundCreateResponse200Study
        from ..models.broadcast_round_create_response_200_round import BroadcastRoundCreateResponse200Round
        from ..models.broadcast_round_create_response_200_tour import BroadcastRoundCreateResponse200Tour
        round_ = self.round_.to_dict()

        tour = self.tour.to_dict()

        study = self.study.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "round": round_,
            "tour": tour,
            "study": study,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_round_create_response_200_study import BroadcastRoundCreateResponse200Study
        from ..models.broadcast_round_create_response_200_round import BroadcastRoundCreateResponse200Round
        from ..models.broadcast_round_create_response_200_tour import BroadcastRoundCreateResponse200Tour
        d = dict(src_dict)
        round_ = BroadcastRoundCreateResponse200Round.from_dict(d.pop("round"))




        tour = BroadcastRoundCreateResponse200Tour.from_dict(d.pop("tour"))




        study = BroadcastRoundCreateResponse200Study.from_dict(d.pop("study"))




        broadcast_round_create_response_200 = cls(
            round_=round_,
            tour=tour,
            study=study,
        )


        broadcast_round_create_response_200.additional_properties = d
        return broadcast_round_create_response_200

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
