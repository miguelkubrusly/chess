from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_top_past_current_page_results_item_tour_info import BroadcastTopPastCurrentPageResultsItemTourInfo





T = TypeVar("T", bound="BroadcastTopPastCurrentPageResultsItemTour")



@_attrs_define
class BroadcastTopPastCurrentPageResultsItemTour:
    """ 
        Attributes:
            id (str):
            name (str):
            slug (str):
            created_at (int):  Example: 1722169800000.
            url (str):
            dates (Union[Unset, list[int]]): Start and end dates of the tournament, as Unix timestamps in milliseconds
                Example: [1722169800000, 1722666600000].
            info (Union[Unset, BroadcastTopPastCurrentPageResultsItemTourInfo]): Additional display information about the
                tournament
            tier (Union[Unset, float]): Used to designate featured tournaments on Lichess
            image (Union[Unset, str]):
            description (Union[Unset, str]): Full tournament description in markdown format, or in HTML if the html=1 query
                parameter is set.
            leaderboard (Union[Unset, bool]):
            team_table (Union[Unset, bool]):
     """

    id: str
    name: str
    slug: str
    created_at: int
    url: str
    dates: Union[Unset, list[int]] = UNSET
    info: Union[Unset, 'BroadcastTopPastCurrentPageResultsItemTourInfo'] = UNSET
    tier: Union[Unset, float] = UNSET
    image: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    leaderboard: Union[Unset, bool] = UNSET
    team_table: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_top_past_current_page_results_item_tour_info import BroadcastTopPastCurrentPageResultsItemTourInfo
        id = self.id

        name = self.name

        slug = self.slug

        created_at = self.created_at

        url = self.url

        dates: Union[Unset, list[int]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates



        info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        tier = self.tier

        image = self.image

        description = self.description

        leaderboard = self.leaderboard

        team_table = self.team_table


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "slug": slug,
            "createdAt": created_at,
            "url": url,
        })
        if dates is not UNSET:
            field_dict["dates"] = dates
        if info is not UNSET:
            field_dict["info"] = info
        if tier is not UNSET:
            field_dict["tier"] = tier
        if image is not UNSET:
            field_dict["image"] = image
        if description is not UNSET:
            field_dict["description"] = description
        if leaderboard is not UNSET:
            field_dict["leaderboard"] = leaderboard
        if team_table is not UNSET:
            field_dict["teamTable"] = team_table

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_top_past_current_page_results_item_tour_info import BroadcastTopPastCurrentPageResultsItemTourInfo
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        created_at = d.pop("createdAt")

        url = d.pop("url")

        dates = cast(list[int], d.pop("dates", UNSET))


        _info = d.pop("info", UNSET)
        info: Union[Unset, BroadcastTopPastCurrentPageResultsItemTourInfo]
        if isinstance(_info,  Unset):
            info = UNSET
        else:
            info = BroadcastTopPastCurrentPageResultsItemTourInfo.from_dict(_info)




        tier = d.pop("tier", UNSET)

        image = d.pop("image", UNSET)

        description = d.pop("description", UNSET)

        leaderboard = d.pop("leaderboard", UNSET)

        team_table = d.pop("teamTable", UNSET)

        broadcast_top_past_current_page_results_item_tour = cls(
            id=id,
            name=name,
            slug=slug,
            created_at=created_at,
            url=url,
            dates=dates,
            info=info,
            tier=tier,
            image=image,
            description=description,
            leaderboard=leaderboard,
            team_table=team_table,
        )


        broadcast_top_past_current_page_results_item_tour.additional_properties = d
        return broadcast_top_past_current_page_results_item_tour

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
