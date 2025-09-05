from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_tournament_response_200_created_item import ApiTournamentResponse200CreatedItem
  from ..models.api_tournament_response_200_started_item import ApiTournamentResponse200StartedItem
  from ..models.api_tournament_response_200_finished_item import ApiTournamentResponse200FinishedItem





T = TypeVar("T", bound="ApiTournamentResponse200")



@_attrs_define
class ApiTournamentResponse200:
    """ 
        Attributes:
            created (Union[Unset, list['ApiTournamentResponse200CreatedItem']]):
            started (Union[Unset, list['ApiTournamentResponse200StartedItem']]):
            finished (Union[Unset, list['ApiTournamentResponse200FinishedItem']]):
     """

    created: Union[Unset, list['ApiTournamentResponse200CreatedItem']] = UNSET
    started: Union[Unset, list['ApiTournamentResponse200StartedItem']] = UNSET
    finished: Union[Unset, list['ApiTournamentResponse200FinishedItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_tournament_response_200_created_item import ApiTournamentResponse200CreatedItem
        from ..models.api_tournament_response_200_started_item import ApiTournamentResponse200StartedItem
        from ..models.api_tournament_response_200_finished_item import ApiTournamentResponse200FinishedItem
        created: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.created, Unset):
            created = []
            for created_item_data in self.created:
                created_item = created_item_data.to_dict()
                created.append(created_item)



        started: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.started, Unset):
            started = []
            for started_item_data in self.started:
                started_item = started_item_data.to_dict()
                started.append(started_item)



        finished: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.finished, Unset):
            finished = []
            for finished_item_data in self.finished:
                finished_item = finished_item_data.to_dict()
                finished.append(finished_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created is not UNSET:
            field_dict["created"] = created
        if started is not UNSET:
            field_dict["started"] = started
        if finished is not UNSET:
            field_dict["finished"] = finished

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_tournament_response_200_created_item import ApiTournamentResponse200CreatedItem
        from ..models.api_tournament_response_200_started_item import ApiTournamentResponse200StartedItem
        from ..models.api_tournament_response_200_finished_item import ApiTournamentResponse200FinishedItem
        d = dict(src_dict)
        created = []
        _created = d.pop("created", UNSET)
        for created_item_data in (_created or []):
            created_item = ApiTournamentResponse200CreatedItem.from_dict(created_item_data)



            created.append(created_item)


        started = []
        _started = d.pop("started", UNSET)
        for started_item_data in (_started or []):
            started_item = ApiTournamentResponse200StartedItem.from_dict(started_item_data)



            started.append(started_item)


        finished = []
        _finished = d.pop("finished", UNSET)
        for finished_item_data in (_finished or []):
            finished_item = ApiTournamentResponse200FinishedItem.from_dict(finished_item_data)



            finished.append(finished_item)


        api_tournament_response_200 = cls(
            created=created,
            started=started,
            finished=finished,
        )


        api_tournament_response_200.additional_properties = d
        return api_tournament_response_200

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
