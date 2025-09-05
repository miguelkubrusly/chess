from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_user_activity_response_200_item_puzzles_score import ApiUserActivityResponse200ItemPuzzlesScore





T = TypeVar("T", bound="ApiUserActivityResponse200ItemPuzzles")



@_attrs_define
class ApiUserActivityResponse200ItemPuzzles:
    """ 
        Attributes:
            score (Union[Unset, ApiUserActivityResponse200ItemPuzzlesScore]):
     """

    score: Union[Unset, 'ApiUserActivityResponse200ItemPuzzlesScore'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_activity_response_200_item_puzzles_score import ApiUserActivityResponse200ItemPuzzlesScore
        score: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.score, Unset):
            score = self.score.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_user_activity_response_200_item_puzzles_score import ApiUserActivityResponse200ItemPuzzlesScore
        d = dict(src_dict)
        _score = d.pop("score", UNSET)
        score: Union[Unset, ApiUserActivityResponse200ItemPuzzlesScore]
        if isinstance(_score,  Unset):
            score = UNSET
        else:
            score = ApiUserActivityResponse200ItemPuzzlesScore.from_dict(_score)




        api_user_activity_response_200_item_puzzles = cls(
            score=score,
        )


        api_user_activity_response_200_item_puzzles.additional_properties = d
        return api_user_activity_response_200_item_puzzles

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
