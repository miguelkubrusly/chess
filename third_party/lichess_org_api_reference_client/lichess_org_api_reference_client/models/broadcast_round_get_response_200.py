from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_round_get_response_200_games_item import BroadcastRoundGetResponse200GamesItem
  from ..models.broadcast_round_get_response_200_study import BroadcastRoundGetResponse200Study
  from ..models.broadcast_round_get_response_200_tour import BroadcastRoundGetResponse200Tour
  from ..models.broadcast_round_get_response_200_group import BroadcastRoundGetResponse200Group
  from ..models.broadcast_round_get_response_200_round import BroadcastRoundGetResponse200Round





T = TypeVar("T", bound="BroadcastRoundGetResponse200")



@_attrs_define
class BroadcastRoundGetResponse200:
    """ 
        Attributes:
            round_ (BroadcastRoundGetResponse200Round):
            tour (BroadcastRoundGetResponse200Tour):
            study (BroadcastRoundGetResponse200Study):
            games (list['BroadcastRoundGetResponse200GamesItem']):
            group (Union[Unset, BroadcastRoundGetResponse200Group]):
     """

    round_: 'BroadcastRoundGetResponse200Round'
    tour: 'BroadcastRoundGetResponse200Tour'
    study: 'BroadcastRoundGetResponse200Study'
    games: list['BroadcastRoundGetResponse200GamesItem']
    group: Union[Unset, 'BroadcastRoundGetResponse200Group'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_round_get_response_200_games_item import BroadcastRoundGetResponse200GamesItem
        from ..models.broadcast_round_get_response_200_study import BroadcastRoundGetResponse200Study
        from ..models.broadcast_round_get_response_200_tour import BroadcastRoundGetResponse200Tour
        from ..models.broadcast_round_get_response_200_group import BroadcastRoundGetResponse200Group
        from ..models.broadcast_round_get_response_200_round import BroadcastRoundGetResponse200Round
        round_ = self.round_.to_dict()

        tour = self.tour.to_dict()

        study = self.study.to_dict()

        games = []
        for games_item_data in self.games:
            games_item = games_item_data.to_dict()
            games.append(games_item)



        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "round": round_,
            "tour": tour,
            "study": study,
            "games": games,
        })
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_round_get_response_200_games_item import BroadcastRoundGetResponse200GamesItem
        from ..models.broadcast_round_get_response_200_study import BroadcastRoundGetResponse200Study
        from ..models.broadcast_round_get_response_200_tour import BroadcastRoundGetResponse200Tour
        from ..models.broadcast_round_get_response_200_group import BroadcastRoundGetResponse200Group
        from ..models.broadcast_round_get_response_200_round import BroadcastRoundGetResponse200Round
        d = dict(src_dict)
        round_ = BroadcastRoundGetResponse200Round.from_dict(d.pop("round"))




        tour = BroadcastRoundGetResponse200Tour.from_dict(d.pop("tour"))




        study = BroadcastRoundGetResponse200Study.from_dict(d.pop("study"))




        games = []
        _games = d.pop("games")
        for games_item_data in (_games):
            games_item = BroadcastRoundGetResponse200GamesItem.from_dict(games_item_data)



            games.append(games_item)


        _group = d.pop("group", UNSET)
        group: Union[Unset, BroadcastRoundGetResponse200Group]
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = BroadcastRoundGetResponse200Group.from_dict(_group)




        broadcast_round_get_response_200 = cls(
            round_=round_,
            tour=tour,
            study=study,
            games=games,
            group=group,
        )


        broadcast_round_get_response_200.additional_properties = d
        return broadcast_round_get_response_200

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
