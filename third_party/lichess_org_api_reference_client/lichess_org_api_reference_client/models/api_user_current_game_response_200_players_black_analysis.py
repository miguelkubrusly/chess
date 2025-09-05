from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiUserCurrentGameResponse200PlayersBlackAnalysis")



@_attrs_define
class ApiUserCurrentGameResponse200PlayersBlackAnalysis:
    """ 
        Attributes:
            inaccuracy (float):
            mistake (float):
            blunder (float):
            acpl (float):
            accuracy (Union[Unset, float]):
     """

    inaccuracy: float
    mistake: float
    blunder: float
    acpl: float
    accuracy: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        inaccuracy = self.inaccuracy

        mistake = self.mistake

        blunder = self.blunder

        acpl = self.acpl

        accuracy = self.accuracy


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "inaccuracy": inaccuracy,
            "mistake": mistake,
            "blunder": blunder,
            "acpl": acpl,
        })
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inaccuracy = d.pop("inaccuracy")

        mistake = d.pop("mistake")

        blunder = d.pop("blunder")

        acpl = d.pop("acpl")

        accuracy = d.pop("accuracy", UNSET)

        api_user_current_game_response_200_players_black_analysis = cls(
            inaccuracy=inaccuracy,
            mistake=mistake,
            blunder=blunder,
            acpl=acpl,
            accuracy=accuracy,
        )


        api_user_current_game_response_200_players_black_analysis.additional_properties = d
        return api_user_current_game_response_200_players_black_analysis

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
