from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.simul_host import SimulHost
  from ..models.simul_variants_item import SimulVariantsItem





T = TypeVar("T", bound="Simul")



@_attrs_define
class Simul:
    """ 
        Attributes:
            id (str):
            host (SimulHost):
            name (str):
            full_name (str):
            variants (list['SimulVariantsItem']):
            is_created (bool):
            is_finished (bool):
            is_running (bool):
            nb_applicants (int):
            nb_pairings (int):
            text (Union[Unset, str]):
            estimated_start_at (Union[Unset, int]):
            started_at (Union[Unset, int]):
            finished_at (Union[Unset, int]):
     """

    id: str
    host: 'SimulHost'
    name: str
    full_name: str
    variants: list['SimulVariantsItem']
    is_created: bool
    is_finished: bool
    is_running: bool
    nb_applicants: int
    nb_pairings: int
    text: Union[Unset, str] = UNSET
    estimated_start_at: Union[Unset, int] = UNSET
    started_at: Union[Unset, int] = UNSET
    finished_at: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.simul_host import SimulHost
        from ..models.simul_variants_item import SimulVariantsItem
        id = self.id

        host = self.host.to_dict()

        name = self.name

        full_name = self.full_name

        variants = []
        for variants_item_data in self.variants:
            variants_item = variants_item_data.to_dict()
            variants.append(variants_item)



        is_created = self.is_created

        is_finished = self.is_finished

        is_running = self.is_running

        nb_applicants = self.nb_applicants

        nb_pairings = self.nb_pairings

        text = self.text

        estimated_start_at = self.estimated_start_at

        started_at = self.started_at

        finished_at = self.finished_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "host": host,
            "name": name,
            "fullName": full_name,
            "variants": variants,
            "isCreated": is_created,
            "isFinished": is_finished,
            "isRunning": is_running,
            "nbApplicants": nb_applicants,
            "nbPairings": nb_pairings,
        })
        if text is not UNSET:
            field_dict["text"] = text
        if estimated_start_at is not UNSET:
            field_dict["estimatedStartAt"] = estimated_start_at
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simul_host import SimulHost
        from ..models.simul_variants_item import SimulVariantsItem
        d = dict(src_dict)
        id = d.pop("id")

        host = SimulHost.from_dict(d.pop("host"))




        name = d.pop("name")

        full_name = d.pop("fullName")

        variants = []
        _variants = d.pop("variants")
        for variants_item_data in (_variants):
            variants_item = SimulVariantsItem.from_dict(variants_item_data)



            variants.append(variants_item)


        is_created = d.pop("isCreated")

        is_finished = d.pop("isFinished")

        is_running = d.pop("isRunning")

        nb_applicants = d.pop("nbApplicants")

        nb_pairings = d.pop("nbPairings")

        text = d.pop("text", UNSET)

        estimated_start_at = d.pop("estimatedStartAt", UNSET)

        started_at = d.pop("startedAt", UNSET)

        finished_at = d.pop("finishedAt", UNSET)

        simul = cls(
            id=id,
            host=host,
            name=name,
            full_name=full_name,
            variants=variants,
            is_created=is_created,
            is_finished=is_finished,
            is_running=is_running,
            nb_applicants=nb_applicants,
            nb_pairings=nb_pairings,
            text=text,
            estimated_start_at=estimated_start_at,
            started_at=started_at,
            finished_at=finished_at,
        )


        simul.additional_properties = d
        return simul

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
