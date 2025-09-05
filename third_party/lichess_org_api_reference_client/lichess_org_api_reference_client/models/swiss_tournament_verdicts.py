from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.swiss_tournament_verdicts_list_item import SwissTournamentVerdictsListItem





T = TypeVar("T", bound="SwissTournamentVerdicts")



@_attrs_define
class SwissTournamentVerdicts:
    """ 
        Attributes:
            accepted (bool):
            list_ (list['SwissTournamentVerdictsListItem']):
     """

    accepted: bool
    list_: list['SwissTournamentVerdictsListItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.swiss_tournament_verdicts_list_item import SwissTournamentVerdictsListItem
        accepted = self.accepted

        list_ = []
        for list_item_data in self.list_:
            list_item = list_item_data.to_dict()
            list_.append(list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "accepted": accepted,
            "list": list_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.swiss_tournament_verdicts_list_item import SwissTournamentVerdictsListItem
        d = dict(src_dict)
        accepted = d.pop("accepted")

        list_ = []
        _list_ = d.pop("list")
        for list_item_data in (_list_):
            list_item = SwissTournamentVerdictsListItem.from_dict(list_item_data)



            list_.append(list_item)


        swiss_tournament_verdicts = cls(
            accepted=accepted,
            list_=list_,
        )


        swiss_tournament_verdicts.additional_properties = d
        return swiss_tournament_verdicts

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
