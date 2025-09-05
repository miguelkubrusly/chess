from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.broadcast_my_round_round_custom_scoring_white import BroadcastMyRoundRoundCustomScoringWhite
  from ..models.broadcast_my_round_round_custom_scoring_black import BroadcastMyRoundRoundCustomScoringBlack





T = TypeVar("T", bound="BroadcastMyRoundRoundCustomScoring")



@_attrs_define
class BroadcastMyRoundRoundCustomScoring:
    """ Scoring overrides for wins or draws.

        Attributes:
            white (BroadcastMyRoundRoundCustomScoringWhite):
            black (BroadcastMyRoundRoundCustomScoringBlack):
     """

    white: 'BroadcastMyRoundRoundCustomScoringWhite'
    black: 'BroadcastMyRoundRoundCustomScoringBlack'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_my_round_round_custom_scoring_white import BroadcastMyRoundRoundCustomScoringWhite
        from ..models.broadcast_my_round_round_custom_scoring_black import BroadcastMyRoundRoundCustomScoringBlack
        white = self.white.to_dict()

        black = self.black.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "white": white,
            "black": black,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_my_round_round_custom_scoring_white import BroadcastMyRoundRoundCustomScoringWhite
        from ..models.broadcast_my_round_round_custom_scoring_black import BroadcastMyRoundRoundCustomScoringBlack
        d = dict(src_dict)
        white = BroadcastMyRoundRoundCustomScoringWhite.from_dict(d.pop("white"))




        black = BroadcastMyRoundRoundCustomScoringBlack.from_dict(d.pop("black"))




        broadcast_my_round_round_custom_scoring = cls(
            white=white,
            black=black,
        )


        broadcast_my_round_round_custom_scoring.additional_properties = d
        return broadcast_my_round_round_custom_scoring

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
