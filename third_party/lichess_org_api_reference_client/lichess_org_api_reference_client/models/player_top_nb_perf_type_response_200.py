from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.player_top_nb_perf_type_response_200_users_item import PlayerTopNbPerfTypeResponse200UsersItem





T = TypeVar("T", bound="PlayerTopNbPerfTypeResponse200")



@_attrs_define
class PlayerTopNbPerfTypeResponse200:
    """ 
        Attributes:
            users (list['PlayerTopNbPerfTypeResponse200UsersItem']):
     """

    users: list['PlayerTopNbPerfTypeResponse200UsersItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.player_top_nb_perf_type_response_200_users_item import PlayerTopNbPerfTypeResponse200UsersItem
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "users": users,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.player_top_nb_perf_type_response_200_users_item import PlayerTopNbPerfTypeResponse200UsersItem
        d = dict(src_dict)
        users = []
        _users = d.pop("users")
        for users_item_data in (_users):
            users_item = PlayerTopNbPerfTypeResponse200UsersItem.from_dict(users_item_data)



            users.append(users_item)


        player_top_nb_perf_type_response_200 = cls(
            users=users,
        )


        player_top_nb_perf_type_response_200.additional_properties = d
        return player_top_nb_perf_type_response_200

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
