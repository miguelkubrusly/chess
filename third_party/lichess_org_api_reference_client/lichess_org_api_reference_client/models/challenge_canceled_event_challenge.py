from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_canceled_event_challenge_color import ChallengeCanceledEventChallengeColor
from ..models.challenge_canceled_event_challenge_direction import ChallengeCanceledEventChallengeDirection
from ..models.challenge_canceled_event_challenge_final_color import ChallengeCanceledEventChallengeFinalColor
from ..models.challenge_canceled_event_challenge_speed import ChallengeCanceledEventChallengeSpeed
from ..models.challenge_canceled_event_challenge_status import ChallengeCanceledEventChallengeStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_canceled_event_challenge_unlimited import ChallengeCanceledEventChallengeUnlimited
  from ..models.challenge_canceled_event_challenge_dest_user_type_0 import ChallengeCanceledEventChallengeDestUserType0
  from ..models.challenge_canceled_event_challenge_real_time import ChallengeCanceledEventChallengeRealTime
  from ..models.challenge_canceled_event_challenge_correspondence import ChallengeCanceledEventChallengeCorrespondence
  from ..models.challenge_canceled_event_challenge_perf import ChallengeCanceledEventChallengePerf
  from ..models.challenge_canceled_event_challenge_challenger import ChallengeCanceledEventChallengeChallenger
  from ..models.challenge_canceled_event_challenge_variant import ChallengeCanceledEventChallengeVariant





T = TypeVar("T", bound="ChallengeCanceledEventChallenge")



