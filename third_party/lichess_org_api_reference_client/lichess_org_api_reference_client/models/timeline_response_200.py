from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.timeline_response_200_entries_item_type_1 import TimelineResponse200EntriesItemType1
  from ..models.timeline_response_200_entries_item_type_13 import TimelineResponse200EntriesItemType13
  from ..models.timeline_response_200_entries_item_type_5 import TimelineResponse200EntriesItemType5
  from ..models.timeline_response_200_entries_item_type_2 import TimelineResponse200EntriesItemType2
  from ..models.timeline_response_200_entries_item_type_0 import TimelineResponse200EntriesItemType0
  from ..models.timeline_response_200_entries_item_type_10 import TimelineResponse200EntriesItemType10
  from ..models.timeline_response_200_users import TimelineResponse200Users
  from ..models.timeline_response_200_entries_item_type_9 import TimelineResponse200EntriesItemType9
  from ..models.timeline_response_200_entries_item_type_7 import TimelineResponse200EntriesItemType7
  from ..models.timeline_response_200_entries_item_type_3 import TimelineResponse200EntriesItemType3
  from ..models.timeline_response_200_entries_item_type_4 import TimelineResponse200EntriesItemType4
  from ..models.timeline_response_200_entries_item_type_8 import TimelineResponse200EntriesItemType8
  from ..models.timeline_response_200_entries_item_type_12 import TimelineResponse200EntriesItemType12
  from ..models.timeline_response_200_entries_item_type_11 import TimelineResponse200EntriesItemType11
  from ..models.timeline_response_200_entries_item_type_6 import TimelineResponse200EntriesItemType6





T = TypeVar("T", bound="TimelineResponse200")



