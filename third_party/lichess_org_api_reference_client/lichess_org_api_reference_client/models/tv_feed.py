from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tv_feed_t import TvFeedT
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.tv_feed_featured import TvFeedFeatured
  from ..models.tv_feed_fen import TvFeedFen





T = TypeVar("T", bound="TvFeed")



@_attrs_define
class TvFeed:
    """ 
        Attributes:
            t (TvFeedT): The type of message.
                A summary of the game is sent as the first message and when the featured game changes.
                Subsequent messages are just the FEN, last move, and clocks.
            d (Union['TvFeedFeatured', 'TvFeedFen']): The data of the message
     """

    t: TvFeedT
    d: Union['TvFeedFeatured', 'TvFeedFen']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tv_feed_featured import TvFeedFeatured
        from ..models.tv_feed_fen import TvFeedFen
        t = self.t.value

        d: dict[str, Any]
        if isinstance(self.d, TvFeedFeatured):
            d = self.d.to_dict()
        else:
            d = self.d.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "t": t,
            "d": d,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tv_feed_featured import TvFeedFeatured
        from ..models.tv_feed_fen import TvFeedFen
        d = dict(src_dict)
        t = TvFeedT(d.pop("t"))




        def _parse_d(data: object) -> Union['TvFeedFeatured', 'TvFeedFen']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                d_featured = TvFeedFeatured.from_dict(data)



                return d_featured
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            d_fen = TvFeedFen.from_dict(data)



            return d_fen

        d = _parse_d(d.pop("d"))


        tv_feed = cls(
            t=t,
            d=d,
        )


        tv_feed.additional_properties = d
        return tv_feed

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
