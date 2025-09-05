from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tablebase_atomic_response_200_category import TablebaseAtomicResponse200Category
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.tablebase_atomic_response_200_moves_item import TablebaseAtomicResponse200MovesItem





T = TypeVar("T", bound="TablebaseAtomicResponse200")



@_attrs_define
class TablebaseAtomicResponse200:
    """ 
        Example:
            {'dtz': 1, 'precise_dtz': 1, 'dtc': None, 'dtm': 17, 'dtw': None, 'checkmate': False, 'stalemate': False,
                'variant_win': False, 'variant_loss': False, 'insufficient_material': False, 'category': 'win', 'moves':
                [{'uci': 'h7h8q', 'san': 'h8=Q+', 'dtz': -2, 'precise_dtz': -2, 'dtc': None, 'dtm': -16, 'dtw': None, 'zeroing':
                True, 'checkmate': False, 'stalemate': False, 'variant_win': False, 'variant_loss': False,
                'insufficient_material': False, 'category': 'loss'}]}

        Attributes:
            category (Union[Unset, TablebaseAtomicResponse200Category]): `cursed-win` and `blessed-loss` means the 50-move
                rule prevents
                the decisive result.

                `syzygy-win` and `syzygy-loss` means exact result is unknown due to
                [DTZ rounding](https://syzygy-tables.info/metrics#dtz), i.e., the
                win or loss could also be prevented by the 50-move rule if
                the user has deviated from the tablebase recommendation since the
                last pawn move or capture.

                `maybe-win` and `maybe-loss` means the result with regard to the
                50-move rule is unknown because the DTC tablebase does not
                guarantee to reach a zeroing move as soon as possible.
            dtz (Union[None, Unset, int]): [DTZ50'' with rounding](https://syzygy-tables.info/metrics#dtz) or null if
                unknown
            precise_dtz (Union[None, Unset, int]): DTZ50'' (only if guaranteed to be not rounded) or null if unknown
            dtc (Union[None, Unset, int]): Depth to Conversion (experimental)
            dtm (Union[None, Unset, int]): Depth To Mate (only for Standard positions with not more than 5 pieces)
            dtw (Union[None, Unset, int]): Depth To Win (only for Antichess positions with not more than 4 pieces)
            checkmate (Union[Unset, bool]):
            stalemate (Union[Unset, bool]):
            variant_win (Union[Unset, bool]): Only in chess variants
            variant_loss (Union[Unset, bool]): Only in chess variants
            insufficient_material (Union[Unset, bool]):
            moves (Union[Unset, list['TablebaseAtomicResponse200MovesItem']]): Information about legal moves, best first
     """

    category: Union[Unset, TablebaseAtomicResponse200Category] = UNSET
    dtz: Union[None, Unset, int] = UNSET
    precise_dtz: Union[None, Unset, int] = UNSET
    dtc: Union[None, Unset, int] = UNSET
    dtm: Union[None, Unset, int] = UNSET
    dtw: Union[None, Unset, int] = UNSET
    checkmate: Union[Unset, bool] = UNSET
    stalemate: Union[Unset, bool] = UNSET
    variant_win: Union[Unset, bool] = UNSET
    variant_loss: Union[Unset, bool] = UNSET
    insufficient_material: Union[Unset, bool] = UNSET
    moves: Union[Unset, list['TablebaseAtomicResponse200MovesItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tablebase_atomic_response_200_moves_item import TablebaseAtomicResponse200MovesItem
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

        checkmate = self.checkmate

        stalemate = self.stalemate

        variant_win = self.variant_win

        variant_loss = self.variant_loss

        insufficient_material = self.insufficient_material

        moves: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.moves, Unset):
            moves = []
            for moves_item_data in self.moves:
                moves_item = moves_item_data.to_dict()
                moves.append(moves_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        if moves is not UNSET:
            field_dict["moves"] = moves

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tablebase_atomic_response_200_moves_item import TablebaseAtomicResponse200MovesItem
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: Union[Unset, TablebaseAtomicResponse200Category]
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = TablebaseAtomicResponse200Category(_category)




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


        checkmate = d.pop("checkmate", UNSET)

        stalemate = d.pop("stalemate", UNSET)

        variant_win = d.pop("variant_win", UNSET)

        variant_loss = d.pop("variant_loss", UNSET)

        insufficient_material = d.pop("insufficient_material", UNSET)

        moves = []
        _moves = d.pop("moves", UNSET)
        for moves_item_data in (_moves or []):
            moves_item = TablebaseAtomicResponse200MovesItem.from_dict(moves_item_data)



            moves.append(moves_item)


        tablebase_atomic_response_200 = cls(
            category=category,
            dtz=dtz,
            precise_dtz=precise_dtz,
            dtc=dtc,
            dtm=dtm,
            dtw=dtw,
            checkmate=checkmate,
            stalemate=stalemate,
            variant_win=variant_win,
            variant_loss=variant_loss,
            insufficient_material=insufficient_material,
            moves=moves,
        )


        tablebase_atomic_response_200.additional_properties = d
        return tablebase_atomic_response_200

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
