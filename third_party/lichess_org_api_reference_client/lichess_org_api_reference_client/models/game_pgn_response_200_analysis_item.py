from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.game_pgn_response_200_analysis_item_judgment import GamePgnResponse200AnalysisItemJudgment





T = TypeVar("T", bound="GamePgnResponse200AnalysisItem")



@_attrs_define
class GamePgnResponse200AnalysisItem:
    """ 
        Attributes:
            eval_ (Union[Unset, float]): Evaluation in centipawns
            mate (Union[Unset, float]): Number of moves until forced mate
            best (Union[Unset, str]): Best move in UCI notation (only if played move was inaccurate) Example: c2c3.
            variation (Union[Unset, str]): Best variation in SAN notation (only if played move was inaccurate) Example: c3
                Nc6 d4 Qb6 Be2 Nge7 Na3 cxd4 cxd4 Nf5.
            judgment (Union[Unset, GamePgnResponse200AnalysisItemJudgment]): Judgment annotation (only if played move was
                inaccurate)
     """

    eval_: Union[Unset, float] = UNSET
    mate: Union[Unset, float] = UNSET
    best: Union[Unset, str] = UNSET
    variation: Union[Unset, str] = UNSET
    judgment: Union[Unset, 'GamePgnResponse200AnalysisItemJudgment'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.game_pgn_response_200_analysis_item_judgment import GamePgnResponse200AnalysisItemJudgment
        eval_ = self.eval_

        mate = self.mate

        best = self.best

        variation = self.variation

        judgment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.judgment, Unset):
            judgment = self.judgment.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if eval_ is not UNSET:
            field_dict["eval"] = eval_
        if mate is not UNSET:
            field_dict["mate"] = mate
        if best is not UNSET:
            field_dict["best"] = best
        if variation is not UNSET:
            field_dict["variation"] = variation
        if judgment is not UNSET:
            field_dict["judgment"] = judgment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_pgn_response_200_analysis_item_judgment import GamePgnResponse200AnalysisItemJudgment
        d = dict(src_dict)
        eval_ = d.pop("eval", UNSET)

        mate = d.pop("mate", UNSET)

        best = d.pop("best", UNSET)

        variation = d.pop("variation", UNSET)

        _judgment = d.pop("judgment", UNSET)
        judgment: Union[Unset, GamePgnResponse200AnalysisItemJudgment]
        if isinstance(_judgment,  Unset):
            judgment = UNSET
        else:
            judgment = GamePgnResponse200AnalysisItemJudgment.from_dict(_judgment)




        game_pgn_response_200_analysis_item = cls(
            eval_=eval_,
            mate=mate,
            best=best,
            variation=variation,
            judgment=judgment,
        )


        game_pgn_response_200_analysis_item.additional_properties = d
        return game_pgn_response_200_analysis_item

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
