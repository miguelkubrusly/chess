from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, Union, cast
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_declined_event_challenge import ChallengeDeclinedEventChallenge





T = TypeVar("T", bound="ChallengeDeclinedEvent")



@_attrs_define
class ChallengeDeclinedEvent:
    """ 
        Attributes:
            type_ (Union[Literal['challengeDeclined'], Unset]):
            challenge (Union[Unset, ChallengeDeclinedEventChallenge]):
     """

    type_: Union[Literal['challengeDeclined'], Unset] = UNSET
    challenge: Union[Unset, 'ChallengeDeclinedEventChallenge'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_declined_event_challenge import ChallengeDeclinedEventChallenge
        type_ = self.type_

        challenge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.challenge, Unset):
            challenge = self.challenge.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if challenge is not UNSET:
            field_dict["challenge"] = challenge

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge_declined_event_challenge import ChallengeDeclinedEventChallenge
        d = dict(src_dict)
        type_ = cast(Union[Literal['challengeDeclined'], Unset] , d.pop("type", UNSET))
        if type_ != 'challengeDeclined'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'challengeDeclined', got '{type_}'")

        _challenge = d.pop("challenge", UNSET)
        challenge: Union[Unset, ChallengeDeclinedEventChallenge]
        if isinstance(_challenge,  Unset):
            challenge = UNSET
        else:
            challenge = ChallengeDeclinedEventChallenge.from_dict(_challenge)




        challenge_declined_event = cls(
            type_=type_,
            challenge=challenge,
        )


        challenge_declined_event.additional_properties = d
        return challenge_declined_event

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
