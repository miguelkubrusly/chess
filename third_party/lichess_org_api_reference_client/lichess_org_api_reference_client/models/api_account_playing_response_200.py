from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_account_playing_response_200_now_playing_item import ApiAccountPlayingResponse200NowPlayingItem





T = TypeVar("T", bound="ApiAccountPlayingResponse200")



@_attrs_define
class ApiAccountPlayingResponse200:
    """ 
        Example:
            {'nowPlaying': [{'gameId': 'rCRw1AuO', 'fullId': 'rCRw1AuOvonq', 'color': 'black', 'fen':
                'r1bqkbnr/pppp2pp/2n1pp2/8/8/3PP3/PPPB1PPP/RN1QKBNR w KQkq - 2 4', 'hasMoved': True, 'isMyTurn': False,
                'lastMove': 'b8c6', 'opponent': {'id': 'philippe', 'rating': 1790, 'username': 'Philippe'}, 'perf':
                'correspondence', 'rated': False, 'secondsLeft': 1209600, 'source': 'friend', 'speed': 'correspondence',
                'variant': {'key': 'standard', 'name': 'Standard'}}]}

        Attributes:
            now_playing (list['ApiAccountPlayingResponse200NowPlayingItem']):
     """

    now_playing: list['ApiAccountPlayingResponse200NowPlayingItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_account_playing_response_200_now_playing_item import ApiAccountPlayingResponse200NowPlayingItem
        now_playing = []
        for now_playing_item_data in self.now_playing:
            now_playing_item = now_playing_item_data.to_dict()
            now_playing.append(now_playing_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "nowPlaying": now_playing,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_account_playing_response_200_now_playing_item import ApiAccountPlayingResponse200NowPlayingItem
        d = dict(src_dict)
        now_playing = []
        _now_playing = d.pop("nowPlaying")
        for now_playing_item_data in (_now_playing):
            now_playing_item = ApiAccountPlayingResponse200NowPlayingItem.from_dict(now_playing_item_data)



            now_playing.append(now_playing_item)


        api_account_playing_response_200 = cls(
            now_playing=now_playing,
        )


        api_account_playing_response_200.additional_properties = d
        return api_account_playing_response_200

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
