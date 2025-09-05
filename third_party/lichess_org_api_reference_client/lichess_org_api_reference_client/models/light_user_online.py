from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.light_user_online_title import LightUserOnlineTitle
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="LightUserOnline")



@_attrs_define
class LightUserOnline:
    """ 
        Attributes:
            id (str):
            name (str):
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            title (Union[Unset, LightUserOnlineTitle]): only appears if the user is a titled player or a bot user
            patron (Union[Unset, bool]):
            online (Union[Unset, bool]):
     """

    id: str
    name: str
    flair: Union[Unset, str] = UNSET
    title: Union[Unset, LightUserOnlineTitle] = UNSET
    patron: Union[Unset, bool] = UNSET
    online: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        flair = self.flair

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value


        patron = self.patron

        online = self.online


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })
        if flair is not UNSET:
            field_dict["flair"] = flair
        if title is not UNSET:
            field_dict["title"] = title
        if patron is not UNSET:
            field_dict["patron"] = patron
        if online is not UNSET:
            field_dict["online"] = online

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        flair = d.pop("flair", UNSET)

        _title = d.pop("title", UNSET)
        title: Union[Unset, LightUserOnlineTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = LightUserOnlineTitle(_title)




        patron = d.pop("patron", UNSET)

        online = d.pop("online", UNSET)

        light_user_online = cls(
            id=id,
            name=name,
            flair=flair,
            title=title,
            patron=patron,
            online=online,
        )


        light_user_online.additional_properties = d
        return light_user_online

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
