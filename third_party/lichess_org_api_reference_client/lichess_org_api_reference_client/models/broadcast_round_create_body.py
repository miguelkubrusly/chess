from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.broadcast_round_create_body_status import BroadcastRoundCreateBodyStatus
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="BroadcastRoundCreateBody")



@_attrs_define
class BroadcastRoundCreateBody:
    """ 
        Attributes:
            starts_at (Union[Unset, int]): Timestamp in milliseconds of broadcast round start. Leave empty to manually start
                the broadcast round.
                Example: `1356998400070`
            starts_after_previous (Union[Unset, bool]): The start date is unknown, and the round will start automatically
                when the previous round completes.
                 Default: False.
            delay (Union[Unset, int]): Delay in seconds for movements to appear on the broadcast. Leave it empty if you
                don't need it.
                Example: `900` (15 min)
            status (Union[Unset, BroadcastRoundCreateBodyStatus]): Lichess can usually detect the round status, but you can
                also set it manually if needed.
                 Default: BroadcastRoundCreateBodyStatus.NEW.
            rated (Union[Unset, bool]): Whether the round is used when calculating players' rating changes. Default: True.
            custom_scoring_white_win (Union[Unset, float]):
            custom_scoring_white_draw (Union[Unset, float]):
            custom_scoring_black_win (Union[Unset, float]):
            custom_scoring_black_draw (Union[Unset, float]):
            period (Union[Unset, int]): (Only for Admins) Waiting time for each poll.
     """

    starts_at: Union[Unset, int] = UNSET
    starts_after_previous: Union[Unset, bool] = False
    delay: Union[Unset, int] = UNSET
    status: Union[Unset, BroadcastRoundCreateBodyStatus] = BroadcastRoundCreateBodyStatus.NEW
    rated: Union[Unset, bool] = True
    custom_scoring_white_win: Union[Unset, float] = UNSET
    custom_scoring_white_draw: Union[Unset, float] = UNSET
    custom_scoring_black_win: Union[Unset, float] = UNSET
    custom_scoring_black_draw: Union[Unset, float] = UNSET
    period: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        starts_at = self.starts_at

        starts_after_previous = self.starts_after_previous

        delay = self.delay

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        rated = self.rated

        custom_scoring_white_win = self.custom_scoring_white_win

        custom_scoring_white_draw = self.custom_scoring_white_draw

        custom_scoring_black_win = self.custom_scoring_black_win

        custom_scoring_black_draw = self.custom_scoring_black_draw

        period = self.period


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at
        if starts_after_previous is not UNSET:
            field_dict["startsAfterPrevious"] = starts_after_previous
        if delay is not UNSET:
            field_dict["delay"] = delay
        if status is not UNSET:
            field_dict["status"] = status
        if rated is not UNSET:
            field_dict["rated"] = rated
        if custom_scoring_white_win is not UNSET:
            field_dict["customScoring.white.win"] = custom_scoring_white_win
        if custom_scoring_white_draw is not UNSET:
            field_dict["customScoring.white.draw"] = custom_scoring_white_draw
        if custom_scoring_black_win is not UNSET:
            field_dict["customScoring.black.win"] = custom_scoring_black_win
        if custom_scoring_black_draw is not UNSET:
            field_dict["customScoring.black.draw"] = custom_scoring_black_draw
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        starts_at = d.pop("startsAt", UNSET)

        starts_after_previous = d.pop("startsAfterPrevious", UNSET)

        delay = d.pop("delay", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BroadcastRoundCreateBodyStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BroadcastRoundCreateBodyStatus(_status)




        rated = d.pop("rated", UNSET)

        custom_scoring_white_win = d.pop("customScoring.white.win", UNSET)

        custom_scoring_white_draw = d.pop("customScoring.white.draw", UNSET)

        custom_scoring_black_win = d.pop("customScoring.black.win", UNSET)

        custom_scoring_black_draw = d.pop("customScoring.black.draw", UNSET)

        period = d.pop("period", UNSET)

        broadcast_round_create_body = cls(
            starts_at=starts_at,
            starts_after_previous=starts_after_previous,
            delay=delay,
            status=status,
            rated=rated,
            custom_scoring_white_win=custom_scoring_white_win,
            custom_scoring_white_draw=custom_scoring_white_draw,
            custom_scoring_black_win=custom_scoring_black_win,
            custom_scoring_black_draw=custom_scoring_black_draw,
            period=period,
        )


        broadcast_round_create_body.additional_properties = d
        return broadcast_round_create_body

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
