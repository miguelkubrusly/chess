from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.top_10s_antichess_item_title import Top10SAntichessItemTitle
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.top_10s_antichess_item_perfs import Top10SAntichessItemPerfs





T = TypeVar("T", bound="Top10SAntichessItem")



@_attrs_define
class Top10SAntichessItem:
    """ 
        Attributes:
            id (str):
            username (str):
            perfs (Union[Unset, Top10SAntichessItemPerfs]):
            title (Union[Unset, Top10SAntichessItemTitle]): only appears if the user is a titled player or a bot user
            patron (Union[Unset, bool]):
            online (Union[Unset, bool]):
     """

    id: str
    username: str
    perfs: Union[Unset, 'Top10SAntichessItemPerfs'] = UNSET
    title: Union[Unset, Top10SAntichessItemTitle] = UNSET
    patron: Union[Unset, bool] = UNSET
    online: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.top_10s_antichess_item_perfs import Top10SAntichessItemPerfs
        id = self.id

        username = self.username

        perfs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.perfs, Unset):
            perfs = self.perfs.to_dict()

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value


        patron = self.patron

        online = self.online


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "username": username,
        })
        if perfs is not UNSET:
            field_dict["perfs"] = perfs
        if title is not UNSET:
            field_dict["title"] = title
        if patron is not UNSET:
            field_dict["patron"] = patron
        if online is not UNSET:
            field_dict["online"] = online

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.top_10s_antichess_item_perfs import Top10SAntichessItemPerfs
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        _perfs = d.pop("perfs", UNSET)
        perfs: Union[Unset, Top10SAntichessItemPerfs]
        if isinstance(_perfs,  Unset):
            perfs = UNSET
        else:
            perfs = Top10SAntichessItemPerfs.from_dict(_perfs)




        _title = d.pop("title", UNSET)
        title: Union[Unset, Top10SAntichessItemTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = Top10SAntichessItemTitle(_title)




        patron = d.pop("patron", UNSET)

        online = d.pop("online", UNSET)

        top_10s_antichess_item = cls(
            id=id,
            username=username,
            perfs=perfs,
            title=title,
            patron=patron,
            online=online,
        )


        top_10s_antichess_item.additional_properties = d
        return top_10s_antichess_item

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
