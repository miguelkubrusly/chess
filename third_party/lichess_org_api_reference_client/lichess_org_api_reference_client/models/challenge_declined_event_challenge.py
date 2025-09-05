from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_declined_event_challenge_color import ChallengeDeclinedEventChallengeColor
from ..models.challenge_declined_event_challenge_decline_reason_key import ChallengeDeclinedEventChallengeDeclineReasonKey
from ..models.challenge_declined_event_challenge_direction import ChallengeDeclinedEventChallengeDirection
from ..models.challenge_declined_event_challenge_final_color import ChallengeDeclinedEventChallengeFinalColor
from ..models.challenge_declined_event_challenge_speed import ChallengeDeclinedEventChallengeSpeed
from ..models.challenge_declined_event_challenge_status import ChallengeDeclinedEventChallengeStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_declined_event_challenge_variant import ChallengeDeclinedEventChallengeVariant
  from ..models.challenge_declined_event_challenge_correspondence import ChallengeDeclinedEventChallengeCorrespondence
  from ..models.challenge_declined_event_challenge_perf import ChallengeDeclinedEventChallengePerf
  from ..models.challenge_declined_event_challenge_dest_user_type_0 import ChallengeDeclinedEventChallengeDestUserType0
  from ..models.challenge_declined_event_challenge_real_time import ChallengeDeclinedEventChallengeRealTime
  from ..models.challenge_declined_event_challenge_unlimited import ChallengeDeclinedEventChallengeUnlimited
  from ..models.challenge_declined_event_challenge_challenger import ChallengeDeclinedEventChallengeChallenger





T = TypeVar("T", bound="ChallengeDeclinedEventChallenge")



