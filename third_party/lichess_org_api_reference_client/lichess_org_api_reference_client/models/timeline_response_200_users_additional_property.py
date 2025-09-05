from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.timeline_response_200_users_additional_property_title import TimelineResponse200UsersAdditionalPropertyTitle
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TimelineResponse200UsersAdditionalProperty")



@_attrs_define
class TimelineResponse200UsersAdditionalProperty:
    """ 
        Attributes:
            id (str):
            name (str):
            title (Union[Unset, TimelineResponse200UsersAdditionalPropertyTitle]): only appears if the user is a titled
                player or a bot user
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            patron (Union[Unset, bool]):
     """

    id: str
    name: str
    title: Union[Unset, TimelineResponse200UsersAdditionalPropertyTitle] = UNSET
    flair: Union[Unset, str] = UNSET
    patron: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value


        flair = self.flair

        patron = self.patron


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })
        if title is not UNSET:
            field_dict["title"] = title
        if flair is not UNSET:
            field_dict["flair"] = flair
        if patron is not UNSET:
            field_dict["patron"] = patron

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        _title = d.pop("title", UNSET)
        title: Union[Unset, TimelineResponse200UsersAdditionalPropertyTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = TimelineResponse200UsersAdditionalPropertyTitle(_title)




        flair = d.pop("flair", UNSET)

        patron = d.pop("patron", UNSET)

        timeline_response_200_users_additional_property = cls(
            id=id,
            name=name,
            title=title,
            flair=flair,
            patron=patron,
        )


        timeline_response_200_users_additional_property.additional_properties = d
        return timeline_response_200_users_additional_property

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
