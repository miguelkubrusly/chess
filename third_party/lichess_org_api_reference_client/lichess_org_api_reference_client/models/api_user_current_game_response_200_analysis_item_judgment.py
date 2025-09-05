from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_user_current_game_response_200_analysis_item_judgment_name import ApiUserCurrentGameResponse200AnalysisItemJudgmentName
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiUserCurrentGameResponse200AnalysisItemJudgment")



@_attrs_define
class ApiUserCurrentGameResponse200AnalysisItemJudgment:
    """ Judgment annotation (only if played move was inaccurate)

        Attributes:
            name (Union[Unset, ApiUserCurrentGameResponse200AnalysisItemJudgmentName]):
            comment (Union[Unset, str]):  Example: Blunder. Nxg6 was best..
     """

    name: Union[Unset, ApiUserCurrentGameResponse200AnalysisItemJudgmentName] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value


        comment = self.comment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, ApiUserCurrentGameResponse200AnalysisItemJudgmentName]
        if isinstance(_name,  Unset):
            name = UNSET
        else:
            name = ApiUserCurrentGameResponse200AnalysisItemJudgmentName(_name)




        comment = d.pop("comment", UNSET)

        api_user_current_game_response_200_analysis_item_judgment = cls(
            name=name,
            comment=comment,
        )


        api_user_current_game_response_200_analysis_item_judgment.additional_properties = d
        return api_user_current_game_response_200_analysis_item_judgment

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