@_attrs_define
class ChallengeDeclinedEventChallenge:
    """ 
        Attributes:
            decline_reason (str): Human readable, possibly translated reason why the challenge was declined.
            decline_reason_key (ChallengeDeclinedEventChallengeDeclineReasonKey): Untranslated, computer-matchable reason
                why the challenge was declined.
            id (str):
            url (str):
            status (ChallengeDeclinedEventChallengeStatus):
            challenger (ChallengeDeclinedEventChallengeChallenger):
            dest_user (Union['ChallengeDeclinedEventChallengeDestUserType0', None]):
            variant (ChallengeDeclinedEventChallengeVariant):
            rated (bool):
            speed (ChallengeDeclinedEventChallengeSpeed):
            time_control (Union['ChallengeDeclinedEventChallengeCorrespondence', 'ChallengeDeclinedEventChallengeRealTime',
                'ChallengeDeclinedEventChallengeUnlimited']):
            color (ChallengeDeclinedEventChallengeColor):
            perf (ChallengeDeclinedEventChallengePerf):
            final_color (Union[Unset, ChallengeDeclinedEventChallengeFinalColor]):
            direction (Union[Unset, ChallengeDeclinedEventChallengeDirection]):
            initial_fen (Union[Unset, str]):
     """

    decline_reason: str
    decline_reason_key: ChallengeDeclinedEventChallengeDeclineReasonKey
    id: str
    url: str
    status: ChallengeDeclinedEventChallengeStatus
    challenger: 'ChallengeDeclinedEventChallengeChallenger'
    dest_user: Union['ChallengeDeclinedEventChallengeDestUserType0', None]
    variant: 'ChallengeDeclinedEventChallengeVariant'
    rated: bool
    speed: ChallengeDeclinedEventChallengeSpeed
    time_control: Union['ChallengeDeclinedEventChallengeCorrespondence', 'ChallengeDeclinedEventChallengeRealTime', 'ChallengeDeclinedEventChallengeUnlimited']
    color: ChallengeDeclinedEventChallengeColor
    perf: 'ChallengeDeclinedEventChallengePerf'
    final_color: Union[Unset, ChallengeDeclinedEventChallengeFinalColor] = UNSET
    direction: Union[Unset, ChallengeDeclinedEventChallengeDirection] = UNSET
    initial_fen: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_declined_event_challenge_variant import ChallengeDeclinedEventChallengeVariant
        from ..models.challenge_declined_event_challenge_correspondence import ChallengeDeclinedEventChallengeCorrespondence
        from ..models.challenge_declined_event_challenge_perf import ChallengeDeclinedEventChallengePerf
        from ..models.challenge_declined_event_challenge_dest_user_type_0 import ChallengeDeclinedEventChallengeDestUserType0
        from ..models.challenge_declined_event_challenge_real_time import ChallengeDeclinedEventChallengeRealTime
        from ..models.challenge_declined_event_challenge_unlimited import ChallengeDeclinedEventChallengeUnlimited
        from ..models.challenge_declined_event_challenge_challenger import ChallengeDeclinedEventChallengeChallenger
        decline_reason = self.decline_reason

        decline_reason_key = self.decline_reason_key.value

        id = self.id

        url = self.url

        status = self.status.value

        challenger = self.challenger.to_dict()

        dest_user: Union[None, dict[str, Any]]
        if isinstance(self.dest_user, ChallengeDeclinedEventChallengeDestUserType0):
            dest_user = self.dest_user.to_dict()
        else:
            dest_user = self.dest_user

        variant = self.variant.to_dict()

        rated = self.rated

        speed = self.speed.value

        time_control: dict[str, Any]
        if isinstance(self.time_control, ChallengeDeclinedEventChallengeRealTime):
            time_control = self.time_control.to_dict()
        elif isinstance(self.time_control, ChallengeDeclinedEventChallengeCorrespondence):
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
            "declineReason": decline_reason,
            "declineReasonKey": decline_reason_key,
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
        from ..models.challenge_declined_event_challenge_variant import ChallengeDeclinedEventChallengeVariant
        from ..models.challenge_declined_event_challenge_correspondence import ChallengeDeclinedEventChallengeCorrespondence
        from ..models.challenge_declined_event_challenge_perf import ChallengeDeclinedEventChallengePerf
        from ..models.challenge_declined_event_challenge_dest_user_type_0 import ChallengeDeclinedEventChallengeDestUserType0
        from ..models.challenge_declined_event_challenge_real_time import ChallengeDeclinedEventChallengeRealTime
        from ..models.challenge_declined_event_challenge_unlimited import ChallengeDeclinedEventChallengeUnlimited
        from ..models.challenge_declined_event_challenge_challenger import ChallengeDeclinedEventChallengeChallenger
        d = dict(src_dict)
        decline_reason = d.pop("declineReason")

        decline_reason_key = ChallengeDeclinedEventChallengeDeclineReasonKey(d.pop("declineReasonKey"))




        id = d.pop("id")

        url = d.pop("url")

        status = ChallengeDeclinedEventChallengeStatus(d.pop("status"))




        challenger = ChallengeDeclinedEventChallengeChallenger.from_dict(d.pop("challenger"))




        def _parse_dest_user(data: object) -> Union['ChallengeDeclinedEventChallengeDestUserType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dest_user_type_0 = ChallengeDeclinedEventChallengeDestUserType0.from_dict(data)



                return dest_user_type_0
            except: # noqa: E722
                pass
            return cast(Union['ChallengeDeclinedEventChallengeDestUserType0', None], data)

        dest_user = _parse_dest_user(d.pop("destUser"))


        variant = ChallengeDeclinedEventChallengeVariant.from_dict(d.pop("variant"))




        rated = d.pop("rated")

        speed = ChallengeDeclinedEventChallengeSpeed(d.pop("speed"))




        def _parse_time_control(data: object) -> Union['ChallengeDeclinedEventChallengeCorrespondence', 'ChallengeDeclinedEventChallengeRealTime', 'ChallengeDeclinedEventChallengeUnlimited']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_real_time = ChallengeDeclinedEventChallengeRealTime.from_dict(data)



                return time_control_real_time
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_correspondence = ChallengeDeclinedEventChallengeCorrespondence.from_dict(data)



                return time_control_correspondence
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            time_control_unlimited = ChallengeDeclinedEventChallengeUnlimited.from_dict(data)



            return time_control_unlimited

        time_control = _parse_time_control(d.pop("timeControl"))


        color = ChallengeDeclinedEventChallengeColor(d.pop("color"))




        perf = ChallengeDeclinedEventChallengePerf.from_dict(d.pop("perf"))




        _final_color = d.pop("finalColor", UNSET)
        final_color: Union[Unset, ChallengeDeclinedEventChallengeFinalColor]
        if isinstance(_final_color,  Unset):
            final_color = UNSET
        else:
            final_color = ChallengeDeclinedEventChallengeFinalColor(_final_color)




        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, ChallengeDeclinedEventChallengeDirection]
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ChallengeDeclinedEventChallengeDirection(_direction)




        initial_fen = d.pop("initialFen", UNSET)

        challenge_declined_event_challenge = cls(
            decline_reason=decline_reason,
            decline_reason_key=decline_reason_key,
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


        challenge_declined_event_challenge.additional_properties = d
        return challenge_declined_event_challenge

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
