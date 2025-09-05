from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.arena_tournament_full_podium_item_title import ArenaTournamentFullPodiumItemTitle
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.arena_tournament_full_podium_item_nb import ArenaTournamentFullPodiumItemNb





T = TypeVar("T", bound="ArenaTournamentFullPodiumItem")



@_attrs_define
class ArenaTournamentFullPodiumItem:
    """ 
        Attributes:
            name (Union[Unset, str]):
            title (Union[Unset, ArenaTournamentFullPodiumItemTitle]): only appears if the user is a titled player or a bot
                user
            patron (Union[Unset, bool]):
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            rank (Union[Unset, float]):
            rating (Union[Unset, float]):
            score (Union[Unset, float]):
            nb (Union[Unset, ArenaTournamentFullPodiumItemNb]):
            performance (Union[Unset, float]):
     """

    name: Union[Unset, str] = UNSET
    title: Union[Unset, ArenaTournamentFullPodiumItemTitle] = UNSET
    patron: Union[Unset, bool] = UNSET
    flair: Union[Unset, str] = UNSET
    rank: Union[Unset, float] = UNSET
    rating: Union[Unset, float] = UNSET
    score: Union[Unset, float] = UNSET
    nb: Union[Unset, 'ArenaTournamentFullPodiumItemNb'] = UNSET
    performance: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.arena_tournament_full_podium_item_nb import ArenaTournamentFullPodiumItemNb
        name = self.name

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value


        patron = self.patron

        flair = self.flair

        rank = self.rank

        rating = self.rating

        score = self.score

        nb: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nb, Unset):
            nb = self.nb.to_dict()

        performance = self.performance


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if patron is not UNSET:
            field_dict["patron"] = patron
        if flair is not UNSET:
            field_dict["flair"] = flair
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rating is not UNSET:
            field_dict["rating"] = rating
        if score is not UNSET:
            field_dict["score"] = score
        if nb is not UNSET:
            field_dict["nb"] = nb
        if performance is not UNSET:
            field_dict["performance"] = performance

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.arena_tournament_full_podium_item_nb import ArenaTournamentFullPodiumItemNb
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _title = d.pop("title", UNSET)
        title: Union[Unset, ArenaTournamentFullPodiumItemTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = ArenaTournamentFullPodiumItemTitle(_title)




        patron = d.pop("patron", UNSET)

        flair = d.pop("flair", UNSET)

        rank = d.pop("rank", UNSET)

        rating = d.pop("rating", UNSET)

        score = d.pop("score", UNSET)

        _nb = d.pop("nb", UNSET)
        nb: Union[Unset, ArenaTournamentFullPodiumItemNb]
        if isinstance(_nb,  Unset):
            nb = UNSET
        else:
            nb = ArenaTournamentFullPodiumItemNb.from_dict(_nb)




        performance = d.pop("performance", UNSET)

        arena_tournament_full_podium_item = cls(
            name=name,
            title=title,
            patron=patron,
            flair=flair,
            rank=rank,
            rating=rating,
            score=score,
            nb=nb,
            performance=performance,
        )


        arena_tournament_full_podium_item.additional_properties = d
        return arena_tournament_full_podium_item

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
