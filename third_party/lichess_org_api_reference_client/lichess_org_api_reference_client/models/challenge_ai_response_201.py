from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_ai_response_201_perf import ChallengeAiResponse201Perf
from ..models.challenge_ai_response_201_player import ChallengeAiResponse201Player
from ..models.challenge_ai_response_201_source import ChallengeAiResponse201Source
from ..models.challenge_ai_response_201_speed import ChallengeAiResponse201Speed
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_ai_response_201_status import ChallengeAiResponse201Status
  from ..models.challenge_ai_response_201_variant import ChallengeAiResponse201Variant





T = TypeVar("T", bound="ChallengeAiResponse201")



@_attrs_define
class ChallengeAiResponse201:
    """ 
        Attributes:
            id (Union[Unset, str]):
            variant (Union[Unset, ChallengeAiResponse201Variant]):
            speed (Union[Unset, ChallengeAiResponse201Speed]):
            perf (Union[Unset, ChallengeAiResponse201Perf]):
            rated (Union[Unset, bool]):
            fen (Union[Unset, str]):
            turns (Union[Unset, int]):
            source (Union[Unset, ChallengeAiResponse201Source]):
            status (Union[Unset, ChallengeAiResponse201Status]):
            created_at (Union[Unset, float]):
            player (Union[Unset, ChallengeAiResponse201Player]):
            full_id (Union[Unset, str]):
     """

    id: Union[Unset, str] = UNSET
    variant: Union[Unset, 'ChallengeAiResponse201Variant'] = UNSET
    speed: Union[Unset, ChallengeAiResponse201Speed] = UNSET
    perf: Union[Unset, ChallengeAiResponse201Perf] = UNSET
    rated: Union[Unset, bool] = UNSET
    fen: Union[Unset, str] = UNSET
    turns: Union[Unset, int] = UNSET
    source: Union[Unset, ChallengeAiResponse201Source] = UNSET
    status: Union[Unset, 'ChallengeAiResponse201Status'] = UNSET
    created_at: Union[Unset, float] = UNSET
    player: Union[Unset, ChallengeAiResponse201Player] = UNSET
    full_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_ai_response_201_status import ChallengeAiResponse201Status
        from ..models.challenge_ai_response_201_variant import ChallengeAiResponse201Variant
        id = self.id

        variant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.to_dict()

        speed: Union[Unset, str] = UNSET
        if not isinstance(self.speed, Unset):
            speed = self.speed.value


        perf: Union[Unset, str] = UNSET
        if not isinstance(self.perf, Unset):
            perf = self.perf.value


        rated = self.rated

        fen = self.fen

        turns = self.turns

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        created_at = self.created_at

        player: Union[Unset, str] = UNSET
        if not isinstance(self.player, Unset):
            player = self.player.value


        full_id = self.full_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if variant is not UNSET:
            field_dict["variant"] = variant
        if speed is not UNSET:
            field_dict["speed"] = speed
        if perf is not UNSET:
            field_dict["perf"] = perf
        if rated is not UNSET:
            field_dict["rated"] = rated
        if fen is not UNSET:
            field_dict["fen"] = fen
        if turns is not UNSET:
            field_dict["turns"] = turns
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if player is not UNSET:
            field_dict["player"] = player
        if full_id is not UNSET:
            field_dict["fullId"] = full_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge_ai_response_201_status import ChallengeAiResponse201Status
        from ..models.challenge_ai_response_201_variant import ChallengeAiResponse201Variant
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, ChallengeAiResponse201Variant]
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = ChallengeAiResponse201Variant.from_dict(_variant)




        _speed = d.pop("speed", UNSET)
        speed: Union[Unset, ChallengeAiResponse201Speed]
        if isinstance(_speed,  Unset):
            speed = UNSET
        else:
            speed = ChallengeAiResponse201Speed(_speed)




        _perf = d.pop("perf", UNSET)
        perf: Union[Unset, ChallengeAiResponse201Perf]
        if isinstance(_perf,  Unset):
            perf = UNSET
        else:
            perf = ChallengeAiResponse201Perf(_perf)




        rated = d.pop("rated", UNSET)

        fen = d.pop("fen", UNSET)

        turns = d.pop("turns", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ChallengeAiResponse201Source]
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = ChallengeAiResponse201Source(_source)




        _status = d.pop("status", UNSET)
        status: Union[Unset, ChallengeAiResponse201Status]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ChallengeAiResponse201Status.from_dict(_status)




        created_at = d.pop("createdAt", UNSET)

        _player = d.pop("player", UNSET)
        player: Union[Unset, ChallengeAiResponse201Player]
        if isinstance(_player,  Unset):
            player = UNSET
        else:
            player = ChallengeAiResponse201Player(_player)




        full_id = d.pop("fullId", UNSET)

        challenge_ai_response_201 = cls(
            id=id,
            variant=variant,
            speed=speed,
            perf=perf,
            rated=rated,
            fen=fen,
            turns=turns,
            source=source,
            status=status,
            created_at=created_at,
            player=player,
            full_id=full_id,
        )


        challenge_ai_response_201.additional_properties = d
        return challenge_ai_response_201

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
