from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_puzzle_replay_response_200_replay import ApiPuzzleReplayResponse200Replay
  from ..models.api_puzzle_replay_response_200_angle import ApiPuzzleReplayResponse200Angle





T = TypeVar("T", bound="ApiPuzzleReplayResponse200")



@_attrs_define
class ApiPuzzleReplayResponse200:
    """ 
        Attributes:
            replay (ApiPuzzleReplayResponse200Replay):
            angle (ApiPuzzleReplayResponse200Angle):
     """

    replay: 'ApiPuzzleReplayResponse200Replay'
    angle: 'ApiPuzzleReplayResponse200Angle'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_puzzle_replay_response_200_replay import ApiPuzzleReplayResponse200Replay
        from ..models.api_puzzle_replay_response_200_angle import ApiPuzzleReplayResponse200Angle
        replay = self.replay.to_dict()

        angle = self.angle.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "replay": replay,
            "angle": angle,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_puzzle_replay_response_200_replay import ApiPuzzleReplayResponse200Replay
        from ..models.api_puzzle_replay_response_200_angle import ApiPuzzleReplayResponse200Angle
        d = dict(src_dict)
        replay = ApiPuzzleReplayResponse200Replay.from_dict(d.pop("replay"))




        angle = ApiPuzzleReplayResponse200Angle.from_dict(d.pop("angle"))




        api_puzzle_replay_response_200 = cls(
            replay=replay,
            angle=angle,
        )


        api_puzzle_replay_response_200.additional_properties = d
        return api_puzzle_replay_response_200

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
