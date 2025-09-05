from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.account_me_response_200_streamer_you_tube import AccountMeResponse200StreamerYouTube
  from ..models.account_me_response_200_streamer_twitch import AccountMeResponse200StreamerTwitch





T = TypeVar("T", bound="AccountMeResponse200Streamer")



@_attrs_define
class AccountMeResponse200Streamer:
    """ 
        Attributes:
            twitch (Union[Unset, AccountMeResponse200StreamerTwitch]):
            you_tube (Union[Unset, AccountMeResponse200StreamerYouTube]):
     """

    twitch: Union[Unset, 'AccountMeResponse200StreamerTwitch'] = UNSET
    you_tube: Union[Unset, 'AccountMeResponse200StreamerYouTube'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_me_response_200_streamer_you_tube import AccountMeResponse200StreamerYouTube
        from ..models.account_me_response_200_streamer_twitch import AccountMeResponse200StreamerTwitch
        twitch: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.twitch, Unset):
            twitch = self.twitch.to_dict()

        you_tube: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.you_tube, Unset):
            you_tube = self.you_tube.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if twitch is not UNSET:
            field_dict["twitch"] = twitch
        if you_tube is not UNSET:
            field_dict["youTube"] = you_tube

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_me_response_200_streamer_you_tube import AccountMeResponse200StreamerYouTube
        from ..models.account_me_response_200_streamer_twitch import AccountMeResponse200StreamerTwitch
        d = dict(src_dict)
        _twitch = d.pop("twitch", UNSET)
        twitch: Union[Unset, AccountMeResponse200StreamerTwitch]
        if isinstance(_twitch,  Unset):
            twitch = UNSET
        else:
            twitch = AccountMeResponse200StreamerTwitch.from_dict(_twitch)




        _you_tube = d.pop("youTube", UNSET)
        you_tube: Union[Unset, AccountMeResponse200StreamerYouTube]
        if isinstance(_you_tube,  Unset):
            you_tube = UNSET
        else:
            you_tube = AccountMeResponse200StreamerYouTube.from_dict(_you_tube)




        account_me_response_200_streamer = cls(
            twitch=twitch,
            you_tube=you_tube,
        )


        account_me_response_200_streamer.additional_properties = d
        return account_me_response_200_streamer

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
