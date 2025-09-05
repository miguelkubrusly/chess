from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_puzzle_id_response_200_game_players_item_title import ApiPuzzleIdResponse200GamePlayersItemTitle
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiPuzzleIdResponse200GamePlayersItem")



@_attrs_define
class ApiPuzzleIdResponse200GamePlayersItem:
    """ 
        Attributes:
            color (str):
            id (str):
            name (str):
            rating (int):
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            patron (Union[Unset, bool]):
            title (Union[Unset, ApiPuzzleIdResponse200GamePlayersItemTitle]): only appears if the user is a titled player or
                a bot user
     """

    color: str
    id: str
    name: str
    rating: int
    flair: Union[Unset, str] = UNSET
    patron: Union[Unset, bool] = UNSET
    title: Union[Unset, ApiPuzzleIdResponse200GamePlayersItemTitle] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        color = self.color

        id = self.id

        name = self.name

        rating = self.rating

        flair = self.flair

        patron = self.patron

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "color": color,
            "id": id,
            "name": name,
            "rating": rating,
        })
        if flair is not UNSET:
            field_dict["flair"] = flair
        if patron is not UNSET:
            field_dict["patron"] = patron
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color")

        id = d.pop("id")

        name = d.pop("name")

        rating = d.pop("rating")

        flair = d.pop("flair", UNSET)

        patron = d.pop("patron", UNSET)

        _title = d.pop("title", UNSET)
        title: Union[Unset, ApiPuzzleIdResponse200GamePlayersItemTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = ApiPuzzleIdResponse200GamePlayersItemTitle(_title)




        api_puzzle_id_response_200_game_players_item = cls(
            color=color,
            id=id,
            name=name,
            rating=rating,
            flair=flair,
            patron=patron,
            title=title,
        )


        api_puzzle_id_response_200_game_players_item.additional_properties = d
        return api_puzzle_id_response_200_game_players_item

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
