from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.cloud_eval_non_mate_variation import CloudEvalNonMateVariation
  from ..models.cloud_eval_mate_variation import CloudEvalMateVariation





T = TypeVar("T", bound="CloudEval")



@_attrs_define
class CloudEval:
    """ 
        Example:
            {'fen': 'r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R', 'knodes': 106325, 'depth': 29, 'pvs': [{'moves':
                'd1e2 d8e7 a2a4 a7a6 b5c4 d7d6 d2d3 g8f6 c1e3 c6a5', 'cp': 41}, {'moves': 'c2c3 a7a6 b5a4 g8f6 d2d3 b7b5 a4b3
                h7h6 a2a4 c8b7', 'cp': 39}, {'moves': 'd2d3 d8f6 c2c3 a7a6 b5a4 f8c5 d3d4 c5a7 c1e3 g8e7', 'cp': 37}]}

        Attributes:
            depth (int):
            fen (str):
            knodes (int):
            pvs (list[Union['CloudEvalMateVariation', 'CloudEvalNonMateVariation']]):
     """

    depth: int
    fen: str
    knodes: int
    pvs: list[Union['CloudEvalMateVariation', 'CloudEvalNonMateVariation']]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_eval_non_mate_variation import CloudEvalNonMateVariation
        from ..models.cloud_eval_mate_variation import CloudEvalMateVariation
        depth = self.depth

        fen = self.fen

        knodes = self.knodes

        pvs = []
        for pvs_item_data in self.pvs:
            pvs_item: dict[str, Any]
            if isinstance(pvs_item_data, CloudEvalNonMateVariation):
                pvs_item = pvs_item_data.to_dict()
            else:
                pvs_item = pvs_item_data.to_dict()

            pvs.append(pvs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "depth": depth,
            "fen": fen,
            "knodes": knodes,
            "pvs": pvs,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_eval_non_mate_variation import CloudEvalNonMateVariation
        from ..models.cloud_eval_mate_variation import CloudEvalMateVariation
        d = dict(src_dict)
        depth = d.pop("depth")

        fen = d.pop("fen")

        knodes = d.pop("knodes")

        pvs = []
        _pvs = d.pop("pvs")
        for pvs_item_data in (_pvs):
            def _parse_pvs_item(data: object) -> Union['CloudEvalMateVariation', 'CloudEvalNonMateVariation']:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    pvs_item_non_mate_variation = CloudEvalNonMateVariation.from_dict(data)



                    return pvs_item_non_mate_variation
                except: # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                pvs_item_mate_variation = CloudEvalMateVariation.from_dict(data)



                return pvs_item_mate_variation

            pvs_item = _parse_pvs_item(pvs_item_data)

            pvs.append(pvs_item)


        cloud_eval = cls(
            depth=depth,
            fen=fen,
            knodes=knodes,
            pvs=pvs,
        )


        cloud_eval.additional_properties = d
        return cloud_eval

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
