from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_simul_response_200_created_item_host_title import ApiSimulResponse200CreatedItemHostTitle
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiSimulResponse200CreatedItemHost")



@_attrs_define
class ApiSimulResponse200CreatedItemHost:
    """ 
        Attributes:
            id (str):
            name (str):
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            title (Union[Unset, ApiSimulResponse200CreatedItemHostTitle]): only appears if the user is a titled player or a
                bot user
            patron (Union[Unset, bool]):
            rating (Union[Unset, int]):
            provisional (Union[Unset, bool]):
            game_id (Union[Unset, str]):
            online (Union[Unset, bool]):
     """

    id: str
    name: str
    flair: Union[Unset, str] = UNSET
    title: Union[Unset, ApiSimulResponse200CreatedItemHostTitle] = UNSET
    patron: Union[Unset, bool] = UNSET
    rating: Union[Unset, int] = UNSET
    provisional: Union[Unset, bool] = UNSET
    game_id: Union[Unset, str] = UNSET
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

        rating = self.rating

        provisional = self.provisional

        game_id = self.game_id

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
        if rating is not UNSET:
            field_dict["rating"] = rating
        if provisional is not UNSET:
            field_dict["provisional"] = provisional
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
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
        title: Union[Unset, ApiSimulResponse200CreatedItemHostTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = ApiSimulResponse200CreatedItemHostTitle(_title)




        patron = d.pop("patron", UNSET)

        rating = d.pop("rating", UNSET)

        provisional = d.pop("provisional", UNSET)

        game_id = d.pop("gameId", UNSET)

        online = d.pop("online", UNSET)

        api_simul_response_200_created_item_host = cls(
            id=id,
            name=name,
            flair=flair,
            title=title,
            patron=patron,
            rating=rating,
            provisional=provisional,
            game_id=game_id,
            online=online,
        )


        api_simul_response_200_created_item_host.additional_properties = d
        return api_simul_response_200_created_item_host

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
