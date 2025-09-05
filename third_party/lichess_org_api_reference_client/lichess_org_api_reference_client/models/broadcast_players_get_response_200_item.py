from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.broadcast_players_get_response_200_item_title import BroadcastPlayersGetResponse200ItemTitle
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_players_get_response_200_item_tiebreaks_item import BroadcastPlayersGetResponse200ItemTiebreaksItem





T = TypeVar("T", bound="BroadcastPlayersGetResponse200Item")



@_attrs_define
class BroadcastPlayersGetResponse200Item:
    """ 
        Attributes:
            name (Union[Unset, str]):  Example: Hernandez Riera, Jose.
            score (Union[Unset, float]):  Example: 2.5.
            played (Union[Unset, int]):  Example: 7.
            rating (Union[Unset, int]):  Example: 2149.
            rating_diff (Union[Unset, int]):  Example: -5.
            performance (Union[Unset, int]):  Example: 2138.
            title (Union[Unset, BroadcastPlayersGetResponse200ItemTitle]): only appears if the user is a titled player or a
                bot user Example: FM.
            fide_id (Union[Unset, int]):  Example: 3408230.
            fed (Union[Unset, str]):  Example: CHI.
            tiebreaks (Union[Unset, list['BroadcastPlayersGetResponse200ItemTiebreaksItem']]):
            rank (Union[Unset, int]):  Example: 1.
     """

    name: Union[Unset, str] = UNSET
    score: Union[Unset, float] = UNSET
    played: Union[Unset, int] = UNSET
    rating: Union[Unset, int] = UNSET
    rating_diff: Union[Unset, int] = UNSET
    performance: Union[Unset, int] = UNSET
    title: Union[Unset, BroadcastPlayersGetResponse200ItemTitle] = UNSET
    fide_id: Union[Unset, int] = UNSET
    fed: Union[Unset, str] = UNSET
    tiebreaks: Union[Unset, list['BroadcastPlayersGetResponse200ItemTiebreaksItem']] = UNSET
    rank: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_players_get_response_200_item_tiebreaks_item import BroadcastPlayersGetResponse200ItemTiebreaksItem
        name = self.name

        score = self.score

        played = self.played

        rating = self.rating

        rating_diff = self.rating_diff

        performance = self.performance

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value


        fide_id = self.fide_id

        fed = self.fed

        tiebreaks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tiebreaks, Unset):
            tiebreaks = []
            for tiebreaks_item_data in self.tiebreaks:
                tiebreaks_item = tiebreaks_item_data.to_dict()
                tiebreaks.append(tiebreaks_item)



        rank = self.rank


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if score is not UNSET:
            field_dict["score"] = score
        if played is not UNSET:
            field_dict["played"] = played
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_diff is not UNSET:
            field_dict["ratingDiff"] = rating_diff
        if performance is not UNSET:
            field_dict["performance"] = performance
        if title is not UNSET:
            field_dict["title"] = title
        if fide_id is not UNSET:
            field_dict["fideId"] = fide_id
        if fed is not UNSET:
            field_dict["fed"] = fed
        if tiebreaks is not UNSET:
            field_dict["tiebreaks"] = tiebreaks
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_players_get_response_200_item_tiebreaks_item import BroadcastPlayersGetResponse200ItemTiebreaksItem
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        score = d.pop("score", UNSET)

        played = d.pop("played", UNSET)

        rating = d.pop("rating", UNSET)

        rating_diff = d.pop("ratingDiff", UNSET)

        performance = d.pop("performance", UNSET)

        _title = d.pop("title", UNSET)
        title: Union[Unset, BroadcastPlayersGetResponse200ItemTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = BroadcastPlayersGetResponse200ItemTitle(_title)




        fide_id = d.pop("fideId", UNSET)

        fed = d.pop("fed", UNSET)

        tiebreaks = []
        _tiebreaks = d.pop("tiebreaks", UNSET)
        for tiebreaks_item_data in (_tiebreaks or []):
            tiebreaks_item = BroadcastPlayersGetResponse200ItemTiebreaksItem.from_dict(tiebreaks_item_data)



            tiebreaks.append(tiebreaks_item)


        rank = d.pop("rank", UNSET)

        broadcast_players_get_response_200_item = cls(
            name=name,
            score=score,
            played=played,
            rating=rating,
            rating_diff=rating_diff,
            performance=performance,
            title=title,
            fide_id=fide_id,
            fed=fed,
            tiebreaks=tiebreaks,
            rank=rank,
        )


        broadcast_players_get_response_200_item.additional_properties = d
        return broadcast_players_get_response_200_item

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
