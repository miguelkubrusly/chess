from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_event_challenge_color import ChallengeEventChallengeColor
from ..models.challenge_event_challenge_direction import ChallengeEventChallengeDirection
from ..models.challenge_event_challenge_final_color import ChallengeEventChallengeFinalColor
from ..models.challenge_event_challenge_speed import ChallengeEventChallengeSpeed
from ..models.challenge_event_challenge_status import ChallengeEventChallengeStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_event_challenge_variant import ChallengeEventChallengeVariant
  from ..models.challenge_event_challenge_real_time import ChallengeEventChallengeRealTime
  from ..models.challenge_event_challenge_unlimited import ChallengeEventChallengeUnlimited
  from ..models.challenge_event_challenge_perf import ChallengeEventChallengePerf
  from ..models.challenge_event_challenge_dest_user_type_0 import ChallengeEventChallengeDestUserType0
  from ..models.challenge_event_challenge_correspondence import ChallengeEventChallengeCorrespondence
  from ..models.challenge_event_challenge_challenger import ChallengeEventChallengeChallenger





T = TypeVar("T", bound="ChallengeEventChallenge")



@_attrs_define
class ChallengeEventChallenge:
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
            status (ChallengeEventChallengeStatus):
            challenger (ChallengeEventChallengeChallenger):
            dest_user (Union['ChallengeEventChallengeDestUserType0', None]):
            variant (ChallengeEventChallengeVariant):
            rated (bool):
            speed (ChallengeEventChallengeSpeed):
            time_control (Union['ChallengeEventChallengeCorrespondence', 'ChallengeEventChallengeRealTime',
                'ChallengeEventChallengeUnlimited']):
            color (ChallengeEventChallengeColor):
            perf (ChallengeEventChallengePerf):
            final_color (Union[Unset, ChallengeEventChallengeFinalColor]):
            direction (Union[Unset, ChallengeEventChallengeDirection]):
            initial_fen (Union[Unset, str]):
     """

    id: str
    url: str
    status: ChallengeEventChallengeStatus
    challenger: 'ChallengeEventChallengeChallenger'
    dest_user: Union['ChallengeEventChallengeDestUserType0', None]
    variant: 'ChallengeEventChallengeVariant'
    rated: bool
    speed: ChallengeEventChallengeSpeed
    time_control: Union['ChallengeEventChallengeCorrespondence', 'ChallengeEventChallengeRealTime', 'ChallengeEventChallengeUnlimited']
    color: ChallengeEventChallengeColor
    perf: 'ChallengeEventChallengePerf'
    final_color: Union[Unset, ChallengeEventChallengeFinalColor] = UNSET
    direction: Union[Unset, ChallengeEventChallengeDirection] = UNSET
    initial_fen: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_event_challenge_variant import ChallengeEventChallengeVariant
        from ..models.challenge_event_challenge_real_time import ChallengeEventChallengeRealTime
        from ..models.challenge_event_challenge_unlimited import ChallengeEventChallengeUnlimited
        from ..models.challenge_event_challenge_perf import ChallengeEventChallengePerf
        from ..models.challenge_event_challenge_dest_user_type_0 import ChallengeEventChallengeDestUserType0
        from ..models.challenge_event_challenge_correspondence import ChallengeEventChallengeCorrespondence
        from ..models.challenge_event_challenge_challenger import ChallengeEventChallengeChallenger
        id = self.id

        url = self.url

        status = self.status.value

        challenger = self.challenger.to_dict()

        dest_user: Union[None, dict[str, Any]]
        if isinstance(self.dest_user, ChallengeEventChallengeDestUserType0):
            dest_user = self.dest_user.to_dict()
        else:
            dest_user = self.dest_user

        variant = self.variant.to_dict()

        rated = self.rated

        speed = self.speed.value

        time_control: dict[str, Any]
        if isinstance(self.time_control, ChallengeEventChallengeRealTime):
            time_control = self.time_control.to_dict()
        elif isinstance(self.time_control, ChallengeEventChallengeCorrespondence):
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
        from ..models.challenge_event_challenge_variant import ChallengeEventChallengeVariant
        from ..models.challenge_event_challenge_real_time import ChallengeEventChallengeRealTime
        from ..models.challenge_event_challenge_unlimited import ChallengeEventChallengeUnlimited
        from ..models.challenge_event_challenge_perf import ChallengeEventChallengePerf
        from ..models.challenge_event_challenge_dest_user_type_0 import ChallengeEventChallengeDestUserType0
        from ..models.challenge_event_challenge_correspondence import ChallengeEventChallengeCorrespondence
        from ..models.challenge_event_challenge_challenger import ChallengeEventChallengeChallenger
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        status = ChallengeEventChallengeStatus(d.pop("status"))




        challenger = ChallengeEventChallengeChallenger.from_dict(d.pop("challenger"))




        def _parse_dest_user(data: object) -> Union['ChallengeEventChallengeDestUserType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dest_user_type_0 = ChallengeEventChallengeDestUserType0.from_dict(data)



                return dest_user_type_0
            except: # noqa: E722
                pass
            return cast(Union['ChallengeEventChallengeDestUserType0', None], data)

        dest_user = _parse_dest_user(d.pop("destUser"))


        variant = ChallengeEventChallengeVariant.from_dict(d.pop("variant"))




        rated = d.pop("rated")

        speed = ChallengeEventChallengeSpeed(d.pop("speed"))




        def _parse_time_control(data: object) -> Union['ChallengeEventChallengeCorrespondence', 'ChallengeEventChallengeRealTime', 'ChallengeEventChallengeUnlimited']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_real_time = ChallengeEventChallengeRealTime.from_dict(data)



                return time_control_real_time
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_correspondence = ChallengeEventChallengeCorrespondence.from_dict(data)



                return time_control_correspondence
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            time_control_unlimited = ChallengeEventChallengeUnlimited.from_dict(data)



            return time_control_unlimited

        time_control = _parse_time_control(d.pop("timeControl"))


        color = ChallengeEventChallengeColor(d.pop("color"))




        perf = ChallengeEventChallengePerf.from_dict(d.pop("perf"))




        _final_color = d.pop("finalColor", UNSET)
        final_color: Union[Unset, ChallengeEventChallengeFinalColor]
        if isinstance(_final_color,  Unset):
            final_color = UNSET
        else:
            final_color = ChallengeEventChallengeFinalColor(_final_color)




        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, ChallengeEventChallengeDirection]
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ChallengeEventChallengeDirection(_direction)




        initial_fen = d.pop("initialFen", UNSET)

        challenge_event_challenge = cls(
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


        challenge_event_challenge.additional_properties = d
        return challenge_event_challenge

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
