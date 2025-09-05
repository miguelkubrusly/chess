from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.team_requests_response_200_item_user_title import TeamRequestsResponse200ItemUserTitle
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.team_requests_response_200_item_user_profile import TeamRequestsResponse200ItemUserProfile
  from ..models.team_requests_response_200_item_user_play_time import TeamRequestsResponse200ItemUserPlayTime
  from ..models.team_requests_response_200_item_user_perfs import TeamRequestsResponse200ItemUserPerfs





T = TypeVar("T", bound="TeamRequestsResponse200ItemUser")



@_attrs_define
class TeamRequestsResponse200ItemUser:
    """ 
        Attributes:
            id (str):  Example: georges.
            username (str):  Example: Georges.
            perfs (Union[Unset, TeamRequestsResponse200ItemUserPerfs]):
            title (Union[Unset, TeamRequestsResponse200ItemUserTitle]): only appears if the user is a titled player or a bot
                user
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            created_at (Union[Unset, int]):  Example: 1290415680000.
            disabled (Union[Unset, bool]): only appears if a user's account is closed
            tos_violation (Union[Unset, bool]): only appears if a user's account is marked for the violation of [Lichess
                TOS](https://lichess.org/terms-of-service)
            profile (Union[Unset, TeamRequestsResponse200ItemUserProfile]):
            seen_at (Union[Unset, int]):  Example: 1522636452014.
            play_time (Union[Unset, TeamRequestsResponse200ItemUserPlayTime]):
            patron (Union[Unset, bool]):  Example: True.
            verified (Union[Unset, bool]):  Example: True.
     """

    id: str
    username: str
    perfs: Union[Unset, 'TeamRequestsResponse200ItemUserPerfs'] = UNSET
    title: Union[Unset, TeamRequestsResponse200ItemUserTitle] = UNSET
    flair: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    disabled: Union[Unset, bool] = UNSET
    tos_violation: Union[Unset, bool] = UNSET
    profile: Union[Unset, 'TeamRequestsResponse200ItemUserProfile'] = UNSET
    seen_at: Union[Unset, int] = UNSET
    play_time: Union[Unset, 'TeamRequestsResponse200ItemUserPlayTime'] = UNSET
    patron: Union[Unset, bool] = UNSET
    verified: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_requests_response_200_item_user_profile import TeamRequestsResponse200ItemUserProfile
        from ..models.team_requests_response_200_item_user_play_time import TeamRequestsResponse200ItemUserPlayTime
        from ..models.team_requests_response_200_item_user_perfs import TeamRequestsResponse200ItemUserPerfs
        id = self.id

        username = self.username

        perfs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.perfs, Unset):
            perfs = self.perfs.to_dict()

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value


        flair = self.flair

        created_at = self.created_at

        disabled = self.disabled

        tos_violation = self.tos_violation

        profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        seen_at = self.seen_at

        play_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.play_time, Unset):
            play_time = self.play_time.to_dict()

        patron = self.patron

        verified = self.verified


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "username": username,
        })
        if perfs is not UNSET:
            field_dict["perfs"] = perfs
        if title is not UNSET:
            field_dict["title"] = title
        if flair is not UNSET:
            field_dict["flair"] = flair
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if tos_violation is not UNSET:
            field_dict["tosViolation"] = tos_violation
        if profile is not UNSET:
            field_dict["profile"] = profile
        if seen_at is not UNSET:
            field_dict["seenAt"] = seen_at
        if play_time is not UNSET:
            field_dict["playTime"] = play_time
        if patron is not UNSET:
            field_dict["patron"] = patron
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_requests_response_200_item_user_profile import TeamRequestsResponse200ItemUserProfile
        from ..models.team_requests_response_200_item_user_play_time import TeamRequestsResponse200ItemUserPlayTime
        from ..models.team_requests_response_200_item_user_perfs import TeamRequestsResponse200ItemUserPerfs
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        _perfs = d.pop("perfs", UNSET)
        perfs: Union[Unset, TeamRequestsResponse200ItemUserPerfs]
        if isinstance(_perfs,  Unset):
            perfs = UNSET
        else:
            perfs = TeamRequestsResponse200ItemUserPerfs.from_dict(_perfs)




        _title = d.pop("title", UNSET)
        title: Union[Unset, TeamRequestsResponse200ItemUserTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = TeamRequestsResponse200ItemUserTitle(_title)




        flair = d.pop("flair", UNSET)

        created_at = d.pop("createdAt", UNSET)

        disabled = d.pop("disabled", UNSET)

        tos_violation = d.pop("tosViolation", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, TeamRequestsResponse200ItemUserProfile]
        if isinstance(_profile,  Unset):
            profile = UNSET
        else:
            profile = TeamRequestsResponse200ItemUserProfile.from_dict(_profile)




        seen_at = d.pop("seenAt", UNSET)

        _play_time = d.pop("playTime", UNSET)
        play_time: Union[Unset, TeamRequestsResponse200ItemUserPlayTime]
        if isinstance(_play_time,  Unset):
            play_time = UNSET
        else:
            play_time = TeamRequestsResponse200ItemUserPlayTime.from_dict(_play_time)




        patron = d.pop("patron", UNSET)

        verified = d.pop("verified", UNSET)

        team_requests_response_200_item_user = cls(
            id=id,
            username=username,
            perfs=perfs,
            title=title,
            flair=flair,
            created_at=created_at,
            disabled=disabled,
            tos_violation=tos_violation,
            profile=profile,
            seen_at=seen_at,
            play_time=play_time,
            patron=patron,
            verified=verified,
        )


        team_requests_response_200_item_user.additional_properties = d
        return team_requests_response_200_item_user

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
