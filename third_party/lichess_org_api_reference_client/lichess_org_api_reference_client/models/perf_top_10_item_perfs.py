from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.perf_top_10_item_perfs_additional_property import PerfTop10ItemPerfsAdditionalProperty





T = TypeVar("T", bound="PerfTop10ItemPerfs")



@_attrs_define
class PerfTop10ItemPerfs:
    """ 
     """

    additional_properties: dict[str, 'PerfTop10ItemPerfsAdditionalProperty'] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.perf_top_10_item_perfs_additional_property import PerfTop10ItemPerfsAdditionalProperty
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.perf_top_10_item_perfs_additional_property import PerfTop10ItemPerfsAdditionalProperty
        d = dict(src_dict)
        perf_top_10_item_perfs = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PerfTop10ItemPerfsAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        perf_top_10_item_perfs.additional_properties = additional_properties
        return perf_top_10_item_perfs

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> 'PerfTop10ItemPerfsAdditionalProperty':
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: 'PerfTop10ItemPerfsAdditionalProperty') -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
