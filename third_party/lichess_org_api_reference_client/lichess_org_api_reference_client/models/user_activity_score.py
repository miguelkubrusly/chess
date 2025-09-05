from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.user_activity_score_rp import UserActivityScoreRp





T = TypeVar("T", bound="UserActivityScore")



@_attrs_define
class UserActivityScore:
    """ 
        Attributes:
            win (float):
            loss (float):
            draw (float):
            rp (UserActivityScoreRp):
     """

    win: float
    loss: float
    draw: float
    rp: 'UserActivityScoreRp'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_activity_score_rp import UserActivityScoreRp
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
        from ..models.user_activity_score_rp import UserActivityScoreRp
        d = dict(src_dict)
        win = d.pop("win")

        loss = d.pop("loss")

        draw = d.pop("draw")

        rp = UserActivityScoreRp.from_dict(d.pop("rp"))




        user_activity_score = cls(
            win=win,
            loss=loss,
            draw=draw,
            rp=rp,
        )


        user_activity_score.additional_properties = d
        return user_activity_score

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
