from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.broadcast_my_round_round import BroadcastMyRoundRound
  from ..models.broadcast_my_round_tour import BroadcastMyRoundTour
  from ..models.broadcast_my_round_study import BroadcastMyRoundStudy





T = TypeVar("T", bound="BroadcastMyRound")



@_attrs_define
class BroadcastMyRound:
    """ 
        Attributes:
            round_ (BroadcastMyRoundRound):
            tour (BroadcastMyRoundTour):
            study (BroadcastMyRoundStudy):
     """

    round_: 'BroadcastMyRoundRound'
    tour: 'BroadcastMyRoundTour'
    study: 'BroadcastMyRoundStudy'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_my_round_round import BroadcastMyRoundRound
        from ..models.broadcast_my_round_tour import BroadcastMyRoundTour
        from ..models.broadcast_my_round_study import BroadcastMyRoundStudy
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
        from ..models.broadcast_my_round_round import BroadcastMyRoundRound
        from ..models.broadcast_my_round_tour import BroadcastMyRoundTour
        from ..models.broadcast_my_round_study import BroadcastMyRoundStudy
        d = dict(src_dict)
        round_ = BroadcastMyRoundRound.from_dict(d.pop("round"))




        tour = BroadcastMyRoundTour.from_dict(d.pop("tour"))




        study = BroadcastMyRoundStudy.from_dict(d.pop("study"))




        broadcast_my_round = cls(
            round_=round_,
            tour=tour,
            study=study,
        )


        broadcast_my_round.additional_properties = d
        return broadcast_my_round

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
