from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_event_challenge import ChallengeEventChallenge
  from ..models.challenge_event_compat import ChallengeEventCompat





T = TypeVar("T", bound="ChallengeEvent")



@_attrs_define
class ChallengeEvent:
    r""" 
        Attributes:
            type_ (Literal['challenge']):
            challenge (ChallengeEventChallenge):  Example: {'id': 'H9fIRZUk', 'url': 'https://lichess.org/H9fIRZUk',
                'status': 'created', 'challenger': {'id': 'bot1', 'name': 'Bot1', 'rating': 1500, 'title': 'BOT', 'provisional':
                True, 'online': True, 'lag': 4}, 'destUser': {'id': 'bobby', 'name': 'Bobby', 'rating': 1635, 'title': 'GM',
                'provisional': True, 'online': True, 'lag': 4}, 'variant': {'key': 'standard', 'name': 'Standard', 'short':
                'Std'}, 'rated': True, 'speed': 'rapid', 'timeControl': {'type': 'clock', 'limit': 600, 'increment': 0, 'show':
                '10+0'}, 'color': 'random', 'finalColor': 'black', 'perf': {'icon': '\ue017', 'name': 'Rapid'}, 'direction':
                'out'}.
            compat (Union[Unset, ChallengeEventCompat]):
     """

    type_: Literal['challenge']
    challenge: 'ChallengeEventChallenge'
    compat: Union[Unset, 'ChallengeEventCompat'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_event_challenge import ChallengeEventChallenge
        from ..models.challenge_event_compat import ChallengeEventCompat
        type_ = self.type_

        challenge = self.challenge.to_dict()

        compat: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.compat, Unset):
            compat = self.compat.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "challenge": challenge,
        })
        if compat is not UNSET:
            field_dict["compat"] = compat

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge_event_challenge import ChallengeEventChallenge
        from ..models.challenge_event_compat import ChallengeEventCompat
        d = dict(src_dict)
        type_ = cast(Literal['challenge'] , d.pop("type"))
        if type_ != 'challenge':
            raise ValueError(f"type must match const 'challenge', got '{type_}'")

        challenge = ChallengeEventChallenge.from_dict(d.pop("challenge"))




        _compat = d.pop("compat", UNSET)
        compat: Union[Unset, ChallengeEventCompat]
        if isinstance(_compat,  Unset):
            compat = UNSET
        else:
            compat = ChallengeEventCompat.from_dict(_compat)




        challenge_event = cls(
            type_=type_,
            challenge=challenge,
            compat=compat,
        )


        challenge_event.additional_properties = d
        return challenge_event

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
