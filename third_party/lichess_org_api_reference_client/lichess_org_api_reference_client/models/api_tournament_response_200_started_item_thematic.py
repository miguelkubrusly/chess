from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiTournamentResponse200StartedItemThematic")



@_attrs_define
class ApiTournamentResponse200StartedItemThematic:
    """ 
        Attributes:
            eco (Union[Unset, str]):  Example: C41.
            name (Union[Unset, str]):  Example: Philidor Defense.
            fen (Union[Unset, str]):  Example: rnbqkbnr/ppp2ppp/3p4/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -.
            url (Union[Unset, str]):  Example: https://lichess.org/opening/Philidor_Defense.
     """

    eco: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    fen: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        eco = self.eco

        name = self.name

        fen = self.fen

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if eco is not UNSET:
            field_dict["eco"] = eco
        if name is not UNSET:
            field_dict["name"] = name
        if fen is not UNSET:
            field_dict["fen"] = fen
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        eco = d.pop("eco", UNSET)

        name = d.pop("name", UNSET)

        fen = d.pop("fen", UNSET)

        url = d.pop("url", UNSET)

        api_tournament_response_200_started_item_thematic = cls(
            eco=eco,
            name=name,
            fen=fen,
            url=url,
        )


        api_tournament_response_200_started_item_thematic.additional_properties = d
        return api_tournament_response_200_started_item_thematic

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
