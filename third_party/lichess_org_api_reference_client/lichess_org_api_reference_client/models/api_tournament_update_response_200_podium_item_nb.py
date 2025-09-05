from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiTournamentUpdateResponse200PodiumItemNb")



@_attrs_define
class ApiTournamentUpdateResponse200PodiumItemNb:
    """ 
        Attributes:
            game (Union[Unset, float]):
            berserk (Union[Unset, float]):
            win (Union[Unset, float]):
     """

    game: Union[Unset, float] = UNSET
    berserk: Union[Unset, float] = UNSET
    win: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        game = self.game

        berserk = self.berserk

        win = self.win


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if game is not UNSET:
            field_dict["game"] = game
        if berserk is not UNSET:
            field_dict["berserk"] = berserk
        if win is not UNSET:
            field_dict["win"] = win

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        game = d.pop("game", UNSET)

        berserk = d.pop("berserk", UNSET)

        win = d.pop("win", UNSET)

        api_tournament_update_response_200_podium_item_nb = cls(
            game=game,
            berserk=berserk,
            win=win,
        )


        api_tournament_update_response_200_podium_item_nb.additional_properties = d
        return api_tournament_update_response_200_podium_item_nb

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
