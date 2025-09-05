from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.antichess_atomic_response_200_moves_item_category import AntichessAtomicResponse200MovesItemCategory
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="AntichessAtomicResponse200MovesItem")



@_attrs_define
class AntichessAtomicResponse200MovesItem:
    """ 
        Attributes:
            uci (Union[Unset, str]):  Example: h7h8q.
            san (Union[Unset, str]):  Example: h8=Q+.
            category (Union[Unset, AntichessAtomicResponse200MovesItemCategory]):
            dtz (Union[None, Unset, int]): DTZ50'' with rounding or null if unknown
            precise_dtz (Union[None, Unset, int]): DTZ50'' (only if guaranteed to be not rounded) or null if unknown
            dtc (Union[None, Unset, int]): Depth to Conversion (experimental)
            dtm (Union[None, Unset, int]): Depth To Mate (only for Standard positions with not more than 5 pieces)
            dtw (Union[None, Unset, int]): Depth To Win (only for Antichess positions with not more than 4 pieces)
            zeroing (Union[Unset, bool]):
            checkmate (Union[Unset, bool]):
            stalemate (Union[Unset, bool]):
            variant_win (Union[Unset, bool]):
            variant_loss (Union[Unset, bool]):
            insufficient_material (Union[Unset, bool]):
     """

    uci: Union[Unset, str] = UNSET
    san: Union[Unset, str] = UNSET
    category: Union[Unset, AntichessAtomicResponse200MovesItemCategory] = UNSET
    dtz: Union[None, Unset, int] = UNSET
    precise_dtz: Union[None, Unset, int] = UNSET
    dtc: Union[None, Unset, int] = UNSET
    dtm: Union[None, Unset, int] = UNSET
    dtw: Union[None, Unset, int] = UNSET
    zeroing: Union[Unset, bool] = UNSET
    checkmate: Union[Unset, bool] = UNSET
    stalemate: Union[Unset, bool] = UNSET
    variant_win: Union[Unset, bool] = UNSET
    variant_loss: Union[Unset, bool] = UNSET
    insufficient_material: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        uci = self.uci

        san = self.san

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value


        dtz: Union[None, Unset, int]
        if isinstance(self.dtz, Unset):
            dtz = UNSET
        else:
            dtz = self.dtz

        precise_dtz: Union[None, Unset, int]
        if isinstance(self.precise_dtz, Unset):
            precise_dtz = UNSET
        else:
            precise_dtz = self.precise_dtz

        dtc: Union[None, Unset, int]
        if isinstance(self.dtc, Unset):
            dtc = UNSET
        else:
            dtc = self.dtc

        dtm: Union[None, Unset, int]
        if isinstance(self.dtm, Unset):
            dtm = UNSET
        else:
            dtm = self.dtm

        dtw: Union[None, Unset, int]
        if isinstance(self.dtw, Unset):
            dtw = UNSET
        else:
            dtw = self.dtw

        zeroing = self.zeroing

        checkmate = self.checkmate

        stalemate = self.stalemate

        variant_win = self.variant_win

        variant_loss = self.variant_loss

        insufficient_material = self.insufficient_material


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if uci is not UNSET:
            field_dict["uci"] = uci
        if san is not UNSET:
            field_dict["san"] = san
        if category is not UNSET:
            field_dict["category"] = category
        if dtz is not UNSET:
            field_dict["dtz"] = dtz
        if precise_dtz is not UNSET:
            field_dict["precise_dtz"] = precise_dtz
        if dtc is not UNSET:
            field_dict["dtc"] = dtc
        if dtm is not UNSET:
            field_dict["dtm"] = dtm
        if dtw is not UNSET:
            field_dict["dtw"] = dtw
        if zeroing is not UNSET:
            field_dict["zeroing"] = zeroing
        if checkmate is not UNSET:
            field_dict["checkmate"] = checkmate
        if stalemate is not UNSET:
            field_dict["stalemate"] = stalemate
        if variant_win is not UNSET:
            field_dict["variant_win"] = variant_win
        if variant_loss is not UNSET:
            field_dict["variant_loss"] = variant_loss
        if insufficient_material is not UNSET:
            field_dict["insufficient_material"] = insufficient_material

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uci = d.pop("uci", UNSET)

        san = d.pop("san", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, AntichessAtomicResponse200MovesItemCategory]
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = AntichessAtomicResponse200MovesItemCategory(_category)




        def _parse_dtz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dtz = _parse_dtz(d.pop("dtz", UNSET))


        def _parse_precise_dtz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        precise_dtz = _parse_precise_dtz(d.pop("precise_dtz", UNSET))


        def _parse_dtc(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dtc = _parse_dtc(d.pop("dtc", UNSET))


        def _parse_dtm(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dtm = _parse_dtm(d.pop("dtm", UNSET))


        def _parse_dtw(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dtw = _parse_dtw(d.pop("dtw", UNSET))


        zeroing = d.pop("zeroing", UNSET)

        checkmate = d.pop("checkmate", UNSET)

        stalemate = d.pop("stalemate", UNSET)

        variant_win = d.pop("variant_win", UNSET)

        variant_loss = d.pop("variant_loss", UNSET)

        insufficient_material = d.pop("insufficient_material", UNSET)

        antichess_atomic_response_200_moves_item = cls(
            uci=uci,
            san=san,
            category=category,
            dtz=dtz,
            precise_dtz=precise_dtz,
            dtc=dtc,
            dtm=dtm,
            dtw=dtw,
            zeroing=zeroing,
            checkmate=checkmate,
            stalemate=stalemate,
            variant_win=variant_win,
            variant_loss=variant_loss,
            insufficient_material=insufficient_material,
        )


        antichess_atomic_response_200_moves_item.additional_properties = d
        return antichess_atomic_response_200_moves_item

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
