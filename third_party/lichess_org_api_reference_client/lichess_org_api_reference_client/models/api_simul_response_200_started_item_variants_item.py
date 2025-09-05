from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_simul_response_200_started_item_variants_item_key import ApiSimulResponse200StartedItemVariantsItemKey
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiSimulResponse200StartedItemVariantsItem")



@_attrs_define
class ApiSimulResponse200StartedItemVariantsItem:
    """ 
        Attributes:
            key (Union[Unset, ApiSimulResponse200StartedItemVariantsItemKey]):  Default:
                ApiSimulResponse200StartedItemVariantsItemKey.STANDARD. Example: standard.
            icon (Union[Unset, str]):
            name (Union[Unset, str]):
     """

    key: Union[Unset, ApiSimulResponse200StartedItemVariantsItemKey] = ApiSimulResponse200StartedItemVariantsItemKey.STANDARD
    icon: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key: Union[Unset, str] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.value


        icon = self.icon

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if icon is not UNSET:
            field_dict["icon"] = icon
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _key = d.pop("key", UNSET)
        key: Union[Unset, ApiSimulResponse200StartedItemVariantsItemKey]
        if isinstance(_key,  Unset):
            key = UNSET
        else:
            key = ApiSimulResponse200StartedItemVariantsItemKey(_key)




        icon = d.pop("icon", UNSET)

        name = d.pop("name", UNSET)

        api_simul_response_200_started_item_variants_item = cls(
            key=key,
            icon=icon,
            name=name,
        )


        api_simul_response_200_started_item_variants_item.additional_properties = d
        return api_simul_response_200_started_item_variants_item

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
