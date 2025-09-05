from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_tour_get_response_200_tour import BroadcastTourGetResponse200Tour
  from ..models.broadcast_tour_get_response_200_rounds_item import BroadcastTourGetResponse200RoundsItem
  from ..models.broadcast_tour_get_response_200_group import BroadcastTourGetResponse200Group





T = TypeVar("T", bound="BroadcastTourGetResponse200")



@_attrs_define
class BroadcastTourGetResponse200:
    """ 
        Attributes:
            tour (BroadcastTourGetResponse200Tour):
            rounds (list['BroadcastTourGetResponse200RoundsItem']):
            group (Union[Unset, BroadcastTourGetResponse200Group]):
            default_round_id (Union[Unset, str]):
     """

    tour: 'BroadcastTourGetResponse200Tour'
    rounds: list['BroadcastTourGetResponse200RoundsItem']
    group: Union[Unset, 'BroadcastTourGetResponse200Group'] = UNSET
    default_round_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_tour_get_response_200_tour import BroadcastTourGetResponse200Tour
        from ..models.broadcast_tour_get_response_200_rounds_item import BroadcastTourGetResponse200RoundsItem
        from ..models.broadcast_tour_get_response_200_group import BroadcastTourGetResponse200Group
        tour = self.tour.to_dict()

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)



        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        default_round_id = self.default_round_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tour": tour,
            "rounds": rounds,
        })
        if group is not UNSET:
            field_dict["group"] = group
        if default_round_id is not UNSET:
            field_dict["defaultRoundId"] = default_round_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_tour_get_response_200_tour import BroadcastTourGetResponse200Tour
        from ..models.broadcast_tour_get_response_200_rounds_item import BroadcastTourGetResponse200RoundsItem
        from ..models.broadcast_tour_get_response_200_group import BroadcastTourGetResponse200Group
        d = dict(src_dict)
        tour = BroadcastTourGetResponse200Tour.from_dict(d.pop("tour"))




        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in (_rounds):
            rounds_item = BroadcastTourGetResponse200RoundsItem.from_dict(rounds_item_data)



            rounds.append(rounds_item)


        _group = d.pop("group", UNSET)
        group: Union[Unset, BroadcastTourGetResponse200Group]
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = BroadcastTourGetResponse200Group.from_dict(_group)




        default_round_id = d.pop("defaultRoundId", UNSET)

        broadcast_tour_get_response_200 = cls(
            tour=tour,
            rounds=rounds,
            group=group,
            default_round_id=default_round_id,
        )


        broadcast_tour_get_response_200.additional_properties = d
        return broadcast_tour_get_response_200

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
