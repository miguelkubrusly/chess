from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_user_activity_response_200_item_posts_item_posts_item import ApiUserActivityResponse200ItemPostsItemPostsItem





T = TypeVar("T", bound="ApiUserActivityResponse200ItemPostsItem")



@_attrs_define
class ApiUserActivityResponse200ItemPostsItem:
    """ 
        Attributes:
            topic_url (str):
            topic_name (str):
            posts (list['ApiUserActivityResponse200ItemPostsItemPostsItem']):
     """

    topic_url: str
    topic_name: str
    posts: list['ApiUserActivityResponse200ItemPostsItemPostsItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_activity_response_200_item_posts_item_posts_item import ApiUserActivityResponse200ItemPostsItemPostsItem
        topic_url = self.topic_url

        topic_name = self.topic_name

        posts = []
        for posts_item_data in self.posts:
            posts_item = posts_item_data.to_dict()
            posts.append(posts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "topicUrl": topic_url,
            "topicName": topic_name,
            "posts": posts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_user_activity_response_200_item_posts_item_posts_item import ApiUserActivityResponse200ItemPostsItemPostsItem
        d = dict(src_dict)
        topic_url = d.pop("topicUrl")

        topic_name = d.pop("topicName")

        posts = []
        _posts = d.pop("posts")
        for posts_item_data in (_posts):
            posts_item = ApiUserActivityResponse200ItemPostsItemPostsItem.from_dict(posts_item_data)



            posts.append(posts_item)


        api_user_activity_response_200_item_posts_item = cls(
            topic_url=topic_url,
            topic_name=topic_name,
            posts=posts,
        )


        api_user_activity_response_200_item_posts_item.additional_properties = d
        return api_user_activity_response_200_item_posts_item

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
