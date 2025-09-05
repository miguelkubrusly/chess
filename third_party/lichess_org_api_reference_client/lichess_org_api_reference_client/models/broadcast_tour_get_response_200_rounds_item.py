from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.broadcast_tour_get_response_200_rounds_item_custom_scoring import BroadcastTourGetResponse200RoundsItemCustomScoring





T = TypeVar("T", bound="BroadcastTourGetResponse200RoundsItem")



@_attrs_define
class BroadcastTourGetResponse200RoundsItem:
    """ 
        Attributes:
            id (str):
            name (str):
            slug (str):
            created_at (int):
            rated (bool): Whether the round is used for rating calculations
            url (str):
            ongoing (Union[Unset, bool]):
            starts_at (Union[Unset, int]):
            starts_after_previous (Union[Unset, bool]): The start date/time is unknown and the round will start
                automatically when the previous round completes
            finished_at (Union[Unset, int]):
            finished (Union[Unset, bool]):
            delay (Union[Unset, int]):
            custom_scoring (Union[Unset, BroadcastTourGetResponse200RoundsItemCustomScoring]): Scoring overrides for wins or
                draws.
     """

    id: str
    name: str
    slug: str
    created_at: int
    rated: bool
    url: str
    ongoing: Union[Unset, bool] = UNSET
    starts_at: Union[Unset, int] = UNSET
    starts_after_previous: Union[Unset, bool] = UNSET
    finished_at: Union[Unset, int] = UNSET
    finished: Union[Unset, bool] = UNSET
    delay: Union[Unset, int] = UNSET
    custom_scoring: Union[Unset, 'BroadcastTourGetResponse200RoundsItemCustomScoring'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_tour_get_response_200_rounds_item_custom_scoring import BroadcastTourGetResponse200RoundsItemCustomScoring
        id = self.id

        name = self.name

        slug = self.slug

        created_at = self.created_at

        rated = self.rated

        url = self.url

        ongoing = self.ongoing

        starts_at = self.starts_at

        starts_after_previous = self.starts_after_previous

        finished_at = self.finished_at

        finished = self.finished

        delay = self.delay

        custom_scoring: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_scoring, Unset):
            custom_scoring = self.custom_scoring.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "slug": slug,
            "createdAt": created_at,
            "rated": rated,
            "url": url,
        })
        if ongoing is not UNSET:
            field_dict["ongoing"] = ongoing
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at
        if starts_after_previous is not UNSET:
            field_dict["startsAfterPrevious"] = starts_after_previous
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if finished is not UNSET:
            field_dict["finished"] = finished
        if delay is not UNSET:
            field_dict["delay"] = delay
        if custom_scoring is not UNSET:
            field_dict["customScoring"] = custom_scoring

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_tour_get_response_200_rounds_item_custom_scoring import BroadcastTourGetResponse200RoundsItemCustomScoring
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        created_at = d.pop("createdAt")

        rated = d.pop("rated")

        url = d.pop("url")

        ongoing = d.pop("ongoing", UNSET)

        starts_at = d.pop("startsAt", UNSET)

        starts_after_previous = d.pop("startsAfterPrevious", UNSET)

        finished_at = d.pop("finishedAt", UNSET)

        finished = d.pop("finished", UNSET)

        delay = d.pop("delay", UNSET)

        _custom_scoring = d.pop("customScoring", UNSET)
        custom_scoring: Union[Unset, BroadcastTourGetResponse200RoundsItemCustomScoring]
        if isinstance(_custom_scoring,  Unset):
            custom_scoring = UNSET
        else:
            custom_scoring = BroadcastTourGetResponse200RoundsItemCustomScoring.from_dict(_custom_scoring)




        broadcast_tour_get_response_200_rounds_item = cls(
            id=id,
            name=name,
            slug=slug,
            created_at=created_at,
            rated=rated,
            url=url,
            ongoing=ongoing,
            starts_at=starts_at,
            starts_after_previous=starts_after_previous,
            finished_at=finished_at,
            finished=finished,
            delay=delay,
            custom_scoring=custom_scoring,
        )


        broadcast_tour_get_response_200_rounds_item.additional_properties = d
        return broadcast_tour_get_response_200_rounds_item

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
