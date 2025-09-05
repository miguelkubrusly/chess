from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.user_activity_puzzles_score import UserActivityPuzzlesScore





T = TypeVar("T", bound="UserActivityPuzzles")



@_attrs_define
class UserActivityPuzzles:
    """ 
        Attributes:
            score (Union[Unset, UserActivityPuzzlesScore]):
     """

    score: Union[Unset, 'UserActivityPuzzlesScore'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_activity_puzzles_score import UserActivityPuzzlesScore
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
        from ..models.user_activity_puzzles_score import UserActivityPuzzlesScore
        d = dict(src_dict)
        _score = d.pop("score", UNSET)
        score: Union[Unset, UserActivityPuzzlesScore]
        if isinstance(_score,  Unset):
            score = UNSET
        else:
            score = UserActivityPuzzlesScore.from_dict(_score)




        user_activity_puzzles = cls(
            score=score,
        )


        user_activity_puzzles.additional_properties = d
        return user_activity_puzzles

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
