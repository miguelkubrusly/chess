from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.team_search_response_200_current_page_results_item_leaders_item import TeamSearchResponse200CurrentPageResultsItemLeadersItem
  from ..models.team_search_response_200_current_page_results_item_leader import TeamSearchResponse200CurrentPageResultsItemLeader





T = TypeVar("T", bound="TeamSearchResponse200CurrentPageResultsItem")



@_attrs_define
class TeamSearchResponse200CurrentPageResultsItem:
    """ 
        Attributes:
            id (str):
            name (str):
            description (Union[Unset, str]):
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            leader (Union[Unset, TeamSearchResponse200CurrentPageResultsItemLeader]):
            leaders (Union[Unset, list['TeamSearchResponse200CurrentPageResultsItemLeadersItem']]):
            nb_members (Union[Unset, int]):
            open_ (Union[Unset, bool]):
            joined (Union[Unset, bool]):
            requested (Union[Unset, bool]):
     """

    id: str
    name: str
    description: Union[Unset, str] = UNSET
    flair: Union[Unset, str] = UNSET
    leader: Union[Unset, 'TeamSearchResponse200CurrentPageResultsItemLeader'] = UNSET
    leaders: Union[Unset, list['TeamSearchResponse200CurrentPageResultsItemLeadersItem']] = UNSET
    nb_members: Union[Unset, int] = UNSET
    open_: Union[Unset, bool] = UNSET
    joined: Union[Unset, bool] = UNSET
    requested: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_search_response_200_current_page_results_item_leaders_item import TeamSearchResponse200CurrentPageResultsItemLeadersItem
        from ..models.team_search_response_200_current_page_results_item_leader import TeamSearchResponse200CurrentPageResultsItemLeader
        id = self.id

        name = self.name

        description = self.description

        flair = self.flair

        leader: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.leader, Unset):
            leader = self.leader.to_dict()

        leaders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.leaders, Unset):
            leaders = []
            for leaders_item_data in self.leaders:
                leaders_item = leaders_item_data.to_dict()
                leaders.append(leaders_item)



        nb_members = self.nb_members

        open_ = self.open_

        joined = self.joined

        requested = self.requested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if flair is not UNSET:
            field_dict["flair"] = flair
        if leader is not UNSET:
            field_dict["leader"] = leader
        if leaders is not UNSET:
            field_dict["leaders"] = leaders
        if nb_members is not UNSET:
            field_dict["nbMembers"] = nb_members
        if open_ is not UNSET:
            field_dict["open"] = open_
        if joined is not UNSET:
            field_dict["joined"] = joined
        if requested is not UNSET:
            field_dict["requested"] = requested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_search_response_200_current_page_results_item_leaders_item import TeamSearchResponse200CurrentPageResultsItemLeadersItem
        from ..models.team_search_response_200_current_page_results_item_leader import TeamSearchResponse200CurrentPageResultsItemLeader
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        flair = d.pop("flair", UNSET)

        _leader = d.pop("leader", UNSET)
        leader: Union[Unset, TeamSearchResponse200CurrentPageResultsItemLeader]
        if isinstance(_leader,  Unset):
            leader = UNSET
        else:
            leader = TeamSearchResponse200CurrentPageResultsItemLeader.from_dict(_leader)




        leaders = []
        _leaders = d.pop("leaders", UNSET)
        for leaders_item_data in (_leaders or []):
            leaders_item = TeamSearchResponse200CurrentPageResultsItemLeadersItem.from_dict(leaders_item_data)



            leaders.append(leaders_item)


        nb_members = d.pop("nbMembers", UNSET)

        open_ = d.pop("open", UNSET)

        joined = d.pop("joined", UNSET)

        requested = d.pop("requested", UNSET)

        team_search_response_200_current_page_results_item = cls(
            id=id,
            name=name,
            description=description,
            flair=flair,
            leader=leader,
            leaders=leaders,
            nb_members=nb_members,
            open_=open_,
            joined=joined,
            requested=requested,
        )


        team_search_response_200_current_page_results_item.additional_properties = d
        return team_search_response_200_current_page_results_item

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