@_attrs_define
class TimelineResponse200:
    """ 
        Example:
            {'entries': [{'type': 'follow', 'data': {'u1': 'neio', 'u2': 'chess-network'}, 'date': 1644232201429}, {'type':
                'team-join', 'data': {'userId': 'neio', 'teamId': 'coders'}, 'date': 1644232201429}, {'type': 'team-create',
                'data': {'userId': 'neio', 'teamId': 'coders'}, 'date': 1644232201429}, {'type': 'forum-post', 'data':
                {'userId': 'neio', 'topicId': 'AAAAAAAN', 'topicName': "World's Tallest LEGO Tower Completed in City Square",
                'postId': 'AAAAAAAL'}, 'date': 1644232201429}, {'type': 'ublog-post', 'data': {'userId': 'neio', 'id':
                'og5pkt1c', 'slug': 'gotta-go-fast', 'title': 'Gotta Go Fast'}, 'date': 1644232201429}, {'type': 'tour-join',
                'data': {'userId': 'chess-network', 'tourId': 'Z24oxqgU', 'tourName': 'Daily Blitz Arena'}, 'date':
                1644232201429}, {'type': 'game-end', 'data': {'fullId': 'iGkAXUdEfLZC', 'perf': 'correspondence', 'opponent':
                'chess-network', 'win': False}, 'date': 1644232201429}, {'type': 'simul-create', 'data': {'userId': 'neio',
                'simulId': 'm3c0Wvu3', 'simulName': 'RCA 1st Jan simul'}, 'date': 1644232201429}, {'type': 'simul-join', 'data':
                {'userId': 'chess-network', 'simulId': 'm3c0Wvu3', 'simulName': 'RCA 1st Jan simul'}, 'date': 1644232201429},
                {'type': 'study-like', 'data': {'userId': 'neio', 'studyId': 'ma5AvZ7o', 'studyName': 'Free wins | Danish
                Gambit'}, 'date': 1644232201429}, {'type': 'plan-start', 'data': {'userId': 'chess-network'}, 'date':
                1644232201429}, {'type': 'plan-renew', 'data': {'userId': 'chess-network', 'months': 64}, 'date':
                1644232201429}, {'type': 'blog-post', 'data': {'id': 'ZUviXRIAACYAVtMm', 'slug': 'lichess-development-made-easy-
                with-gitpod', 'title': 'Lichess Development Made Easy With Gitpod'}, 'date': 1644232201429}, {'type': 'ublog-
                post-like', 'data': {'userId': 'neio', 'id': 'ZUviXRIAACYAVtMm', 'title': 'Lichess Development Made Easy With
                Gitpod'}, 'date': 1644232201429}, {'type': 'stream-start', 'data': {'id': 'chess-network', 'title': 'Streamers
                Battle December !team | lichess.org'}, 'date': 1644232201429}], 'users': {'neio': {'id': 'neio', 'name': 'Neio',
                'title': 'NM'}, 'chess-network': {'id': 'chess-network', 'name': 'Chess-Network', 'title': 'NM', 'patron':
                True}}}

        Attributes:
            entries (list[Union['TimelineResponse200EntriesItemType0', 'TimelineResponse200EntriesItemType1',
                'TimelineResponse200EntriesItemType10', 'TimelineResponse200EntriesItemType11',
                'TimelineResponse200EntriesItemType12', 'TimelineResponse200EntriesItemType13',
                'TimelineResponse200EntriesItemType2', 'TimelineResponse200EntriesItemType3',
                'TimelineResponse200EntriesItemType4', 'TimelineResponse200EntriesItemType5',
                'TimelineResponse200EntriesItemType6', 'TimelineResponse200EntriesItemType7',
                'TimelineResponse200EntriesItemType8', 'TimelineResponse200EntriesItemType9']]):
            users (TimelineResponse200Users):
     """

    entries: list[Union['TimelineResponse200EntriesItemType0', 'TimelineResponse200EntriesItemType1', 'TimelineResponse200EntriesItemType10', 'TimelineResponse200EntriesItemType11', 'TimelineResponse200EntriesItemType12', 'TimelineResponse200EntriesItemType13', 'TimelineResponse200EntriesItemType2', 'TimelineResponse200EntriesItemType3', 'TimelineResponse200EntriesItemType4', 'TimelineResponse200EntriesItemType5', 'TimelineResponse200EntriesItemType6', 'TimelineResponse200EntriesItemType7', 'TimelineResponse200EntriesItemType8', 'TimelineResponse200EntriesItemType9']]
    users: 'TimelineResponse200Users'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.timeline_response_200_entries_item_type_1 import TimelineResponse200EntriesItemType1
        from ..models.timeline_response_200_entries_item_type_13 import TimelineResponse200EntriesItemType13
        from ..models.timeline_response_200_entries_item_type_5 import TimelineResponse200EntriesItemType5
        from ..models.timeline_response_200_entries_item_type_2 import TimelineResponse200EntriesItemType2
        from ..models.timeline_response_200_entries_item_type_0 import TimelineResponse200EntriesItemType0
        from ..models.timeline_response_200_entries_item_type_10 import TimelineResponse200EntriesItemType10
        from ..models.timeline_response_200_users import TimelineResponse200Users
        from ..models.timeline_response_200_entries_item_type_9 import TimelineResponse200EntriesItemType9
        from ..models.timeline_response_200_entries_item_type_7 import TimelineResponse200EntriesItemType7
        from ..models.timeline_response_200_entries_item_type_3 import TimelineResponse200EntriesItemType3
        from ..models.timeline_response_200_entries_item_type_4 import TimelineResponse200EntriesItemType4
        from ..models.timeline_response_200_entries_item_type_8 import TimelineResponse200EntriesItemType8
        from ..models.timeline_response_200_entries_item_type_12 import TimelineResponse200EntriesItemType12
        from ..models.timeline_response_200_entries_item_type_11 import TimelineResponse200EntriesItemType11
        from ..models.timeline_response_200_entries_item_type_6 import TimelineResponse200EntriesItemType6
        entries = []
        for entries_item_data in self.entries:
            entries_item: dict[str, Any]
            if isinstance(entries_item_data, TimelineResponse200EntriesItemType0):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType1):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType2):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType3):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType4):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType5):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType6):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType7):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType8):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType9):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType10):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType11):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineResponse200EntriesItemType12):
                entries_item = entries_item_data.to_dict()
            else:
                entries_item = entries_item_data.to_dict()

            entries.append(entries_item)



        users = self.users.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "entries": entries,
            "users": users,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeline_response_200_entries_item_type_1 import TimelineResponse200EntriesItemType1
        from ..models.timeline_response_200_entries_item_type_13 import TimelineResponse200EntriesItemType13
        from ..models.timeline_response_200_entries_item_type_5 import TimelineResponse200EntriesItemType5
        from ..models.timeline_response_200_entries_item_type_2 import TimelineResponse200EntriesItemType2
        from ..models.timeline_response_200_entries_item_type_0 import TimelineResponse200EntriesItemType0
        from ..models.timeline_response_200_entries_item_type_10 import TimelineResponse200EntriesItemType10
        from ..models.timeline_response_200_users import TimelineResponse200Users
        from ..models.timeline_response_200_entries_item_type_9 import TimelineResponse200EntriesItemType9
        from ..models.timeline_response_200_entries_item_type_7 import TimelineResponse200EntriesItemType7
        from ..models.timeline_response_200_entries_item_type_3 import TimelineResponse200EntriesItemType3
        from ..models.timeline_response_200_entries_item_type_4 import TimelineResponse200EntriesItemType4
        from ..models.timeline_response_200_entries_item_type_8 import TimelineResponse200EntriesItemType8
        from ..models.timeline_response_200_entries_item_type_12 import TimelineResponse200EntriesItemType12
        from ..models.timeline_response_200_entries_item_type_11 import TimelineResponse200EntriesItemType11
        from ..models.timeline_response_200_entries_item_type_6 import TimelineResponse200EntriesItemType6
        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in (_entries):
            def _parse_entries_item(data: object) -> Union['TimelineResponse200EntriesItemType0', 'TimelineResponse200EntriesItemType1', 'TimelineResponse200EntriesItemType10', 'TimelineResponse200EntriesItemType11', 'TimelineResponse200EntriesItemType12', 'TimelineResponse200EntriesItemType13', 'TimelineResponse200EntriesItemType2', 'TimelineResponse200EntriesItemType3', 'TimelineResponse200EntriesItemType4', 'TimelineResponse200EntriesItemType5', 'TimelineResponse200EntriesItemType6', 'TimelineResponse200EntriesItemType7', 'TimelineResponse200EntriesItemType8', 'TimelineResponse200EntriesItemType9']:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_0 = TimelineResponse200EntriesItemType0.from_dict(data)



                    return entries_item_type_0
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_1 = TimelineResponse200EntriesItemType1.from_dict(data)



                    return entries_item_type_1
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_2 = TimelineResponse200EntriesItemType2.from_dict(data)



                    return entries_item_type_2
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_3 = TimelineResponse200EntriesItemType3.from_dict(data)



                    return entries_item_type_3
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_4 = TimelineResponse200EntriesItemType4.from_dict(data)



                    return entries_item_type_4
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_5 = TimelineResponse200EntriesItemType5.from_dict(data)



                    return entries_item_type_5
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_6 = TimelineResponse200EntriesItemType6.from_dict(data)



                    return entries_item_type_6
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_7 = TimelineResponse200EntriesItemType7.from_dict(data)



                    return entries_item_type_7
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_8 = TimelineResponse200EntriesItemType8.from_dict(data)



                    return entries_item_type_8
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_9 = TimelineResponse200EntriesItemType9.from_dict(data)



                    return entries_item_type_9
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_10 = TimelineResponse200EntriesItemType10.from_dict(data)



                    return entries_item_type_10
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_11 = TimelineResponse200EntriesItemType11.from_dict(data)



                    return entries_item_type_11
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_12 = TimelineResponse200EntriesItemType12.from_dict(data)



                    return entries_item_type_12
                except: # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                entries_item_type_13 = TimelineResponse200EntriesItemType13.from_dict(data)



                return entries_item_type_13

            entries_item = _parse_entries_item(entries_item_data)

            entries.append(entries_item)


        users = TimelineResponse200Users.from_dict(d.pop("users"))




        timeline_response_200 = cls(
            entries=entries,
            users=users,
        )


        timeline_response_200.additional_properties = d
        return timeline_response_200

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
