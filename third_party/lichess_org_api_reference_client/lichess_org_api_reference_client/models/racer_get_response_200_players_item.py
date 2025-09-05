from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RacerGetResponse200PlayersItem")



@_attrs_define
class RacerGetResponse200PlayersItem:
    """ 
        Attributes:
            name (str): Player username
            score (int): Player's current score in the race
            id (Union[Unset, str]): User ID. Missing if player is anonymous.
            flair (Union[Unset, str]): User's flair icon
            patron (Union[Unset, bool]): Whether the player is a Lichess patron
     """

    name: str
    score: int
    id: Union[Unset, str] = UNSET
    flair: Union[Unset, str] = UNSET
    patron: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        score = self.score

        id = self.id

        flair = self.flair

        patron = self.patron


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "score": score,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if flair is not UNSET:
            field_dict["flair"] = flair
        if patron is not UNSET:
            field_dict["patron"] = patron

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        score = d.pop("score")

        id = d.pop("id", UNSET)

        flair = d.pop("flair", UNSET)

        patron = d.pop("patron", UNSET)

        racer_get_response_200_players_item = cls(
            name=name,
            score=score,
            id=id,
            flair=flair,
            patron=patron,
        )


        racer_get_response_200_players_item.additional_properties = d
        return racer_get_response_200_players_item

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
