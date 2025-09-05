from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.user_note_to import UserNoteTo
  from ..models.user_note_from import UserNoteFrom





T = TypeVar("T", bound="UserNote")



@_attrs_define
class UserNote:
    """ 
        Attributes:
            from_ (Union[Unset, UserNoteFrom]):
            to (Union[Unset, UserNoteTo]):
            text (Union[Unset, str]):  Example: This is a note.
            date (Union[Unset, int]):  Example: 1290415680000.
     """

    from_: Union[Unset, 'UserNoteFrom'] = UNSET
    to: Union[Unset, 'UserNoteTo'] = UNSET
    text: Union[Unset, str] = UNSET
    date: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_note_to import UserNoteTo
        from ..models.user_note_from import UserNoteFrom
        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        text = self.text

        date = self.date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if text is not UNSET:
            field_dict["text"] = text
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_note_to import UserNoteTo
        from ..models.user_note_from import UserNoteFrom
        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, UserNoteFrom]
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = UserNoteFrom.from_dict(_from_)




        _to = d.pop("to", UNSET)
        to: Union[Unset, UserNoteTo]
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = UserNoteTo.from_dict(_to)




        text = d.pop("text", UNSET)

        date = d.pop("date", UNSET)

        user_note = cls(
            from_=from_,
            to=to,
            text=text,
            date=date,
        )


        user_note.additional_properties = d
        return user_note

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
