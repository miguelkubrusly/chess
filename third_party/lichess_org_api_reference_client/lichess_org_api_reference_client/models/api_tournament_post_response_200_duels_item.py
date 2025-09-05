from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_tournament_post_response_200_duels_item_p_item import ApiTournamentPostResponse200DuelsItemPItem





T = TypeVar("T", bound="ApiTournamentPostResponse200DuelsItem")



@_attrs_define
class ApiTournamentPostResponse200DuelsItem:
    """ 
        Attributes:
            id (Union[Unset, str]):
            p (Union[Unset, list['ApiTournamentPostResponse200DuelsItemPItem']]):
     """

    id: Union[Unset, str] = UNSET
    p: Union[Unset, list['ApiTournamentPostResponse200DuelsItemPItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_tournament_post_response_200_duels_item_p_item import ApiTournamentPostResponse200DuelsItemPItem
        id = self.id

        p: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.p, Unset):
            p = []
            for p_item_data in self.p:
                p_item = p_item_data.to_dict()
                p.append(p_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if p is not UNSET:
            field_dict["p"] = p

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_tournament_post_response_200_duels_item_p_item import ApiTournamentPostResponse200DuelsItemPItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        p = []
        _p = d.pop("p", UNSET)
        for p_item_data in (_p or []):
            p_item = ApiTournamentPostResponse200DuelsItemPItem.from_dict(p_item_data)



            p.append(p_item)


        api_tournament_post_response_200_duels_item = cls(
            id=id,
            p=p,
        )


        api_tournament_post_response_200_duels_item.additional_properties = d
        return api_tournament_post_response_200_duels_item

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
