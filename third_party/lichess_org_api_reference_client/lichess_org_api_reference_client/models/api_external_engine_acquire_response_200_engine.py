from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_external_engine_acquire_response_200_engine_variants_item import ApiExternalEngineAcquireResponse200EngineVariantsItem
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ApiExternalEngineAcquireResponse200Engine")



@_attrs_define
class ApiExternalEngineAcquireResponse200Engine:
    """ 
        Attributes:
            id (str): Unique engine registration ID.
            name (str): Display name of the engine.
            client_secret (str): A secret token that can be used to
                [*request* analysis](#tag/External-engine/operation/apiExternalEngineAnalyse)
                from this external engine.
            user_id (str): The user this engine has been registered for.
            max_threads (int): Maximum number of available threads.
            max_hash (int): Maximum available hash table size, in MiB.
            variants (list[ApiExternalEngineAcquireResponse200EngineVariantsItem]): List of supported chess variants.
            provider_data (Union[None, Unset, str]): Arbitrary data that the engine provider can use for identification
                or bookkeeping.

                Users can read this information, but updating it requires knowing
                or changing the `providerSecret`.
     """

    id: str
    name: str
    client_secret: str
    user_id: str
    max_threads: int
    max_hash: int
    variants: list[ApiExternalEngineAcquireResponse200EngineVariantsItem]
    provider_data: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        client_secret = self.client_secret

        user_id = self.user_id

        max_threads = self.max_threads

        max_hash = self.max_hash

        variants = []
        for variants_item_data in self.variants:
            variants_item = variants_item_data.value
            variants.append(variants_item)



        provider_data: Union[None, Unset, str]
        if isinstance(self.provider_data, Unset):
            provider_data = UNSET
        else:
            provider_data = self.provider_data


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "clientSecret": client_secret,
            "userId": user_id,
            "maxThreads": max_threads,
            "maxHash": max_hash,
            "variants": variants,
        })
        if provider_data is not UNSET:
            field_dict["providerData"] = provider_data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        client_secret = d.pop("clientSecret")

        user_id = d.pop("userId")

        max_threads = d.pop("maxThreads")

        max_hash = d.pop("maxHash")

        variants = []
        _variants = d.pop("variants")
        for variants_item_data in (_variants):
            variants_item = ApiExternalEngineAcquireResponse200EngineVariantsItem(variants_item_data)



            variants.append(variants_item)


        def _parse_provider_data(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_data = _parse_provider_data(d.pop("providerData", UNSET))


        api_external_engine_acquire_response_200_engine = cls(
            id=id,
            name=name,
            client_secret=client_secret,
            user_id=user_id,
            max_threads=max_threads,
            max_hash=max_hash,
            variants=variants,
            provider_data=provider_data,
        )


        api_external_engine_acquire_response_200_engine.additional_properties = d
        return api_external_engine_acquire_response_200_engine

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
