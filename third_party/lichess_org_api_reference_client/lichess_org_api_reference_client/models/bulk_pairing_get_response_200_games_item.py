from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="BulkPairingGetResponse200GamesItem")



@_attrs_define
class BulkPairingGetResponse200GamesItem:
    """ 
        Attributes:
            id (Union[Unset, str]):
            black (Union[Unset, str]):
            white (Union[Unset, str]):
     """

    id: Union[Unset, str] = UNSET
    black: Union[Unset, str] = UNSET
    white: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        black = self.black

        white = self.white


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if black is not UNSET:
            field_dict["black"] = black
        if white is not UNSET:
            field_dict["white"] = white

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        black = d.pop("black", UNSET)

        white = d.pop("white", UNSET)

        bulk_pairing_get_response_200_games_item = cls(
            id=id,
            black=black,
            white=white,
        )


        bulk_pairing_get_response_200_games_item.additional_properties = d
        return bulk_pairing_get_response_200_games_item

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
