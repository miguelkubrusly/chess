from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.broadcast_round_tour_info_fide_tc import BroadcastRoundTourInfoFideTc
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="BroadcastRoundTourInfo")



@_attrs_define
class BroadcastRoundTourInfo:
    """ Additional display information about the tournament

        Attributes:
            website (Union[Unset, str]): Official website. External website URL
            players (Union[Unset, str]): Featured players
            location (Union[Unset, str]): Tournament location
            tc (Union[Unset, str]): Time control
            fide_tc (Union[Unset, BroadcastRoundTourInfoFideTc]): FIDE rating category
            time_zone (Union[Unset, str]): Timezone of the tournament. Example: `America/New_York`.
                See [list of possible timezone identifiers](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for
                more.
            standings (Union[Unset, str]): Official standings website. External website URL
            format_ (Union[Unset, str]): Tournament format
     """

    website: Union[Unset, str] = UNSET
    players: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    tc: Union[Unset, str] = UNSET
    fide_tc: Union[Unset, BroadcastRoundTourInfoFideTc] = UNSET
    time_zone: Union[Unset, str] = UNSET
    standings: Union[Unset, str] = UNSET
    format_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        website = self.website

        players = self.players

        location = self.location

        tc = self.tc

        fide_tc: Union[Unset, str] = UNSET
        if not isinstance(self.fide_tc, Unset):
            fide_tc = self.fide_tc.value


        time_zone = self.time_zone

        standings = self.standings

        format_ = self.format_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if website is not UNSET:
            field_dict["website"] = website
        if players is not UNSET:
            field_dict["players"] = players
        if location is not UNSET:
            field_dict["location"] = location
        if tc is not UNSET:
            field_dict["tc"] = tc
        if fide_tc is not UNSET:
            field_dict["fideTc"] = fide_tc
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if standings is not UNSET:
            field_dict["standings"] = standings
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        website = d.pop("website", UNSET)

        players = d.pop("players", UNSET)

        location = d.pop("location", UNSET)

        tc = d.pop("tc", UNSET)

        _fide_tc = d.pop("fideTc", UNSET)
        fide_tc: Union[Unset, BroadcastRoundTourInfoFideTc]
        if isinstance(_fide_tc,  Unset):
            fide_tc = UNSET
        else:
            fide_tc = BroadcastRoundTourInfoFideTc(_fide_tc)




        time_zone = d.pop("timeZone", UNSET)

        standings = d.pop("standings", UNSET)

        format_ = d.pop("format", UNSET)

        broadcast_round_tour_info = cls(
            website=website,
            players=players,
            location=location,
            tc=tc,
            fide_tc=fide_tc,
            time_zone=time_zone,
            standings=standings,
            format_=format_,
        )


        broadcast_round_tour_info.additional_properties = d
        return broadcast_round_tour_info

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
