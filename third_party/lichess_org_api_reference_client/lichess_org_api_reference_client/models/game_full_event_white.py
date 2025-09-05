from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.game_full_event_white_title_type_0 import GameFullEventWhiteTitleType0
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="GameFullEventWhite")



@_attrs_define
class GameFullEventWhite:
    """ 
        Attributes:
            id (str):
            name (str):
            ai_level (Union[Unset, int]):
            title (Union[GameFullEventWhiteTitleType0, None, Unset]):
            rating (Union[Unset, int]):
            provisional (Union[Unset, bool]):
     """

    id: str
    name: str
    ai_level: Union[Unset, int] = UNSET
    title: Union[GameFullEventWhiteTitleType0, None, Unset] = UNSET
    rating: Union[Unset, int] = UNSET
    provisional: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ai_level = self.ai_level

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, GameFullEventWhiteTitleType0):
            title = self.title.value
        else:
            title = self.title

        rating = self.rating

        provisional = self.provisional


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })
        if ai_level is not UNSET:
            field_dict["aiLevel"] = ai_level
        if title is not UNSET:
            field_dict["title"] = title
        if rating is not UNSET:
            field_dict["rating"] = rating
        if provisional is not UNSET:
            field_dict["provisional"] = provisional

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        ai_level = d.pop("aiLevel", UNSET)

        def _parse_title(data: object) -> Union[GameFullEventWhiteTitleType0, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                title_type_0 = GameFullEventWhiteTitleType0(data)



                return title_type_0
            except: # noqa: E722
                pass
            return cast(Union[GameFullEventWhiteTitleType0, None, Unset], data)

        title = _parse_title(d.pop("title", UNSET))


        rating = d.pop("rating", UNSET)

        provisional = d.pop("provisional", UNSET)

        game_full_event_white = cls(
            id=id,
            name=name,
            ai_level=ai_level,
            title=title,
            rating=rating,
            provisional=provisional,
        )


        game_full_event_white.additional_properties = d
        return game_full_event_white

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
