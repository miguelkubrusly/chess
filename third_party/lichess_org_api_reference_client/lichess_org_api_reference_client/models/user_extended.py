from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_extended_title import UserExtendedTitle
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.user_extended_count import UserExtendedCount
  from ..models.user_extended_play_time import UserExtendedPlayTime
  from ..models.user_extended_profile import UserExtendedProfile
  from ..models.user_extended_perfs import UserExtendedPerfs
  from ..models.user_extended_streamer import UserExtendedStreamer





T = TypeVar("T", bound="UserExtended")



@_attrs_define
class UserExtended:
    """ 
        Attributes:
            id (str):  Example: georges.
            username (str):  Example: Georges.
            url (str):  Example: https://lichess.org/@/georges.
            perfs (Union[Unset, UserExtendedPerfs]):
            title (Union[Unset, UserExtendedTitle]): only appears if the user is a titled player or a bot user
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            created_at (Union[Unset, int]):  Example: 1290415680000.
            disabled (Union[Unset, bool]): only appears if a user's account is closed
            tos_violation (Union[Unset, bool]): only appears if a user's account is marked for the violation of [Lichess
                TOS](https://lichess.org/terms-of-service)
            profile (Union[Unset, UserExtendedProfile]):
            seen_at (Union[Unset, int]):  Example: 1522636452014.
            play_time (Union[Unset, UserExtendedPlayTime]):
            patron (Union[Unset, bool]):  Example: True.
            verified (Union[Unset, bool]):  Example: True.
            playing (Union[Unset, str]):  Example: https://lichess.org/yqfLYJ5E/black.
            count (Union[Unset, UserExtendedCount]):
            streaming (Union[Unset, bool]):
            streamer (Union[Unset, UserExtendedStreamer]):
            followable (Union[Unset, bool]): only appears if the request is [authenticated with
                OAuth2](#section/Introduction/Authentication) Example: True.
            following (Union[Unset, bool]): only appears if the request is [authenticated with
                OAuth2](#section/Introduction/Authentication)
            blocking (Union[Unset, bool]): only appears if the request is [authenticated with
                OAuth2](#section/Introduction/Authentication)
     """

    id: str
    username: str
    url: str
    perfs: Union[Unset, 'UserExtendedPerfs'] = UNSET
    title: Union[Unset, UserExtendedTitle] = UNSET
    flair: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    disabled: Union[Unset, bool] = UNSET
    tos_violation: Union[Unset, bool] = UNSET
    profile: Union[Unset, 'UserExtendedProfile'] = UNSET
    seen_at: Union[Unset, int] = UNSET
    play_time: Union[Unset, 'UserExtendedPlayTime'] = UNSET
    patron: Union[Unset, bool] = UNSET
    verified: Union[Unset, bool] = UNSET
    playing: Union[Unset, str] = UNSET
    count: Union[Unset, 'UserExtendedCount'] = UNSET
    streaming: Union[Unset, bool] = UNSET
    streamer: Union[Unset, 'UserExtendedStreamer'] = UNSET
    followable: Union[Unset, bool] = UNSET
    following: Union[Unset, bool] = UNSET
    blocking: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_extended_count import UserExtendedCount
        from ..models.user_extended_play_time import UserExtendedPlayTime
        from ..models.user_extended_profile import UserExtendedProfile
        from ..models.user_extended_perfs import UserExtendedPerfs
        from ..models.user_extended_streamer import UserExtendedStreamer
        id = self.id

        username = self.username

        url = self.url

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

        playing = self.playing

        count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.count, Unset):
            count = self.count.to_dict()

        streaming = self.streaming

        streamer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.streamer, Unset):
            streamer = self.streamer.to_dict()

        followable = self.followable

        following = self.following

        blocking = self.blocking


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "username": username,
            "url": url,
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
        if playing is not UNSET:
            field_dict["playing"] = playing
        if count is not UNSET:
            field_dict["count"] = count
        if streaming is not UNSET:
            field_dict["streaming"] = streaming
        if streamer is not UNSET:
            field_dict["streamer"] = streamer
        if followable is not UNSET:
            field_dict["followable"] = followable
        if following is not UNSET:
            field_dict["following"] = following
        if blocking is not UNSET:
            field_dict["blocking"] = blocking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_extended_count import UserExtendedCount
        from ..models.user_extended_play_time import UserExtendedPlayTime
        from ..models.user_extended_profile import UserExtendedProfile
        from ..models.user_extended_perfs import UserExtendedPerfs
        from ..models.user_extended_streamer import UserExtendedStreamer
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        url = d.pop("url")

        _perfs = d.pop("perfs", UNSET)
        perfs: Union[Unset, UserExtendedPerfs]
        if isinstance(_perfs,  Unset):
            perfs = UNSET
        else:
            perfs = UserExtendedPerfs.from_dict(_perfs)




        _title = d.pop("title", UNSET)
        title: Union[Unset, UserExtendedTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = UserExtendedTitle(_title)




        flair = d.pop("flair", UNSET)

        created_at = d.pop("createdAt", UNSET)

        disabled = d.pop("disabled", UNSET)

        tos_violation = d.pop("tosViolation", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, UserExtendedProfile]
        if isinstance(_profile,  Unset):
            profile = UNSET
        else:
            profile = UserExtendedProfile.from_dict(_profile)




        seen_at = d.pop("seenAt", UNSET)

        _play_time = d.pop("playTime", UNSET)
        play_time: Union[Unset, UserExtendedPlayTime]
        if isinstance(_play_time,  Unset):
            play_time = UNSET
        else:
            play_time = UserExtendedPlayTime.from_dict(_play_time)




        patron = d.pop("patron", UNSET)

        verified = d.pop("verified", UNSET)

        playing = d.pop("playing", UNSET)

        _count = d.pop("count", UNSET)
        count: Union[Unset, UserExtendedCount]
        if isinstance(_count,  Unset):
            count = UNSET
        else:
            count = UserExtendedCount.from_dict(_count)




        streaming = d.pop("streaming", UNSET)

        _streamer = d.pop("streamer", UNSET)
        streamer: Union[Unset, UserExtendedStreamer]
        if isinstance(_streamer,  Unset):
            streamer = UNSET
        else:
            streamer = UserExtendedStreamer.from_dict(_streamer)




        followable = d.pop("followable", UNSET)

        following = d.pop("following", UNSET)

        blocking = d.pop("blocking", UNSET)

        user_extended = cls(
            id=id,
            username=username,
            url=url,
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
            playing=playing,
            count=count,
            streaming=streaming,
            streamer=streamer,
            followable=followable,
            following=following,
            blocking=blocking,
        )


        user_extended.additional_properties = d
        return user_extended

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
