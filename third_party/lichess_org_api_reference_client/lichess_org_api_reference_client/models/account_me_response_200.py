from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_me_response_200_title import AccountMeResponse200Title
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.account_me_response_200_play_time import AccountMeResponse200PlayTime
  from ..models.account_me_response_200_perfs import AccountMeResponse200Perfs
  from ..models.account_me_response_200_streamer import AccountMeResponse200Streamer
  from ..models.account_me_response_200_profile import AccountMeResponse200Profile
  from ..models.account_me_response_200_count import AccountMeResponse200Count





T = TypeVar("T", bound="AccountMeResponse200")



@_attrs_define
class AccountMeResponse200:
    """ 
        Attributes:
            id (str):  Example: georges.
            username (str):  Example: Georges.
            url (str):  Example: https://lichess.org/@/georges.
            perfs (Union[Unset, AccountMeResponse200Perfs]):
            title (Union[Unset, AccountMeResponse200Title]): only appears if the user is a titled player or a bot user
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            created_at (Union[Unset, int]):  Example: 1290415680000.
            disabled (Union[Unset, bool]): only appears if a user's account is closed
            tos_violation (Union[Unset, bool]): only appears if a user's account is marked for the violation of [Lichess
                TOS](https://lichess.org/terms-of-service)
            profile (Union[Unset, AccountMeResponse200Profile]):
            seen_at (Union[Unset, int]):  Example: 1522636452014.
            play_time (Union[Unset, AccountMeResponse200PlayTime]):
            patron (Union[Unset, bool]):  Example: True.
            verified (Union[Unset, bool]):  Example: True.
            playing (Union[Unset, str]):  Example: https://lichess.org/yqfLYJ5E/black.
            count (Union[Unset, AccountMeResponse200Count]):
            streaming (Union[Unset, bool]):
            streamer (Union[Unset, AccountMeResponse200Streamer]):
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
    perfs: Union[Unset, 'AccountMeResponse200Perfs'] = UNSET
    title: Union[Unset, AccountMeResponse200Title] = UNSET
    flair: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    disabled: Union[Unset, bool] = UNSET
    tos_violation: Union[Unset, bool] = UNSET
    profile: Union[Unset, 'AccountMeResponse200Profile'] = UNSET
    seen_at: Union[Unset, int] = UNSET
    play_time: Union[Unset, 'AccountMeResponse200PlayTime'] = UNSET
    patron: Union[Unset, bool] = UNSET
    verified: Union[Unset, bool] = UNSET
    playing: Union[Unset, str] = UNSET
    count: Union[Unset, 'AccountMeResponse200Count'] = UNSET
    streaming: Union[Unset, bool] = UNSET
    streamer: Union[Unset, 'AccountMeResponse200Streamer'] = UNSET
    followable: Union[Unset, bool] = UNSET
    following: Union[Unset, bool] = UNSET
    blocking: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_me_response_200_play_time import AccountMeResponse200PlayTime
        from ..models.account_me_response_200_perfs import AccountMeResponse200Perfs
        from ..models.account_me_response_200_streamer import AccountMeResponse200Streamer
        from ..models.account_me_response_200_profile import AccountMeResponse200Profile
        from ..models.account_me_response_200_count import AccountMeResponse200Count
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
        from ..models.account_me_response_200_play_time import AccountMeResponse200PlayTime
        from ..models.account_me_response_200_perfs import AccountMeResponse200Perfs
        from ..models.account_me_response_200_streamer import AccountMeResponse200Streamer
        from ..models.account_me_response_200_profile import AccountMeResponse200Profile
        from ..models.account_me_response_200_count import AccountMeResponse200Count
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        url = d.pop("url")

        _perfs = d.pop("perfs", UNSET)
        perfs: Union[Unset, AccountMeResponse200Perfs]
        if isinstance(_perfs,  Unset):
            perfs = UNSET
        else:
            perfs = AccountMeResponse200Perfs.from_dict(_perfs)




        _title = d.pop("title", UNSET)
        title: Union[Unset, AccountMeResponse200Title]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = AccountMeResponse200Title(_title)




        flair = d.pop("flair", UNSET)

        created_at = d.pop("createdAt", UNSET)

        disabled = d.pop("disabled", UNSET)

        tos_violation = d.pop("tosViolation", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, AccountMeResponse200Profile]
        if isinstance(_profile,  Unset):
            profile = UNSET
        else:
            profile = AccountMeResponse200Profile.from_dict(_profile)




        seen_at = d.pop("seenAt", UNSET)

        _play_time = d.pop("playTime", UNSET)
        play_time: Union[Unset, AccountMeResponse200PlayTime]
        if isinstance(_play_time,  Unset):
            play_time = UNSET
        else:
            play_time = AccountMeResponse200PlayTime.from_dict(_play_time)




        patron = d.pop("patron", UNSET)

        verified = d.pop("verified", UNSET)

        playing = d.pop("playing", UNSET)

        _count = d.pop("count", UNSET)
        count: Union[Unset, AccountMeResponse200Count]
        if isinstance(_count,  Unset):
            count = UNSET
        else:
            count = AccountMeResponse200Count.from_dict(_count)




        streaming = d.pop("streaming", UNSET)

        _streamer = d.pop("streamer", UNSET)
        streamer: Union[Unset, AccountMeResponse200Streamer]
        if isinstance(_streamer,  Unset):
            streamer = UNSET
        else:
            streamer = AccountMeResponse200Streamer.from_dict(_streamer)




        followable = d.pop("followable", UNSET)

        following = d.pop("following", UNSET)

        blocking = d.pop("blocking", UNSET)

        account_me_response_200 = cls(
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


        account_me_response_200.additional_properties = d
        return account_me_response_200

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
