from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tv_feed_featured_orientation import TvFeedFeaturedOrientation
from typing import cast

if TYPE_CHECKING:
  from ..models.tv_feed_featured_players_item import TvFeedFeaturedPlayersItem





T = TypeVar("T", bound="TvFeedFeatured")



@_attrs_define
class TvFeedFeatured:
    """ 
        Attributes:
            id (str): The game ID
            orientation (TvFeedFeaturedOrientation):
            players (list['TvFeedFeaturedPlayersItem']):
            fen (str): The FEN of the current position
     """

    id: str
    orientation: TvFeedFeaturedOrientation
    players: list['TvFeedFeaturedPlayersItem']
    fen: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tv_feed_featured_players_item import TvFeedFeaturedPlayersItem
        id = self.id

        orientation = self.orientation.value

        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)



        fen = self.fen


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "orientation": orientation,
            "players": players,
            "fen": fen,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tv_feed_featured_players_item import TvFeedFeaturedPlayersItem
        d = dict(src_dict)
        id = d.pop("id")

        orientation = TvFeedFeaturedOrientation(d.pop("orientation"))




        players = []
        _players = d.pop("players")
        for players_item_data in (_players):
            players_item = TvFeedFeaturedPlayersItem.from_dict(players_item_data)



            players.append(players_item)


        fen = d.pop("fen")

        tv_feed_featured = cls(
            id=id,
            orientation=orientation,
            players=players,
            fen=fen,
        )


        tv_feed_featured.additional_properties = d
        return tv_feed_featured

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
