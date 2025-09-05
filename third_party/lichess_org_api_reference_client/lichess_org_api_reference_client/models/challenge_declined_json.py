from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_declined_json_color import ChallengeDeclinedJsonColor
from ..models.challenge_declined_json_decline_reason_key import ChallengeDeclinedJsonDeclineReasonKey
from ..models.challenge_declined_json_direction import ChallengeDeclinedJsonDirection
from ..models.challenge_declined_json_final_color import ChallengeDeclinedJsonFinalColor
from ..models.challenge_declined_json_speed import ChallengeDeclinedJsonSpeed
from ..models.challenge_declined_json_status import ChallengeDeclinedJsonStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_declined_json_real_time import ChallengeDeclinedJsonRealTime
  from ..models.challenge_declined_json_variant import ChallengeDeclinedJsonVariant
  from ..models.challenge_declined_json_unlimited import ChallengeDeclinedJsonUnlimited
  from ..models.challenge_declined_json_correspondence import ChallengeDeclinedJsonCorrespondence
  from ..models.challenge_declined_json_dest_user_type_0 import ChallengeDeclinedJsonDestUserType0
  from ..models.challenge_declined_json_perf import ChallengeDeclinedJsonPerf
  from ..models.challenge_declined_json_challenger import ChallengeDeclinedJsonChallenger





T = TypeVar("T", bound="ChallengeDeclinedJson")



