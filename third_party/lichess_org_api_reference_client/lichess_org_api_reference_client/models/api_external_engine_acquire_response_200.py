from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.api_external_engine_acquire_response_200_work_type_0 import ApiExternalEngineAcquireResponse200WorkType0
  from ..models.api_external_engine_acquire_response_200_work_type_1 import ApiExternalEngineAcquireResponse200WorkType1
  from ..models.api_external_engine_acquire_response_200_engine import ApiExternalEngineAcquireResponse200Engine
  from ..models.api_external_engine_acquire_response_200_work_type_2 import ApiExternalEngineAcquireResponse200WorkType2





T = TypeVar("T", bound="ApiExternalEngineAcquireResponse200")



@_attrs_define
class ApiExternalEngineAcquireResponse200:
    """ 
        Attributes:
            id (str):  Example: aingoohiJee2sius.
            work (Union['ApiExternalEngineAcquireResponse200WorkType0', 'ApiExternalEngineAcquireResponse200WorkType1',
                'ApiExternalEngineAcquireResponse200WorkType2']):
            engine (ApiExternalEngineAcquireResponse200Engine):
     """

    id: str
    work: Union['ApiExternalEngineAcquireResponse200WorkType0', 'ApiExternalEngineAcquireResponse200WorkType1', 'ApiExternalEngineAcquireResponse200WorkType2']
    engine: 'ApiExternalEngineAcquireResponse200Engine'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_external_engine_acquire_response_200_work_type_0 import ApiExternalEngineAcquireResponse200WorkType0
        from ..models.api_external_engine_acquire_response_200_work_type_1 import ApiExternalEngineAcquireResponse200WorkType1
        from ..models.api_external_engine_acquire_response_200_engine import ApiExternalEngineAcquireResponse200Engine
        from ..models.api_external_engine_acquire_response_200_work_type_2 import ApiExternalEngineAcquireResponse200WorkType2
        id = self.id

        work: dict[str, Any]
        if isinstance(self.work, ApiExternalEngineAcquireResponse200WorkType0):
            work = self.work.to_dict()
        elif isinstance(self.work, ApiExternalEngineAcquireResponse200WorkType1):
            work = self.work.to_dict()
        else:
            work = self.work.to_dict()


        engine = self.engine.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "work": work,
            "engine": engine,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_external_engine_acquire_response_200_work_type_0 import ApiExternalEngineAcquireResponse200WorkType0
        from ..models.api_external_engine_acquire_response_200_work_type_1 import ApiExternalEngineAcquireResponse200WorkType1
        from ..models.api_external_engine_acquire_response_200_engine import ApiExternalEngineAcquireResponse200Engine
        from ..models.api_external_engine_acquire_response_200_work_type_2 import ApiExternalEngineAcquireResponse200WorkType2
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_work(data: object) -> Union['ApiExternalEngineAcquireResponse200WorkType0', 'ApiExternalEngineAcquireResponse200WorkType1', 'ApiExternalEngineAcquireResponse200WorkType2']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                work_type_0 = ApiExternalEngineAcquireResponse200WorkType0.from_dict(data)



                return work_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                work_type_1 = ApiExternalEngineAcquireResponse200WorkType1.from_dict(data)



                return work_type_1
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            work_type_2 = ApiExternalEngineAcquireResponse200WorkType2.from_dict(data)



            return work_type_2

        work = _parse_work(d.pop("work"))


        engine = ApiExternalEngineAcquireResponse200Engine.from_dict(d.pop("engine"))




        api_external_engine_acquire_response_200 = cls(
            id=id,
            work=work,
            engine=engine,
        )


        api_external_engine_acquire_response_200.additional_properties = d
        return api_external_engine_acquire_response_200

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
