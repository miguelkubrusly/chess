from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.user_activity_games_king_of_the_hill_rp import UserActivityGamesKingOfTheHillRp





T = TypeVar("T", bound="UserActivityGamesKingOfTheHill")



@_attrs_define
class UserActivityGamesKingOfTheHill:
    """ 
        Attributes:
            win (float):
            loss (float):
            draw (float):
            rp (UserActivityGamesKingOfTheHillRp):
     """

    win: float
    loss: float
    draw: float
    rp: 'UserActivityGamesKingOfTheHillRp'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_activity_games_king_of_the_hill_rp import UserActivityGamesKingOfTheHillRp
        win = self.win

        loss = self.loss

        draw = self.draw

        rp = self.rp.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "win": win,
            "loss": loss,
            "draw": draw,
            "rp": rp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_activity_games_king_of_the_hill_rp import UserActivityGamesKingOfTheHillRp
        d = dict(src_dict)
        win = d.pop("win")

        loss = d.pop("loss")

        draw = d.pop("draw")

        rp = UserActivityGamesKingOfTheHillRp.from_dict(d.pop("rp"))




        user_activity_games_king_of_the_hill = cls(
            win=win,
            loss=loss,
            draw=draw,
            rp=rp,
        )


        user_activity_games_king_of_the_hill.additional_properties = d
        return user_activity_games_king_of_the_hill

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
