from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.broadcast_round_round_custom_scoring_white import BroadcastRoundRoundCustomScoringWhite
  from ..models.broadcast_round_round_custom_scoring_black import BroadcastRoundRoundCustomScoringBlack





T = TypeVar("T", bound="BroadcastRoundRoundCustomScoring")



@_attrs_define
class BroadcastRoundRoundCustomScoring:
    """ Scoring overrides for wins or draws.

        Attributes:
            white (BroadcastRoundRoundCustomScoringWhite):
            black (BroadcastRoundRoundCustomScoringBlack):
     """

    white: 'BroadcastRoundRoundCustomScoringWhite'
    black: 'BroadcastRoundRoundCustomScoringBlack'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_round_round_custom_scoring_white import BroadcastRoundRoundCustomScoringWhite
        from ..models.broadcast_round_round_custom_scoring_black import BroadcastRoundRoundCustomScoringBlack
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
        from ..models.broadcast_round_round_custom_scoring_white import BroadcastRoundRoundCustomScoringWhite
        from ..models.broadcast_round_round_custom_scoring_black import BroadcastRoundRoundCustomScoringBlack
        d = dict(src_dict)
        white = BroadcastRoundRoundCustomScoringWhite.from_dict(d.pop("white"))




        black = BroadcastRoundRoundCustomScoringBlack.from_dict(d.pop("black"))




        broadcast_round_round_custom_scoring = cls(
            white=white,
            black=black,
        )


        broadcast_round_round_custom_scoring.additional_properties = d
        return broadcast_round_round_custom_scoring

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
