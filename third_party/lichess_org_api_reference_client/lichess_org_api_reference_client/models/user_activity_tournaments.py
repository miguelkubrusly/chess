from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.user_activity_tournaments_best_item import UserActivityTournamentsBestItem





T = TypeVar("T", bound="UserActivityTournaments")



@_attrs_define
class UserActivityTournaments:
    """ 
        Attributes:
            nb (Union[Unset, float]):
            best (Union[Unset, list['UserActivityTournamentsBestItem']]):
     """

    nb: Union[Unset, float] = UNSET
    best: Union[Unset, list['UserActivityTournamentsBestItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_activity_tournaments_best_item import UserActivityTournamentsBestItem
        nb = self.nb

        best: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.best, Unset):
            best = []
            for best_item_data in self.best:
                best_item = best_item_data.to_dict()
                best.append(best_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if nb is not UNSET:
            field_dict["nb"] = nb
        if best is not UNSET:
            field_dict["best"] = best

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_activity_tournaments_best_item import UserActivityTournamentsBestItem
        d = dict(src_dict)
        nb = d.pop("nb", UNSET)

        best = []
        _best = d.pop("best", UNSET)
        for best_item_data in (_best or []):
            best_item = UserActivityTournamentsBestItem.from_dict(best_item_data)



            best.append(best_item)


        user_activity_tournaments = cls(
            nb=nb,
            best=best,
        )


        user_activity_tournaments.additional_properties = d
        return user_activity_tournaments

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
