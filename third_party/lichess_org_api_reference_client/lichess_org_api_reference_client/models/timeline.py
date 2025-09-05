from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.timeline_entries_item_type_5 import TimelineEntriesItemType5
  from ..models.timeline_entries_item_type_1 import TimelineEntriesItemType1
  from ..models.timeline_entries_item_type_7 import TimelineEntriesItemType7
  from ..models.timeline_entries_item_type_13 import TimelineEntriesItemType13
  from ..models.timeline_entries_item_type_4 import TimelineEntriesItemType4
  from ..models.timeline_entries_item_type_8 import TimelineEntriesItemType8
  from ..models.timeline_entries_item_type_2 import TimelineEntriesItemType2
  from ..models.timeline_entries_item_type_9 import TimelineEntriesItemType9
  from ..models.timeline_entries_item_type_10 import TimelineEntriesItemType10
  from ..models.timeline_entries_item_type_12 import TimelineEntriesItemType12
  from ..models.timeline_entries_item_type_6 import TimelineEntriesItemType6
  from ..models.timeline_entries_item_type_0 import TimelineEntriesItemType0
  from ..models.timeline_users import TimelineUsers
  from ..models.timeline_entries_item_type_11 import TimelineEntriesItemType11
  from ..models.timeline_entries_item_type_3 import TimelineEntriesItemType3





T = TypeVar("T", bound="Timeline")



@_attrs_define
class Timeline:
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
            entries (list[Union['TimelineEntriesItemType0', 'TimelineEntriesItemType1', 'TimelineEntriesItemType10',
                'TimelineEntriesItemType11', 'TimelineEntriesItemType12', 'TimelineEntriesItemType13',
                'TimelineEntriesItemType2', 'TimelineEntriesItemType3', 'TimelineEntriesItemType4', 'TimelineEntriesItemType5',
                'TimelineEntriesItemType6', 'TimelineEntriesItemType7', 'TimelineEntriesItemType8',
                'TimelineEntriesItemType9']]):
            users (TimelineUsers):
     """

    entries: list[Union['TimelineEntriesItemType0', 'TimelineEntriesItemType1', 'TimelineEntriesItemType10', 'TimelineEntriesItemType11', 'TimelineEntriesItemType12', 'TimelineEntriesItemType13', 'TimelineEntriesItemType2', 'TimelineEntriesItemType3', 'TimelineEntriesItemType4', 'TimelineEntriesItemType5', 'TimelineEntriesItemType6', 'TimelineEntriesItemType7', 'TimelineEntriesItemType8', 'TimelineEntriesItemType9']]
    users: 'TimelineUsers'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.timeline_entries_item_type_5 import TimelineEntriesItemType5
        from ..models.timeline_entries_item_type_1 import TimelineEntriesItemType1
        from ..models.timeline_entries_item_type_7 import TimelineEntriesItemType7
        from ..models.timeline_entries_item_type_13 import TimelineEntriesItemType13
        from ..models.timeline_entries_item_type_4 import TimelineEntriesItemType4
        from ..models.timeline_entries_item_type_8 import TimelineEntriesItemType8
        from ..models.timeline_entries_item_type_2 import TimelineEntriesItemType2
        from ..models.timeline_entries_item_type_9 import TimelineEntriesItemType9
        from ..models.timeline_entries_item_type_10 import TimelineEntriesItemType10
        from ..models.timeline_entries_item_type_12 import TimelineEntriesItemType12
        from ..models.timeline_entries_item_type_6 import TimelineEntriesItemType6
        from ..models.timeline_entries_item_type_0 import TimelineEntriesItemType0
        from ..models.timeline_users import TimelineUsers
        from ..models.timeline_entries_item_type_11 import TimelineEntriesItemType11
        from ..models.timeline_entries_item_type_3 import TimelineEntriesItemType3
        entries = []
        for entries_item_data in self.entries:
            entries_item: dict[str, Any]
            if isinstance(entries_item_data, TimelineEntriesItemType0):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType1):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType2):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType3):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType4):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType5):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType6):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType7):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType8):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType9):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType10):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType11):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, TimelineEntriesItemType12):
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
        from ..models.timeline_entries_item_type_5 import TimelineEntriesItemType5
        from ..models.timeline_entries_item_type_1 import TimelineEntriesItemType1
        from ..models.timeline_entries_item_type_7 import TimelineEntriesItemType7
        from ..models.timeline_entries_item_type_13 import TimelineEntriesItemType13
        from ..models.timeline_entries_item_type_4 import TimelineEntriesItemType4
        from ..models.timeline_entries_item_type_8 import TimelineEntriesItemType8
        from ..models.timeline_entries_item_type_2 import TimelineEntriesItemType2
        from ..models.timeline_entries_item_type_9 import TimelineEntriesItemType9
        from ..models.timeline_entries_item_type_10 import TimelineEntriesItemType10
        from ..models.timeline_entries_item_type_12 import TimelineEntriesItemType12
        from ..models.timeline_entries_item_type_6 import TimelineEntriesItemType6
        from ..models.timeline_entries_item_type_0 import TimelineEntriesItemType0
        from ..models.timeline_users import TimelineUsers
        from ..models.timeline_entries_item_type_11 import TimelineEntriesItemType11
        from ..models.timeline_entries_item_type_3 import TimelineEntriesItemType3
        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in (_entries):
            def _parse_entries_item(data: object) -> Union['TimelineEntriesItemType0', 'TimelineEntriesItemType1', 'TimelineEntriesItemType10', 'TimelineEntriesItemType11', 'TimelineEntriesItemType12', 'TimelineEntriesItemType13', 'TimelineEntriesItemType2', 'TimelineEntriesItemType3', 'TimelineEntriesItemType4', 'TimelineEntriesItemType5', 'TimelineEntriesItemType6', 'TimelineEntriesItemType7', 'TimelineEntriesItemType8', 'TimelineEntriesItemType9']:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_0 = TimelineEntriesItemType0.from_dict(data)



                    return entries_item_type_0
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_1 = TimelineEntriesItemType1.from_dict(data)



                    return entries_item_type_1
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_2 = TimelineEntriesItemType2.from_dict(data)



                    return entries_item_type_2
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_3 = TimelineEntriesItemType3.from_dict(data)



                    return entries_item_type_3
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_4 = TimelineEntriesItemType4.from_dict(data)



                    return entries_item_type_4
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_5 = TimelineEntriesItemType5.from_dict(data)



                    return entries_item_type_5
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_6 = TimelineEntriesItemType6.from_dict(data)



                    return entries_item_type_6
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_7 = TimelineEntriesItemType7.from_dict(data)



                    return entries_item_type_7
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_8 = TimelineEntriesItemType8.from_dict(data)



                    return entries_item_type_8
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_9 = TimelineEntriesItemType9.from_dict(data)



                    return entries_item_type_9
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_10 = TimelineEntriesItemType10.from_dict(data)



                    return entries_item_type_10
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_11 = TimelineEntriesItemType11.from_dict(data)



                    return entries_item_type_11
                except: # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_12 = TimelineEntriesItemType12.from_dict(data)



                    return entries_item_type_12
                except: # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                entries_item_type_13 = TimelineEntriesItemType13.from_dict(data)



                return entries_item_type_13

            entries_item = _parse_entries_item(entries_item_data)

            entries.append(entries_item)


        users = TimelineUsers.from_dict(d.pop("users"))




        timeline = cls(
            entries=entries,
            users=users,
        )


        timeline.additional_properties = d
        return timeline

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
