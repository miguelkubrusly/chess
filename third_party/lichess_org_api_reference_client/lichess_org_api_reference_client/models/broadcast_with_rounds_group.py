from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_with_rounds_group_tours_item import BroadcastWithRoundsGroupToursItem





T = TypeVar("T", bound="BroadcastWithRoundsGroup")



@_attrs_define
class BroadcastWithRoundsGroup:
    """ 
        Attributes:
            name (Union[Unset, str]):
            tours (Union[Unset, list['BroadcastWithRoundsGroupToursItem']]):
     """

    name: Union[Unset, str] = UNSET
    tours: Union[Unset, list['BroadcastWithRoundsGroupToursItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_with_rounds_group_tours_item import BroadcastWithRoundsGroupToursItem
        name = self.name

        tours: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tours, Unset):
            tours = []
            for tours_item_data in self.tours:
                tours_item = tours_item_data.to_dict()
                tours.append(tours_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if tours is not UNSET:
            field_dict["tours"] = tours

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_with_rounds_group_tours_item import BroadcastWithRoundsGroupToursItem
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        tours = []
        _tours = d.pop("tours", UNSET)
        for tours_item_data in (_tours or []):
            tours_item = BroadcastWithRoundsGroupToursItem.from_dict(tours_item_data)



            tours.append(tours_item)


        broadcast_with_rounds_group = cls(
            name=name,
            tours=tours,
        )


        broadcast_with_rounds_group.additional_properties = d
        return broadcast_with_rounds_group

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
