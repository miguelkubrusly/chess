from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_create_response_200_color import ChallengeCreateResponse200Color
from ..models.challenge_create_response_200_direction import ChallengeCreateResponse200Direction
from ..models.challenge_create_response_200_final_color import ChallengeCreateResponse200FinalColor
from ..models.challenge_create_response_200_speed import ChallengeCreateResponse200Speed
from ..models.challenge_create_response_200_status import ChallengeCreateResponse200Status
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_create_response_200_correspondence import ChallengeCreateResponse200Correspondence
  from ..models.challenge_create_response_200_dest_user_type_0 import ChallengeCreateResponse200DestUserType0
  from ..models.challenge_create_response_200_unlimited import ChallengeCreateResponse200Unlimited
  from ..models.challenge_create_response_200_real_time import ChallengeCreateResponse200RealTime
  from ..models.challenge_create_response_200_challenger import ChallengeCreateResponse200Challenger
  from ..models.challenge_create_response_200_variant import ChallengeCreateResponse200Variant
  from ..models.challenge_create_response_200_perf import ChallengeCreateResponse200Perf





T = TypeVar("T", bound="ChallengeCreateResponse200")



@_attrs_define
class ChallengeCreateResponse200:
    r""" 
        Example:
            {'id': 'H9fIRZUk', 'url': 'https://lichess.org/H9fIRZUk', 'status': 'created', 'challenger': {'id': 'bot1',
                'name': 'Bot1', 'rating': 1500, 'title': 'BOT', 'provisional': True, 'online': True, 'lag': 4}, 'destUser':
                {'id': 'bobby', 'name': 'Bobby', 'rating': 1635, 'title': 'GM', 'provisional': True, 'online': True, 'lag': 4},
                'variant': {'key': 'standard', 'name': 'Standard', 'short': 'Std'}, 'rated': True, 'speed': 'rapid',
                'timeControl': {'type': 'clock', 'limit': 600, 'increment': 0, 'show': '10+0'}, 'color': 'random', 'finalColor':
                'black', 'perf': {'icon': '\ue017', 'name': 'Rapid'}, 'direction': 'out'}

        Attributes:
            id (str):
            url (str):
            status (ChallengeCreateResponse200Status):
            challenger (ChallengeCreateResponse200Challenger):
            dest_user (Union['ChallengeCreateResponse200DestUserType0', None]):
            variant (ChallengeCreateResponse200Variant):
            rated (bool):
            speed (ChallengeCreateResponse200Speed):
            time_control (Union['ChallengeCreateResponse200Correspondence', 'ChallengeCreateResponse200RealTime',
                'ChallengeCreateResponse200Unlimited']):
            color (ChallengeCreateResponse200Color):
            perf (ChallengeCreateResponse200Perf):
            final_color (Union[Unset, ChallengeCreateResponse200FinalColor]):
            direction (Union[Unset, ChallengeCreateResponse200Direction]):
            initial_fen (Union[Unset, str]):
     """

    id: str
    url: str
    status: ChallengeCreateResponse200Status
    challenger: 'ChallengeCreateResponse200Challenger'
    dest_user: Union['ChallengeCreateResponse200DestUserType0', None]
    variant: 'ChallengeCreateResponse200Variant'
    rated: bool
    speed: ChallengeCreateResponse200Speed
    time_control: Union['ChallengeCreateResponse200Correspondence', 'ChallengeCreateResponse200RealTime', 'ChallengeCreateResponse200Unlimited']
    color: ChallengeCreateResponse200Color
    perf: 'ChallengeCreateResponse200Perf'
    final_color: Union[Unset, ChallengeCreateResponse200FinalColor] = UNSET
    direction: Union[Unset, ChallengeCreateResponse200Direction] = UNSET
    initial_fen: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_create_response_200_correspondence import ChallengeCreateResponse200Correspondence
        from ..models.challenge_create_response_200_dest_user_type_0 import ChallengeCreateResponse200DestUserType0
        from ..models.challenge_create_response_200_unlimited import ChallengeCreateResponse200Unlimited
        from ..models.challenge_create_response_200_real_time import ChallengeCreateResponse200RealTime
        from ..models.challenge_create_response_200_challenger import ChallengeCreateResponse200Challenger
        from ..models.challenge_create_response_200_variant import ChallengeCreateResponse200Variant
        from ..models.challenge_create_response_200_perf import ChallengeCreateResponse200Perf
        id = self.id

        url = self.url

        status = self.status.value

        challenger = self.challenger.to_dict()

        dest_user: Union[None, dict[str, Any]]
        if isinstance(self.dest_user, ChallengeCreateResponse200DestUserType0):
            dest_user = self.dest_user.to_dict()
        else:
            dest_user = self.dest_user

        variant = self.variant.to_dict()

        rated = self.rated

        speed = self.speed.value

        time_control: dict[str, Any]
        if isinstance(self.time_control, ChallengeCreateResponse200RealTime):
            time_control = self.time_control.to_dict()
        elif isinstance(self.time_control, ChallengeCreateResponse200Correspondence):
            time_control = self.time_control.to_dict()
        else:
            time_control = self.time_control.to_dict()


        color = self.color.value

        perf = self.perf.to_dict()

        final_color: Union[Unset, str] = UNSET
        if not isinstance(self.final_color, Unset):
            final_color = self.final_color.value


        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value


        initial_fen = self.initial_fen


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "url": url,
            "status": status,
            "challenger": challenger,
            "destUser": dest_user,
            "variant": variant,
            "rated": rated,
            "speed": speed,
            "timeControl": time_control,
            "color": color,
            "perf": perf,
        })
        if final_color is not UNSET:
            field_dict["finalColor"] = final_color
        if direction is not UNSET:
            field_dict["direction"] = direction
        if initial_fen is not UNSET:
            field_dict["initialFen"] = initial_fen

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge_create_response_200_correspondence import ChallengeCreateResponse200Correspondence
        from ..models.challenge_create_response_200_dest_user_type_0 import ChallengeCreateResponse200DestUserType0
        from ..models.challenge_create_response_200_unlimited import ChallengeCreateResponse200Unlimited
        from ..models.challenge_create_response_200_real_time import ChallengeCreateResponse200RealTime
        from ..models.challenge_create_response_200_challenger import ChallengeCreateResponse200Challenger
        from ..models.challenge_create_response_200_variant import ChallengeCreateResponse200Variant
        from ..models.challenge_create_response_200_perf import ChallengeCreateResponse200Perf
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        status = ChallengeCreateResponse200Status(d.pop("status"))




        challenger = ChallengeCreateResponse200Challenger.from_dict(d.pop("challenger"))




        def _parse_dest_user(data: object) -> Union['ChallengeCreateResponse200DestUserType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dest_user_type_0 = ChallengeCreateResponse200DestUserType0.from_dict(data)



                return dest_user_type_0
            except: # noqa: E722
                pass
            return cast(Union['ChallengeCreateResponse200DestUserType0', None], data)

        dest_user = _parse_dest_user(d.pop("destUser"))


        variant = ChallengeCreateResponse200Variant.from_dict(d.pop("variant"))




        rated = d.pop("rated")

        speed = ChallengeCreateResponse200Speed(d.pop("speed"))




        def _parse_time_control(data: object) -> Union['ChallengeCreateResponse200Correspondence', 'ChallengeCreateResponse200RealTime', 'ChallengeCreateResponse200Unlimited']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_real_time = ChallengeCreateResponse200RealTime.from_dict(data)



                return time_control_real_time
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_correspondence = ChallengeCreateResponse200Correspondence.from_dict(data)



                return time_control_correspondence
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            time_control_unlimited = ChallengeCreateResponse200Unlimited.from_dict(data)



            return time_control_unlimited

        time_control = _parse_time_control(d.pop("timeControl"))


        color = ChallengeCreateResponse200Color(d.pop("color"))




        perf = ChallengeCreateResponse200Perf.from_dict(d.pop("perf"))




        _final_color = d.pop("finalColor", UNSET)
        final_color: Union[Unset, ChallengeCreateResponse200FinalColor]
        if isinstance(_final_color,  Unset):
            final_color = UNSET
        else:
            final_color = ChallengeCreateResponse200FinalColor(_final_color)




        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, ChallengeCreateResponse200Direction]
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ChallengeCreateResponse200Direction(_direction)




        initial_fen = d.pop("initialFen", UNSET)

        challenge_create_response_200 = cls(
            id=id,
            url=url,
            status=status,
            challenger=challenger,
            dest_user=dest_user,
            variant=variant,
            rated=rated,
            speed=speed,
            time_control=time_control,
            color=color,
            perf=perf,
            final_color=final_color,
            direction=direction,
            initial_fen=initial_fen,
        )


        challenge_create_response_200.additional_properties = d
        return challenge_create_response_200

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
