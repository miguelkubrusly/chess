from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TvFeedFen")



@_attrs_define
class TvFeedFen:
    """ 
        Attributes:
            fen (str): The FEN of the current position
            lm (str): The last move in UCI format
            wc (int): White's clock in seconds
            bc (int): Black's clock in seconds
     """

    fen: str
    lm: str
    wc: int
    bc: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        fen = self.fen

        lm = self.lm

        wc = self.wc

        bc = self.bc


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fen": fen,
            "lm": lm,
            "wc": wc,
            "bc": bc,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fen = d.pop("fen")

        lm = d.pop("lm")

        wc = d.pop("wc")

        bc = d.pop("bc")

        tv_feed_fen = cls(
            fen=fen,
            lm=lm,
            wc=wc,
            bc=bc,
        )


        tv_feed_fen.additional_properties = d
        return tv_feed_fen

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
