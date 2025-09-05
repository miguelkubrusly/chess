from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_external_engine_acquire_response_200_work_type_1_variant import ApiExternalEngineAcquireResponse200WorkType1Variant
from typing import cast






T = TypeVar("T", bound="ApiExternalEngineAcquireResponse200WorkType1")



@_attrs_define
class ApiExternalEngineAcquireResponse200WorkType1:
    """ 
        Attributes:
            depth (int): Analysis target depth
            session_id (str): Arbitary string that identifies the analysis session.
                Providers may wish to clear the hash table between sessions.
            threads (int): Number of threads to use for analysis.
            hash_ (int): Hash table size to use for analysis, in MiB.
            multi_pv (int): Requested number of principal variations.
            variant (ApiExternalEngineAcquireResponse200WorkType1Variant):  Default:
                ApiExternalEngineAcquireResponse200WorkType1Variant.CHESS. Example: chess.
            initial_fen (str): Initial position of the game.
            moves (list[str]): List of moves played from the initial position, in UCI notation.
     """

    depth: int
    session_id: str
    threads: int
    hash_: int
    multi_pv: int
    initial_fen: str
    moves: list[str]
    variant: ApiExternalEngineAcquireResponse200WorkType1Variant = ApiExternalEngineAcquireResponse200WorkType1Variant.CHESS
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        depth = self.depth

        session_id = self.session_id

        threads = self.threads

        hash_ = self.hash_

        multi_pv = self.multi_pv

        variant = self.variant.value

        initial_fen = self.initial_fen

        moves = self.moves




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "depth": depth,
            "sessionId": session_id,
            "threads": threads,
            "hash": hash_,
            "multiPv": multi_pv,
            "variant": variant,
            "initialFen": initial_fen,
            "moves": moves,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        depth = d.pop("depth")

        session_id = d.pop("sessionId")

        threads = d.pop("threads")

        hash_ = d.pop("hash")

        multi_pv = d.pop("multiPv")

        variant = ApiExternalEngineAcquireResponse200WorkType1Variant(d.pop("variant"))




        initial_fen = d.pop("initialFen")

        moves = cast(list[str], d.pop("moves"))


        api_external_engine_acquire_response_200_work_type_1 = cls(
            depth=depth,
            session_id=session_id,
            threads=threads,
            hash_=hash_,
            multi_pv=multi_pv,
            variant=variant,
            initial_fen=initial_fen,
            moves=moves,
        )


        api_external_engine_acquire_response_200_work_type_1.additional_properties = d
        return api_external_engine_acquire_response_200_work_type_1

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
