from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.streamer_live_response_200_item_title import StreamerLiveResponse200ItemTitle
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.streamer_live_response_200_item_stream import StreamerLiveResponse200ItemStream
  from ..models.streamer_live_response_200_item_streamer import StreamerLiveResponse200ItemStreamer





T = TypeVar("T", bound="StreamerLiveResponse200Item")



@_attrs_define
class StreamerLiveResponse200Item:
    """ 
        Attributes:
            id (str):
            name (str):
            flair (Union[Unset, str]): See [available flair list and images](https://github.com/lichess-
                org/lila/tree/master/public/flair)
            title (Union[Unset, StreamerLiveResponse200ItemTitle]): only appears if the user is a titled player or a bot
                user
            patron (Union[Unset, bool]):
            stream (Union[Unset, StreamerLiveResponse200ItemStream]):
            streamer (Union[Unset, StreamerLiveResponse200ItemStreamer]):
     """

    id: str
    name: str
    flair: Union[Unset, str] = UNSET
    title: Union[Unset, StreamerLiveResponse200ItemTitle] = UNSET
    patron: Union[Unset, bool] = UNSET
    stream: Union[Unset, 'StreamerLiveResponse200ItemStream'] = UNSET
    streamer: Union[Unset, 'StreamerLiveResponse200ItemStreamer'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.streamer_live_response_200_item_stream import StreamerLiveResponse200ItemStream
        from ..models.streamer_live_response_200_item_streamer import StreamerLiveResponse200ItemStreamer
        id = self.id

        name = self.name

        flair = self.flair

        title: Union[Unset, str] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.value


        patron = self.patron

        stream: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stream, Unset):
            stream = self.stream.to_dict()

        streamer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.streamer, Unset):
            streamer = self.streamer.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
        })
        if flair is not UNSET:
            field_dict["flair"] = flair
        if title is not UNSET:
            field_dict["title"] = title
        if patron is not UNSET:
            field_dict["patron"] = patron
        if stream is not UNSET:
            field_dict["stream"] = stream
        if streamer is not UNSET:
            field_dict["streamer"] = streamer

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.streamer_live_response_200_item_stream import StreamerLiveResponse200ItemStream
        from ..models.streamer_live_response_200_item_streamer import StreamerLiveResponse200ItemStreamer
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        flair = d.pop("flair", UNSET)

        _title = d.pop("title", UNSET)
        title: Union[Unset, StreamerLiveResponse200ItemTitle]
        if isinstance(_title,  Unset):
            title = UNSET
        else:
            title = StreamerLiveResponse200ItemTitle(_title)




        patron = d.pop("patron", UNSET)

        _stream = d.pop("stream", UNSET)
        stream: Union[Unset, StreamerLiveResponse200ItemStream]
        if isinstance(_stream,  Unset):
            stream = UNSET
        else:
            stream = StreamerLiveResponse200ItemStream.from_dict(_stream)




        _streamer = d.pop("streamer", UNSET)
        streamer: Union[Unset, StreamerLiveResponse200ItemStreamer]
        if isinstance(_streamer,  Unset):
            streamer = UNSET
        else:
            streamer = StreamerLiveResponse200ItemStreamer.from_dict(_streamer)




        streamer_live_response_200_item = cls(
            id=id,
            name=name,
            flair=flair,
            title=title,
            patron=patron,
            stream=stream,
            streamer=streamer,
        )


        streamer_live_response_200_item.additional_properties = d
        return streamer_live_response_200_item

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
