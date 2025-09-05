from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_open_response_200_color import ChallengeOpenResponse200Color
from ..models.challenge_open_response_200_final_color import ChallengeOpenResponse200FinalColor
from ..models.challenge_open_response_200_speed import ChallengeOpenResponse200Speed
from ..models.challenge_open_response_200_status import ChallengeOpenResponse200Status
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_open_response_200_variant import ChallengeOpenResponse200Variant
  from ..models.challenge_open_response_200_correspondence import ChallengeOpenResponse200Correspondence
  from ..models.challenge_open_response_200_perf import ChallengeOpenResponse200Perf
  from ..models.challenge_open_response_200_open import ChallengeOpenResponse200Open
  from ..models.challenge_open_response_200_unlimited import ChallengeOpenResponse200Unlimited
  from ..models.challenge_open_response_200_real_time import ChallengeOpenResponse200RealTime





T = TypeVar("T", bound="ChallengeOpenResponse200")



@_attrs_define
class ChallengeOpenResponse200:
    """ 
        Attributes:
            id (str):
            url (str):
            status (ChallengeOpenResponse200Status):
            challenger (None):
            dest_user (None):
            variant (ChallengeOpenResponse200Variant):
            rated (bool):
            speed (ChallengeOpenResponse200Speed):
            time_control (Union['ChallengeOpenResponse200Correspondence', 'ChallengeOpenResponse200RealTime',
                'ChallengeOpenResponse200Unlimited']):
            color (ChallengeOpenResponse200Color):
            perf (ChallengeOpenResponse200Perf):
            url_white (str):
            url_black (str):
            open_ (ChallengeOpenResponse200Open):
            final_color (Union[Unset, ChallengeOpenResponse200FinalColor]):
            initial_fen (Union[Unset, str]):
     """

    id: str
    url: str
    status: ChallengeOpenResponse200Status
    challenger: None
    dest_user: None
    variant: 'ChallengeOpenResponse200Variant'
    rated: bool
    speed: ChallengeOpenResponse200Speed
    time_control: Union['ChallengeOpenResponse200Correspondence', 'ChallengeOpenResponse200RealTime', 'ChallengeOpenResponse200Unlimited']
    color: ChallengeOpenResponse200Color
    perf: 'ChallengeOpenResponse200Perf'
    url_white: str
    url_black: str
    open_: 'ChallengeOpenResponse200Open'
    final_color: Union[Unset, ChallengeOpenResponse200FinalColor] = UNSET
    initial_fen: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_open_response_200_variant import ChallengeOpenResponse200Variant
        from ..models.challenge_open_response_200_correspondence import ChallengeOpenResponse200Correspondence
        from ..models.challenge_open_response_200_perf import ChallengeOpenResponse200Perf
        from ..models.challenge_open_response_200_open import ChallengeOpenResponse200Open
        from ..models.challenge_open_response_200_unlimited import ChallengeOpenResponse200Unlimited
        from ..models.challenge_open_response_200_real_time import ChallengeOpenResponse200RealTime
        id = self.id

        url = self.url

        status = self.status.value

        challenger = self.challenger

        dest_user = self.dest_user

        variant = self.variant.to_dict()

        rated = self.rated

        speed = self.speed.value

        time_control: dict[str, Any]
        if isinstance(self.time_control, ChallengeOpenResponse200RealTime):
            time_control = self.time_control.to_dict()
        elif isinstance(self.time_control, ChallengeOpenResponse200Correspondence):
            time_control = self.time_control.to_dict()
        else:
            time_control = self.time_control.to_dict()


        color = self.color.value

        perf = self.perf.to_dict()

        url_white = self.url_white

        url_black = self.url_black

        open_ = self.open_.to_dict()

        final_color: Union[Unset, str] = UNSET
        if not isinstance(self.final_color, Unset):
            final_color = self.final_color.value


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
            "urlWhite": url_white,
            "urlBlack": url_black,
            "open": open_,
        })
        if final_color is not UNSET:
            field_dict["finalColor"] = final_color
        if initial_fen is not UNSET:
            field_dict["initialFen"] = initial_fen

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge_open_response_200_variant import ChallengeOpenResponse200Variant
        from ..models.challenge_open_response_200_correspondence import ChallengeOpenResponse200Correspondence
        from ..models.challenge_open_response_200_perf import ChallengeOpenResponse200Perf
        from ..models.challenge_open_response_200_open import ChallengeOpenResponse200Open
        from ..models.challenge_open_response_200_unlimited import ChallengeOpenResponse200Unlimited
        from ..models.challenge_open_response_200_real_time import ChallengeOpenResponse200RealTime
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        status = ChallengeOpenResponse200Status(d.pop("status"))




        challenger = d.pop("challenger")

        dest_user = d.pop("destUser")

        variant = ChallengeOpenResponse200Variant.from_dict(d.pop("variant"))




        rated = d.pop("rated")

        speed = ChallengeOpenResponse200Speed(d.pop("speed"))




        def _parse_time_control(data: object) -> Union['ChallengeOpenResponse200Correspondence', 'ChallengeOpenResponse200RealTime', 'ChallengeOpenResponse200Unlimited']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_real_time = ChallengeOpenResponse200RealTime.from_dict(data)



                return time_control_real_time
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_correspondence = ChallengeOpenResponse200Correspondence.from_dict(data)



                return time_control_correspondence
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            time_control_unlimited = ChallengeOpenResponse200Unlimited.from_dict(data)



            return time_control_unlimited

        time_control = _parse_time_control(d.pop("timeControl"))


        color = ChallengeOpenResponse200Color(d.pop("color"))




        perf = ChallengeOpenResponse200Perf.from_dict(d.pop("perf"))




        url_white = d.pop("urlWhite")

        url_black = d.pop("urlBlack")

        open_ = ChallengeOpenResponse200Open.from_dict(d.pop("open"))




        _final_color = d.pop("finalColor", UNSET)
        final_color: Union[Unset, ChallengeOpenResponse200FinalColor]
        if isinstance(_final_color,  Unset):
            final_color = UNSET
        else:
            final_color = ChallengeOpenResponse200FinalColor(_final_color)




        initial_fen = d.pop("initialFen", UNSET)

        challenge_open_response_200 = cls(
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
            url_white=url_white,
            url_black=url_black,
            open_=open_,
            final_color=final_color,
            initial_fen=initial_fen,
        )


        challenge_open_response_200.additional_properties = d
        return challenge_open_response_200

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
