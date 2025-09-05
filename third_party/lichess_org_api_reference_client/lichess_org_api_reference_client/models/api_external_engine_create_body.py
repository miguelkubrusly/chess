from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_external_engine_create_body_variants_item import ApiExternalEngineCreateBodyVariantsItem
from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="ApiExternalEngineCreateBody")



@_attrs_define
class ApiExternalEngineCreateBody:
    """ 
        Attributes:
            name (str): Display name of the engine. Example: Stockfish 15.
            max_threads (int): Maximum number of available threads. Example: 8.
            max_hash (int): Maximum available hash table size, in MiB. Example: 2048.
            provider_secret (str): A random token that can be used to
                [wait for analysis requests](#tag/External-engine/operation/apiExternalEngineAcquire)
                and provide analysis.

                The engine provider should securely generate a random string.

                The token will not be readable again, even by the user.

                The analysis provider can register multiple engines with the same
                token, even for different users, and wait for analysis requests
                from any of them. In this case, the request must not be made via
                CORS, so that the token is not revealed to any of the users.
                 Example: Dee3uwieZei9ahpaici9bee2yahsai0K.
            variants (Union[Unset, list[ApiExternalEngineCreateBodyVariantsItem]]): Optional list of supported chess
                variants.
            provider_data (Union[Unset, str]): Arbitrary data that the engine provider can use for identification
                or bookkeeping.

                Users can read this information, but updating it requires knowing
                or changing the `providerSecret`.
     """

    name: str
    max_threads: int
    max_hash: int
    provider_secret: str
    variants: Union[Unset, list[ApiExternalEngineCreateBodyVariantsItem]] = UNSET
    provider_data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        max_threads = self.max_threads

        max_hash = self.max_hash

        provider_secret = self.provider_secret

        variants: Union[Unset, list[str]] = UNSET
        if not isinstance(self.variants, Unset):
            variants = []
            for variants_item_data in self.variants:
                variants_item = variants_item_data.value
                variants.append(variants_item)



        provider_data = self.provider_data


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "maxThreads": max_threads,
            "maxHash": max_hash,
            "providerSecret": provider_secret,
        })
        if variants is not UNSET:
            field_dict["variants"] = variants
        if provider_data is not UNSET:
            field_dict["providerData"] = provider_data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        max_threads = d.pop("maxThreads")

        max_hash = d.pop("maxHash")

        provider_secret = d.pop("providerSecret")

        variants = []
        _variants = d.pop("variants", UNSET)
        for variants_item_data in (_variants or []):
            variants_item = ApiExternalEngineCreateBodyVariantsItem(variants_item_data)



            variants.append(variants_item)


        provider_data = d.pop("providerData", UNSET)

        api_external_engine_create_body = cls(
            name=name,
            max_threads=max_threads,
            max_hash=max_hash,
            provider_secret=provider_secret,
            variants=variants,
            provider_data=provider_data,
        )


        api_external_engine_create_body.additional_properties = d
        return api_external_engine_create_body

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
