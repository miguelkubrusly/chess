from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_user_title_type_0 import ChallengeUserTitleType0
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ChallengeUser")



@_attrs_define
class ChallengeUser:
    """ 
        Attributes:
            id (str):
            name (str):
            rating (Union[Unset, float]):
            title (Union[ChallengeUserTitleType0, None, Unset]):
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            patron (Union[Unset, bool]):
            provisional (Union[Unset, bool]):
            online (Union[Unset, bool]):
            lag (Union[Unset, float]):
     """

    id: str
    name: str
    rating: Union[Unset, float] = UNSET
    title: Union[ChallengeUserTitleType0, None, Unset] = UNSET
    flair: Union[Unset, str] = UNSET
    patron: Union[Unset, bool] = UNSET
    provisional: Union[Unset, bool] = UNSET
    online: Union[Unset, bool] = UNSET
    lag: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        rating = self.rating

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, ChallengeUserTitleType0):
            title = self.title.value
        else:
            title = self.title

        flair = self.flair

        patron = self.patron

        provisional = self.provisional

        online = self.online

        lag = self.lag


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })
        if rating is not UNSET:
            field_dict["rating"] = rating
        if title is not UNSET:
            field_dict["title"] = title
        if flair is not UNSET:
            field_dict["flair"] = flair
        if patron is not UNSET:
            field_dict["patron"] = patron
        if provisional is not UNSET:
            field_dict["provisional"] = provisional
        if online is not UNSET:
            field_dict["online"] = online
        if lag is not UNSET:
            field_dict["lag"] = lag

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        rating = d.pop("rating", UNSET)

        def _parse_title(data: object) -> Union[ChallengeUserTitleType0, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                title_type_0 = ChallengeUserTitleType0(data)



                return title_type_0
            except: # noqa: E722
                pass
            return cast(Union[ChallengeUserTitleType0, None, Unset], data)

        title = _parse_title(d.pop("title", UNSET))


        flair = d.pop("flair", UNSET)

        patron = d.pop("patron", UNSET)

        provisional = d.pop("provisional", UNSET)

        online = d.pop("online", UNSET)

        lag = d.pop("lag", UNSET)

        challenge_user = cls(
            id=id,
            name=name,
            rating=rating,
            title=title,
            flair=flair,
            patron=patron,
            provisional=provisional,
            online=online,
            lag=lag,
        )


        challenge_user.additional_properties = d
        return challenge_user

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
