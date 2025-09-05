from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_decline_body_reason import ChallengeDeclineBodyReason
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ChallengeDeclineBody")



@_attrs_define
class ChallengeDeclineBody:
    """ 
        Attributes:
            reason (Union[Unset, ChallengeDeclineBodyReason]): Reason challenge was declined. It will be translated to the
                player's language. See [the full list in the translation
                file](https://github.com/ornicar/lila/blob/master/translation/source/challenge.xml#L14).
     """

    reason: Union[Unset, ChallengeDeclineBodyReason] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, ChallengeDeclineBodyReason]
        if isinstance(_reason,  Unset):
            reason = UNSET
        else:
            reason = ChallengeDeclineBodyReason(_reason)




        challenge_decline_body = cls(
            reason=reason,
        )


        challenge_decline_body.additional_properties = d
        return challenge_decline_body

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
