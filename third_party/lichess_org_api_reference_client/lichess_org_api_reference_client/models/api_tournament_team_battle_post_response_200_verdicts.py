from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_tournament_team_battle_post_response_200_verdicts_list_item import ApiTournamentTeamBattlePostResponse200VerdictsListItem





T = TypeVar("T", bound="ApiTournamentTeamBattlePostResponse200Verdicts")



@_attrs_define
class ApiTournamentTeamBattlePostResponse200Verdicts:
    """ 
        Attributes:
            accepted (bool):
            list_ (list['ApiTournamentTeamBattlePostResponse200VerdictsListItem']):
     """

    accepted: bool
    list_: list['ApiTournamentTeamBattlePostResponse200VerdictsListItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_tournament_team_battle_post_response_200_verdicts_list_item import ApiTournamentTeamBattlePostResponse200VerdictsListItem
        accepted = self.accepted

        list_ = []
        for list_item_data in self.list_:
            list_item = list_item_data.to_dict()
            list_.append(list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "accepted": accepted,
            "list": list_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_tournament_team_battle_post_response_200_verdicts_list_item import ApiTournamentTeamBattlePostResponse200VerdictsListItem
        d = dict(src_dict)
        accepted = d.pop("accepted")

        list_ = []
        _list_ = d.pop("list")
        for list_item_data in (_list_):
            list_item = ApiTournamentTeamBattlePostResponse200VerdictsListItem.from_dict(list_item_data)



            list_.append(list_item)


        api_tournament_team_battle_post_response_200_verdicts = cls(
            accepted=accepted,
            list_=list_,
        )


        api_tournament_team_battle_post_response_200_verdicts.additional_properties = d
        return api_tournament_team_battle_post_response_200_verdicts

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
