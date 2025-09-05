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
  from ..models.challenge_canceled_event_challenge import ChallengeCanceledEventChallenge





T = TypeVar("T", bound="ChallengeCanceledEvent")



@_attrs_define
class ChallengeCanceledEvent:
    r""" 
        Attributes:
            type_ (Union[Literal['challengeCanceled'], Unset]):
            challenge (Union[Unset, ChallengeCanceledEventChallenge]):  Example: {'id': 'H9fIRZUk', 'url':
                'https://lichess.org/H9fIRZUk', 'status': 'created', 'challenger': {'id': 'bot1', 'name': 'Bot1', 'rating':
                1500, 'title': 'BOT', 'provisional': True, 'online': True, 'lag': 4}, 'destUser': {'id': 'bobby', 'name':
                'Bobby', 'rating': 1635, 'title': 'GM', 'provisional': True, 'online': True, 'lag': 4}, 'variant': {'key':
                'standard', 'name': 'Standard', 'short': 'Std'}, 'rated': True, 'speed': 'rapid', 'timeControl': {'type':
                'clock', 'limit': 600, 'increment': 0, 'show': '10+0'}, 'color': 'random', 'finalColor': 'black', 'perf':
                {'icon': '\ue017', 'name': 'Rapid'}, 'direction': 'out'}.
     """

    type_: Union[Literal['challengeCanceled'], Unset] = UNSET
    challenge: Union[Unset, 'ChallengeCanceledEventChallenge'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_canceled_event_challenge import ChallengeCanceledEventChallenge
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
        from ..models.challenge_canceled_event_challenge import ChallengeCanceledEventChallenge
        d = dict(src_dict)
        type_ = cast(Union[Literal['challengeCanceled'], Unset] , d.pop("type", UNSET))
        if type_ != 'challengeCanceled'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'challengeCanceled', got '{type_}'")

        _challenge = d.pop("challenge", UNSET)
        challenge: Union[Unset, ChallengeCanceledEventChallenge]
        if isinstance(_challenge,  Unset):
            challenge = UNSET
        else:
            challenge = ChallengeCanceledEventChallenge.from_dict(_challenge)




        challenge_canceled_event = cls(
            type_=type_,
            challenge=challenge,
        )


        challenge_canceled_event.additional_properties = d
        return challenge_canceled_event

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