@_attrs_define
class ChallengeCanceledEventChallenge:
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
            status (ChallengeCanceledEventChallengeStatus):
            challenger (ChallengeCanceledEventChallengeChallenger):
            dest_user (Union['ChallengeCanceledEventChallengeDestUserType0', None]):
            variant (ChallengeCanceledEventChallengeVariant):
            rated (bool):
            speed (ChallengeCanceledEventChallengeSpeed):
            time_control (Union['ChallengeCanceledEventChallengeCorrespondence', 'ChallengeCanceledEventChallengeRealTime',
                'ChallengeCanceledEventChallengeUnlimited']):
            color (ChallengeCanceledEventChallengeColor):
            perf (ChallengeCanceledEventChallengePerf):
            final_color (Union[Unset, ChallengeCanceledEventChallengeFinalColor]):
            direction (Union[Unset, ChallengeCanceledEventChallengeDirection]):
            initial_fen (Union[Unset, str]):
     """

    id: str
    url: str
    status: ChallengeCanceledEventChallengeStatus
    challenger: 'ChallengeCanceledEventChallengeChallenger'
    dest_user: Union['ChallengeCanceledEventChallengeDestUserType0', None]
    variant: 'ChallengeCanceledEventChallengeVariant'
    rated: bool
    speed: ChallengeCanceledEventChallengeSpeed
    time_control: Union['ChallengeCanceledEventChallengeCorrespondence', 'ChallengeCanceledEventChallengeRealTime', 'ChallengeCanceledEventChallengeUnlimited']
    color: ChallengeCanceledEventChallengeColor
    perf: 'ChallengeCanceledEventChallengePerf'
    final_color: Union[Unset, ChallengeCanceledEventChallengeFinalColor] = UNSET
    direction: Union[Unset, ChallengeCanceledEventChallengeDirection] = UNSET
    initial_fen: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_canceled_event_challenge_unlimited import ChallengeCanceledEventChallengeUnlimited
        from ..models.challenge_canceled_event_challenge_dest_user_type_0 import ChallengeCanceledEventChallengeDestUserType0
        from ..models.challenge_canceled_event_challenge_real_time import ChallengeCanceledEventChallengeRealTime
        from ..models.challenge_canceled_event_challenge_correspondence import ChallengeCanceledEventChallengeCorrespondence
        from ..models.challenge_canceled_event_challenge_perf import ChallengeCanceledEventChallengePerf
        from ..models.challenge_canceled_event_challenge_challenger import ChallengeCanceledEventChallengeChallenger
        from ..models.challenge_canceled_event_challenge_variant import ChallengeCanceledEventChallengeVariant
        id = self.id

        url = self.url

        status = self.status.value

        challenger = self.challenger.to_dict()

        dest_user: Union[None, dict[str, Any]]
        if isinstance(self.dest_user, ChallengeCanceledEventChallengeDestUserType0):
            dest_user = self.dest_user.to_dict()
        else:
            dest_user = self.dest_user

        variant = self.variant.to_dict()

        rated = self.rated

        speed = self.speed.value

        time_control: dict[str, Any]
        if isinstance(self.time_control, ChallengeCanceledEventChallengeRealTime):
            time_control = self.time_control.to_dict()
        elif isinstance(self.time_control, ChallengeCanceledEventChallengeCorrespondence):
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
        from ..models.challenge_canceled_event_challenge_unlimited import ChallengeCanceledEventChallengeUnlimited
        from ..models.challenge_canceled_event_challenge_dest_user_type_0 import ChallengeCanceledEventChallengeDestUserType0
        from ..models.challenge_canceled_event_challenge_real_time import ChallengeCanceledEventChallengeRealTime
        from ..models.challenge_canceled_event_challenge_correspondence import ChallengeCanceledEventChallengeCorrespondence
        from ..models.challenge_canceled_event_challenge_perf import ChallengeCanceledEventChallengePerf
        from ..models.challenge_canceled_event_challenge_challenger import ChallengeCanceledEventChallengeChallenger
        from ..models.challenge_canceled_event_challenge_variant import ChallengeCanceledEventChallengeVariant
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        status = ChallengeCanceledEventChallengeStatus(d.pop("status"))




        challenger = ChallengeCanceledEventChallengeChallenger.from_dict(d.pop("challenger"))




        def _parse_dest_user(data: object) -> Union['ChallengeCanceledEventChallengeDestUserType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dest_user_type_0 = ChallengeCanceledEventChallengeDestUserType0.from_dict(data)



                return dest_user_type_0
            except: # noqa: E722
                pass
            return cast(Union['ChallengeCanceledEventChallengeDestUserType0', None], data)

        dest_user = _parse_dest_user(d.pop("destUser"))


        variant = ChallengeCanceledEventChallengeVariant.from_dict(d.pop("variant"))




        rated = d.pop("rated")

        speed = ChallengeCanceledEventChallengeSpeed(d.pop("speed"))




        def _parse_time_control(data: object) -> Union['ChallengeCanceledEventChallengeCorrespondence', 'ChallengeCanceledEventChallengeRealTime', 'ChallengeCanceledEventChallengeUnlimited']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_real_time = ChallengeCanceledEventChallengeRealTime.from_dict(data)



                return time_control_real_time
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_correspondence = ChallengeCanceledEventChallengeCorrespondence.from_dict(data)



                return time_control_correspondence
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            time_control_unlimited = ChallengeCanceledEventChallengeUnlimited.from_dict(data)



            return time_control_unlimited

        time_control = _parse_time_control(d.pop("timeControl"))


        color = ChallengeCanceledEventChallengeColor(d.pop("color"))




        perf = ChallengeCanceledEventChallengePerf.from_dict(d.pop("perf"))




        _final_color = d.pop("finalColor", UNSET)
        final_color: Union[Unset, ChallengeCanceledEventChallengeFinalColor]
        if isinstance(_final_color,  Unset):
            final_color = UNSET
        else:
            final_color = ChallengeCanceledEventChallengeFinalColor(_final_color)




        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, ChallengeCanceledEventChallengeDirection]
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ChallengeCanceledEventChallengeDirection(_direction)




        initial_fen = d.pop("initialFen", UNSET)

        challenge_canceled_event_challenge = cls(
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


        challenge_canceled_event_challenge.additional_properties = d
        return challenge_canceled_event_challenge

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
