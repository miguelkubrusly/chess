from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TimelineEntriesItemType3Data")



@_attrs_define
class TimelineEntriesItemType3Data:
    """ 
        Attributes:
            user_id (str):
            topic_id (str):
            topic_name (str):
            post_id (str):
     """

    user_id: str
    topic_id: str
    topic_name: str
    post_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        topic_id = self.topic_id

        topic_name = self.topic_name

        post_id = self.post_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "userId": user_id,
            "topicId": topic_id,
            "topicName": topic_name,
            "postId": post_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        topic_id = d.pop("topicId")

        topic_name = d.pop("topicName")

        post_id = d.pop("postId")

        timeline_entries_item_type_3_data = cls(
            user_id=user_id,
            topic_id=topic_id,
            topic_name=topic_name,
            post_id=post_id,
        )


        timeline_entries_item_type_3_data.additional_properties = d
        return timeline_entries_item_type_3_data

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
