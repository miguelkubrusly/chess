from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="Count")



@_attrs_define
class Count:
    """ 
        Attributes:
            all_ (int):
            rated (int):
            ai (int):
            draw (int):
            draw_h (int):
            loss (int):
            loss_h (int):
            win (int):
            win_h (int):
            bookmark (int):
            playing (int):
            import_ (int):
            me (int):
     """

    all_: int
    rated: int
    ai: int
    draw: int
    draw_h: int
    loss: int
    loss_h: int
    win: int
    win_h: int
    bookmark: int
    playing: int
    import_: int
    me: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        rated = self.rated

        ai = self.ai

        draw = self.draw

        draw_h = self.draw_h

        loss = self.loss

        loss_h = self.loss_h

        win = self.win

        win_h = self.win_h

        bookmark = self.bookmark

        playing = self.playing

        import_ = self.import_

        me = self.me


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "all": all_,
            "rated": rated,
            "ai": ai,
            "draw": draw,
            "drawH": draw_h,
            "loss": loss,
            "lossH": loss_h,
            "win": win,
            "winH": win_h,
            "bookmark": bookmark,
            "playing": playing,
            "import": import_,
            "me": me,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_ = d.pop("all")

        rated = d.pop("rated")

        ai = d.pop("ai")

        draw = d.pop("draw")

        draw_h = d.pop("drawH")

        loss = d.pop("loss")

        loss_h = d.pop("lossH")

        win = d.pop("win")

        win_h = d.pop("winH")

        bookmark = d.pop("bookmark")

        playing = d.pop("playing")

        import_ = d.pop("import")

        me = d.pop("me")

        count = cls(
            all_=all_,
            rated=rated,
            ai=ai,
            draw=draw,
            draw_h=draw_h,
            loss=loss,
            loss_h=loss_h,
            win=win,
            win_h=win_h,
            bookmark=bookmark,
            playing=playing,
            import_=import_,
            me=me,
        )


        count.additional_properties = d
        return count

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
