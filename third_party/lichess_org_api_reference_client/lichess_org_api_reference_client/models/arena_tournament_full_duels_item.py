from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.arena_tournament_full_duels_item_p_item import ArenaTournamentFullDuelsItemPItem





T = TypeVar("T", bound="ArenaTournamentFullDuelsItem")



@_attrs_define
class ArenaTournamentFullDuelsItem:
    """ 
        Attributes:
            id (Union[Unset, str]):
            p (Union[Unset, list['ArenaTournamentFullDuelsItemPItem']]):
     """

    id: Union[Unset, str] = UNSET
    p: Union[Unset, list['ArenaTournamentFullDuelsItemPItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.arena_tournament_full_duels_item_p_item import ArenaTournamentFullDuelsItemPItem
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
        from ..models.arena_tournament_full_duels_item_p_item import ArenaTournamentFullDuelsItemPItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        p = []
        _p = d.pop("p", UNSET)
        for p_item_data in (_p or []):
            p_item = ArenaTournamentFullDuelsItemPItem.from_dict(p_item_data)



            p.append(p_item)


        arena_tournament_full_duels_item = cls(
            id=id,
            p=p,
        )


        arena_tournament_full_duels_item.additional_properties = d
        return arena_tournament_full_duels_item

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