@_attrs_define
class ChallengeDeclinedJson:
    """ 
        Attributes:
            decline_reason (str): Human readable, possibly translated reason why the challenge was declined.
            decline_reason_key (ChallengeDeclinedJsonDeclineReasonKey): Untranslated, computer-matchable reason why the
                challenge was declined.
            id (str):
            url (str):
            status (ChallengeDeclinedJsonStatus):
            challenger (ChallengeDeclinedJsonChallenger):
            dest_user (Union['ChallengeDeclinedJsonDestUserType0', None]):
            variant (ChallengeDeclinedJsonVariant):
            rated (bool):
            speed (ChallengeDeclinedJsonSpeed):
            time_control (Union['ChallengeDeclinedJsonCorrespondence', 'ChallengeDeclinedJsonRealTime',
                'ChallengeDeclinedJsonUnlimited']):
            color (ChallengeDeclinedJsonColor):
            perf (ChallengeDeclinedJsonPerf):
            final_color (Union[Unset, ChallengeDeclinedJsonFinalColor]):
            direction (Union[Unset, ChallengeDeclinedJsonDirection]):
            initial_fen (Union[Unset, str]):
     """

    decline_reason: str
    decline_reason_key: ChallengeDeclinedJsonDeclineReasonKey
    id: str
    url: str
    status: ChallengeDeclinedJsonStatus
    challenger: 'ChallengeDeclinedJsonChallenger'
    dest_user: Union['ChallengeDeclinedJsonDestUserType0', None]
    variant: 'ChallengeDeclinedJsonVariant'
    rated: bool
    speed: ChallengeDeclinedJsonSpeed
    time_control: Union['ChallengeDeclinedJsonCorrespondence', 'ChallengeDeclinedJsonRealTime', 'ChallengeDeclinedJsonUnlimited']
    color: ChallengeDeclinedJsonColor
    perf: 'ChallengeDeclinedJsonPerf'
    final_color: Union[Unset, ChallengeDeclinedJsonFinalColor] = UNSET
    direction: Union[Unset, ChallengeDeclinedJsonDirection] = UNSET
    initial_fen: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_declined_json_real_time import ChallengeDeclinedJsonRealTime
        from ..models.challenge_declined_json_variant import ChallengeDeclinedJsonVariant
        from ..models.challenge_declined_json_unlimited import ChallengeDeclinedJsonUnlimited
        from ..models.challenge_declined_json_correspondence import ChallengeDeclinedJsonCorrespondence
        from ..models.challenge_declined_json_dest_user_type_0 import ChallengeDeclinedJsonDestUserType0
        from ..models.challenge_declined_json_perf import ChallengeDeclinedJsonPerf
        from ..models.challenge_declined_json_challenger import ChallengeDeclinedJsonChallenger
        decline_reason = self.decline_reason

        decline_reason_key = self.decline_reason_key.value

        id = self.id

        url = self.url

        status = self.status.value

        challenger = self.challenger.to_dict()

        dest_user: Union[None, dict[str, Any]]
        if isinstance(self.dest_user, ChallengeDeclinedJsonDestUserType0):
            dest_user = self.dest_user.to_dict()
        else:
            dest_user = self.dest_user

        variant = self.variant.to_dict()

        rated = self.rated

        speed = self.speed.value

        time_control: dict[str, Any]
        if isinstance(self.time_control, ChallengeDeclinedJsonRealTime):
            time_control = self.time_control.to_dict()
        elif isinstance(self.time_control, ChallengeDeclinedJsonCorrespondence):
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
        from ..models.challenge_declined_json_real_time import ChallengeDeclinedJsonRealTime
        from ..models.challenge_declined_json_variant import ChallengeDeclinedJsonVariant
        from ..models.challenge_declined_json_unlimited import ChallengeDeclinedJsonUnlimited
        from ..models.challenge_declined_json_correspondence import ChallengeDeclinedJsonCorrespondence
        from ..models.challenge_declined_json_dest_user_type_0 import ChallengeDeclinedJsonDestUserType0
        from ..models.challenge_declined_json_perf import ChallengeDeclinedJsonPerf
        from ..models.challenge_declined_json_challenger import ChallengeDeclinedJsonChallenger
        d = dict(src_dict)
        decline_reason = d.pop("declineReason")

        decline_reason_key = ChallengeDeclinedJsonDeclineReasonKey(d.pop("declineReasonKey"))




        id = d.pop("id")

        url = d.pop("url")

        status = ChallengeDeclinedJsonStatus(d.pop("status"))




        challenger = ChallengeDeclinedJsonChallenger.from_dict(d.pop("challenger"))




        def _parse_dest_user(data: object) -> Union['ChallengeDeclinedJsonDestUserType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dest_user_type_0 = ChallengeDeclinedJsonDestUserType0.from_dict(data)



                return dest_user_type_0
            except: # noqa: E722
                pass
            return cast(Union['ChallengeDeclinedJsonDestUserType0', None], data)

        dest_user = _parse_dest_user(d.pop("destUser"))


        variant = ChallengeDeclinedJsonVariant.from_dict(d.pop("variant"))




        rated = d.pop("rated")

        speed = ChallengeDeclinedJsonSpeed(d.pop("speed"))




        def _parse_time_control(data: object) -> Union['ChallengeDeclinedJsonCorrespondence', 'ChallengeDeclinedJsonRealTime', 'ChallengeDeclinedJsonUnlimited']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_real_time = ChallengeDeclinedJsonRealTime.from_dict(data)



                return time_control_real_time
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_correspondence = ChallengeDeclinedJsonCorrespondence.from_dict(data)



                return time_control_correspondence
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            time_control_unlimited = ChallengeDeclinedJsonUnlimited.from_dict(data)



            return time_control_unlimited

        time_control = _parse_time_control(d.pop("timeControl"))


        color = ChallengeDeclinedJsonColor(d.pop("color"))




        perf = ChallengeDeclinedJsonPerf.from_dict(d.pop("perf"))




        _final_color = d.pop("finalColor", UNSET)
        final_color: Union[Unset, ChallengeDeclinedJsonFinalColor]
        if isinstance(_final_color,  Unset):
            final_color = UNSET
        else:
            final_color = ChallengeDeclinedJsonFinalColor(_final_color)




        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, ChallengeDeclinedJsonDirection]
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ChallengeDeclinedJsonDirection(_direction)




        initial_fen = d.pop("initialFen", UNSET)

        challenge_declined_json = cls(
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


        challenge_declined_json.additional_properties = d
        return challenge_declined_json

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
