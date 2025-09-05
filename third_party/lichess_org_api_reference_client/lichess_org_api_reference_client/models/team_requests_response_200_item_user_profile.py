from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TeamRequestsResponse200ItemUserProfile")



@_attrs_define
class TeamRequestsResponse200ItemUserProfile:
    """ 
        Attributes:
            flag (Union[Unset, str]):  Example: EC.
            location (Union[Unset, str]):
            bio (Union[Unset, str]):  Example: Free bugs!.
            real_name (Union[Unset, str]):  Example: Thibault Duplessis.
            fide_rating (Union[Unset, int]): only appears if a user has set them Example: 1500.
            uscf_rating (Union[Unset, int]): only appears if a user has set them Example: 1500.
            ecf_rating (Union[Unset, int]): only appears if a user has set them Example: 1500.
            cfc_rating (Union[Unset, int]): only appears if a user has set them Example: 1500.
            rcf_rating (Union[Unset, int]): only appears if a user has set them Example: 1500.
            dsb_rating (Union[Unset, int]): only appears if a user has set them Example: 1500.
            links (Union[Unset, str]):  Example: github.com/ornicar
                mas.to/@thibault.
     """

    flag: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    bio: Union[Unset, str] = UNSET
    real_name: Union[Unset, str] = UNSET
    fide_rating: Union[Unset, int] = UNSET
    uscf_rating: Union[Unset, int] = UNSET
    ecf_rating: Union[Unset, int] = UNSET
    cfc_rating: Union[Unset, int] = UNSET
    rcf_rating: Union[Unset, int] = UNSET
    dsb_rating: Union[Unset, int] = UNSET
    links: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        flag = self.flag

        location = self.location

        bio = self.bio

        real_name = self.real_name

        fide_rating = self.fide_rating

        uscf_rating = self.uscf_rating

        ecf_rating = self.ecf_rating

        cfc_rating = self.cfc_rating

        rcf_rating = self.rcf_rating

        dsb_rating = self.dsb_rating

        links = self.links


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if flag is not UNSET:
            field_dict["flag"] = flag
        if location is not UNSET:
            field_dict["location"] = location
        if bio is not UNSET:
            field_dict["bio"] = bio
        if real_name is not UNSET:
            field_dict["realName"] = real_name
        if fide_rating is not UNSET:
            field_dict["fideRating"] = fide_rating
        if uscf_rating is not UNSET:
            field_dict["uscfRating"] = uscf_rating
        if ecf_rating is not UNSET:
            field_dict["ecfRating"] = ecf_rating
        if cfc_rating is not UNSET:
            field_dict["cfcRating"] = cfc_rating
        if rcf_rating is not UNSET:
            field_dict["rcfRating"] = rcf_rating
        if dsb_rating is not UNSET:
            field_dict["dsbRating"] = dsb_rating
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        flag = d.pop("flag", UNSET)

        location = d.pop("location", UNSET)

        bio = d.pop("bio", UNSET)

        real_name = d.pop("realName", UNSET)

        fide_rating = d.pop("fideRating", UNSET)

        uscf_rating = d.pop("uscfRating", UNSET)

        ecf_rating = d.pop("ecfRating", UNSET)

        cfc_rating = d.pop("cfcRating", UNSET)

        rcf_rating = d.pop("rcfRating", UNSET)

        dsb_rating = d.pop("dsbRating", UNSET)

        links = d.pop("links", UNSET)

        team_requests_response_200_item_user_profile = cls(
            flag=flag,
            location=location,
            bio=bio,
            real_name=real_name,
            fide_rating=fide_rating,
            uscf_rating=uscf_rating,
            ecf_rating=ecf_rating,
            cfc_rating=cfc_rating,
            rcf_rating=rcf_rating,
            dsb_rating=dsb_rating,
            links=links,
        )


        team_requests_response_200_item_user_profile.additional_properties = d
        return team_requests_response_200_item_user_profile

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
