from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_list_response_200_out_item_color import ChallengeListResponse200OutItemColor
from ..models.challenge_list_response_200_out_item_direction import ChallengeListResponse200OutItemDirection
from ..models.challenge_list_response_200_out_item_final_color import ChallengeListResponse200OutItemFinalColor
from ..models.challenge_list_response_200_out_item_speed import ChallengeListResponse200OutItemSpeed
from ..models.challenge_list_response_200_out_item_status import ChallengeListResponse200OutItemStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.challenge_list_response_200_out_item_perf import ChallengeListResponse200OutItemPerf
  from ..models.challenge_list_response_200_out_item_real_time import ChallengeListResponse200OutItemRealTime
  from ..models.challenge_list_response_200_out_item_correspondence import ChallengeListResponse200OutItemCorrespondence
  from ..models.challenge_list_response_200_out_item_variant import ChallengeListResponse200OutItemVariant
  from ..models.challenge_list_response_200_out_item_challenger import ChallengeListResponse200OutItemChallenger
  from ..models.challenge_list_response_200_out_item_dest_user_type_0 import ChallengeListResponse200OutItemDestUserType0
  from ..models.challenge_list_response_200_out_item_unlimited import ChallengeListResponse200OutItemUnlimited





T = TypeVar("T", bound="ChallengeListResponse200OutItem")



@_attrs_define
class ChallengeListResponse200OutItem:
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
            status (ChallengeListResponse200OutItemStatus):
            challenger (ChallengeListResponse200OutItemChallenger):
            dest_user (Union['ChallengeListResponse200OutItemDestUserType0', None]):
            variant (ChallengeListResponse200OutItemVariant):
            rated (bool):
            speed (ChallengeListResponse200OutItemSpeed):
            time_control (Union['ChallengeListResponse200OutItemCorrespondence', 'ChallengeListResponse200OutItemRealTime',
                'ChallengeListResponse200OutItemUnlimited']):
            color (ChallengeListResponse200OutItemColor):
            perf (ChallengeListResponse200OutItemPerf):
            final_color (Union[Unset, ChallengeListResponse200OutItemFinalColor]):
            direction (Union[Unset, ChallengeListResponse200OutItemDirection]):
            initial_fen (Union[Unset, str]):
     """

    id: str
    url: str
    status: ChallengeListResponse200OutItemStatus
    challenger: 'ChallengeListResponse200OutItemChallenger'
    dest_user: Union['ChallengeListResponse200OutItemDestUserType0', None]
    variant: 'ChallengeListResponse200OutItemVariant'
    rated: bool
    speed: ChallengeListResponse200OutItemSpeed
    time_control: Union['ChallengeListResponse200OutItemCorrespondence', 'ChallengeListResponse200OutItemRealTime', 'ChallengeListResponse200OutItemUnlimited']
    color: ChallengeListResponse200OutItemColor
    perf: 'ChallengeListResponse200OutItemPerf'
    final_color: Union[Unset, ChallengeListResponse200OutItemFinalColor] = UNSET
    direction: Union[Unset, ChallengeListResponse200OutItemDirection] = UNSET
    initial_fen: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_list_response_200_out_item_perf import ChallengeListResponse200OutItemPerf
        from ..models.challenge_list_response_200_out_item_real_time import ChallengeListResponse200OutItemRealTime
        from ..models.challenge_list_response_200_out_item_correspondence import ChallengeListResponse200OutItemCorrespondence
        from ..models.challenge_list_response_200_out_item_variant import ChallengeListResponse200OutItemVariant
        from ..models.challenge_list_response_200_out_item_challenger import ChallengeListResponse200OutItemChallenger
        from ..models.challenge_list_response_200_out_item_dest_user_type_0 import ChallengeListResponse200OutItemDestUserType0
        from ..models.challenge_list_response_200_out_item_unlimited import ChallengeListResponse200OutItemUnlimited
        id = self.id

        url = self.url

        status = self.status.value

        challenger = self.challenger.to_dict()

        dest_user: Union[None, dict[str, Any]]
        if isinstance(self.dest_user, ChallengeListResponse200OutItemDestUserType0):
            dest_user = self.dest_user.to_dict()
        else:
            dest_user = self.dest_user

        variant = self.variant.to_dict()

        rated = self.rated

        speed = self.speed.value

        time_control: dict[str, Any]
        if isinstance(self.time_control, ChallengeListResponse200OutItemRealTime):
            time_control = self.time_control.to_dict()
        elif isinstance(self.time_control, ChallengeListResponse200OutItemCorrespondence):
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
        from ..models.challenge_list_response_200_out_item_perf import ChallengeListResponse200OutItemPerf
        from ..models.challenge_list_response_200_out_item_real_time import ChallengeListResponse200OutItemRealTime
        from ..models.challenge_list_response_200_out_item_correspondence import ChallengeListResponse200OutItemCorrespondence
        from ..models.challenge_list_response_200_out_item_variant import ChallengeListResponse200OutItemVariant
        from ..models.challenge_list_response_200_out_item_challenger import ChallengeListResponse200OutItemChallenger
        from ..models.challenge_list_response_200_out_item_dest_user_type_0 import ChallengeListResponse200OutItemDestUserType0
        from ..models.challenge_list_response_200_out_item_unlimited import ChallengeListResponse200OutItemUnlimited
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        status = ChallengeListResponse200OutItemStatus(d.pop("status"))




        challenger = ChallengeListResponse200OutItemChallenger.from_dict(d.pop("challenger"))




        def _parse_dest_user(data: object) -> Union['ChallengeListResponse200OutItemDestUserType0', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dest_user_type_0 = ChallengeListResponse200OutItemDestUserType0.from_dict(data)



                return dest_user_type_0
            except: # noqa: E722
                pass
            return cast(Union['ChallengeListResponse200OutItemDestUserType0', None], data)

        dest_user = _parse_dest_user(d.pop("destUser"))


        variant = ChallengeListResponse200OutItemVariant.from_dict(d.pop("variant"))




        rated = d.pop("rated")

        speed = ChallengeListResponse200OutItemSpeed(d.pop("speed"))




        def _parse_time_control(data: object) -> Union['ChallengeListResponse200OutItemCorrespondence', 'ChallengeListResponse200OutItemRealTime', 'ChallengeListResponse200OutItemUnlimited']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_real_time = ChallengeListResponse200OutItemRealTime.from_dict(data)



                return time_control_real_time
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_control_correspondence = ChallengeListResponse200OutItemCorrespondence.from_dict(data)



                return time_control_correspondence
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            time_control_unlimited = ChallengeListResponse200OutItemUnlimited.from_dict(data)



            return time_control_unlimited

        time_control = _parse_time_control(d.pop("timeControl"))


        color = ChallengeListResponse200OutItemColor(d.pop("color"))




        perf = ChallengeListResponse200OutItemPerf.from_dict(d.pop("perf"))




        _final_color = d.pop("finalColor", UNSET)
        final_color: Union[Unset, ChallengeListResponse200OutItemFinalColor]
        if isinstance(_final_color,  Unset):
            final_color = UNSET
        else:
            final_color = ChallengeListResponse200OutItemFinalColor(_final_color)




        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, ChallengeListResponse200OutItemDirection]
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ChallengeListResponse200OutItemDirection(_direction)




        initial_fen = d.pop("initialFen", UNSET)

        challenge_list_response_200_out_item = cls(
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


        challenge_list_response_200_out_item.additional_properties = d
        return challenge_list_response_200_out_item

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
