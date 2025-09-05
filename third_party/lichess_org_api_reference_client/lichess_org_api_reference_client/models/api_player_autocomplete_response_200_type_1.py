from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_player_autocomplete_response_200_type_1_result_item import ApiPlayerAutocompleteResponse200Type1ResultItem





T = TypeVar("T", bound="ApiPlayerAutocompleteResponse200Type1")



@_attrs_define
class ApiPlayerAutocompleteResponse200Type1:
    """ 
        Attributes:
            result (Union[Unset, list['ApiPlayerAutocompleteResponse200Type1ResultItem']]):
     """

    result: Union[Unset, list['ApiPlayerAutocompleteResponse200Type1ResultItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_player_autocomplete_response_200_type_1_result_item import ApiPlayerAutocompleteResponse200Type1ResultItem
        result: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for result_item_data in self.result:
                result_item = result_item_data.to_dict()
                result.append(result_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_player_autocomplete_response_200_type_1_result_item import ApiPlayerAutocompleteResponse200Type1ResultItem
        d = dict(src_dict)
        result = []
        _result = d.pop("result", UNSET)
        for result_item_data in (_result or []):
            result_item = ApiPlayerAutocompleteResponse200Type1ResultItem.from_dict(result_item_data)



            result.append(result_item)


        api_player_autocomplete_response_200_type_1 = cls(
            result=result,
        )


        api_player_autocomplete_response_200_type_1.additional_properties = d
        return api_player_autocomplete_response_200_type_1

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
