from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.broadcast_round_update_response_200_round_custom_scoring_white import BroadcastRoundUpdateResponse200RoundCustomScoringWhite
  from ..models.broadcast_round_update_response_200_round_custom_scoring_black import BroadcastRoundUpdateResponse200RoundCustomScoringBlack





T = TypeVar("T", bound="BroadcastRoundUpdateResponse200RoundCustomScoring")



@_attrs_define
class BroadcastRoundUpdateResponse200RoundCustomScoring:
    """ Scoring overrides for wins or draws.

        Attributes:
            white (BroadcastRoundUpdateResponse200RoundCustomScoringWhite):
            black (BroadcastRoundUpdateResponse200RoundCustomScoringBlack):
     """

    white: 'BroadcastRoundUpdateResponse200RoundCustomScoringWhite'
    black: 'BroadcastRoundUpdateResponse200RoundCustomScoringBlack'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_round_update_response_200_round_custom_scoring_white import BroadcastRoundUpdateResponse200RoundCustomScoringWhite
        from ..models.broadcast_round_update_response_200_round_custom_scoring_black import BroadcastRoundUpdateResponse200RoundCustomScoringBlack
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
        from ..models.broadcast_round_update_response_200_round_custom_scoring_white import BroadcastRoundUpdateResponse200RoundCustomScoringWhite
        from ..models.broadcast_round_update_response_200_round_custom_scoring_black import BroadcastRoundUpdateResponse200RoundCustomScoringBlack
        d = dict(src_dict)
        white = BroadcastRoundUpdateResponse200RoundCustomScoringWhite.from_dict(d.pop("white"))




        black = BroadcastRoundUpdateResponse200RoundCustomScoringBlack.from_dict(d.pop("black"))




        broadcast_round_update_response_200_round_custom_scoring = cls(
            white=white,
            black=black,
        )


        broadcast_round_update_response_200_round_custom_scoring.additional_properties = d
        return broadcast_round_update_response_200_round_custom_scoring

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
