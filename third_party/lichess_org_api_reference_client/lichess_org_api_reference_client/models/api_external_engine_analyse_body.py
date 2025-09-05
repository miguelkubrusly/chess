from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.api_external_engine_analyse_body_work_type_0 import ApiExternalEngineAnalyseBodyWorkType0
  from ..models.api_external_engine_analyse_body_work_type_1 import ApiExternalEngineAnalyseBodyWorkType1
  from ..models.api_external_engine_analyse_body_work_type_2 import ApiExternalEngineAnalyseBodyWorkType2





T = TypeVar("T", bound="ApiExternalEngineAnalyseBody")



@_attrs_define
class ApiExternalEngineAnalyseBody:
    """ 
        Attributes:
            client_secret (str):  Example: ees_mdF2hK0hlKGSPeC6.
            work (Union['ApiExternalEngineAnalyseBodyWorkType0', 'ApiExternalEngineAnalyseBodyWorkType1',
                'ApiExternalEngineAnalyseBodyWorkType2']):
     """

    client_secret: str
    work: Union['ApiExternalEngineAnalyseBodyWorkType0', 'ApiExternalEngineAnalyseBodyWorkType1', 'ApiExternalEngineAnalyseBodyWorkType2']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_external_engine_analyse_body_work_type_0 import ApiExternalEngineAnalyseBodyWorkType0
        from ..models.api_external_engine_analyse_body_work_type_1 import ApiExternalEngineAnalyseBodyWorkType1
        from ..models.api_external_engine_analyse_body_work_type_2 import ApiExternalEngineAnalyseBodyWorkType2
        client_secret = self.client_secret

        work: dict[str, Any]
        if isinstance(self.work, ApiExternalEngineAnalyseBodyWorkType0):
            work = self.work.to_dict()
        elif isinstance(self.work, ApiExternalEngineAnalyseBodyWorkType1):
            work = self.work.to_dict()
        else:
            work = self.work.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "clientSecret": client_secret,
            "work": work,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_external_engine_analyse_body_work_type_0 import ApiExternalEngineAnalyseBodyWorkType0
        from ..models.api_external_engine_analyse_body_work_type_1 import ApiExternalEngineAnalyseBodyWorkType1
        from ..models.api_external_engine_analyse_body_work_type_2 import ApiExternalEngineAnalyseBodyWorkType2
        d = dict(src_dict)
        client_secret = d.pop("clientSecret")

        def _parse_work(data: object) -> Union['ApiExternalEngineAnalyseBodyWorkType0', 'ApiExternalEngineAnalyseBodyWorkType1', 'ApiExternalEngineAnalyseBodyWorkType2']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                work_type_0 = ApiExternalEngineAnalyseBodyWorkType0.from_dict(data)



                return work_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                work_type_1 = ApiExternalEngineAnalyseBodyWorkType1.from_dict(data)



                return work_type_1
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            work_type_2 = ApiExternalEngineAnalyseBodyWorkType2.from_dict(data)



            return work_type_2

        work = _parse_work(d.pop("work"))


        api_external_engine_analyse_body = cls(
            client_secret=client_secret,
            work=work,
        )


        api_external_engine_analyse_body.additional_properties = d
        return api_external_engine_analyse_body

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
