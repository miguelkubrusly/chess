from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_board_seek_body_variant import ApiBoardSeekBodyVariant
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiBoardSeekBody")



@_attrs_define
class ApiBoardSeekBody:
    """ 
        Attributes:
            rated (Union[Unset, bool]): Whether the game is rated and impacts players ratings. Default: False. Example:
                True.
            variant (Union[Unset, ApiBoardSeekBodyVariant]):  Default: ApiBoardSeekBodyVariant.STANDARD. Example: standard.
            rating_range (Union[Unset, str]): The rating range of potential opponents. Better left empty.
                Example: 1500-1800
     """

    rated: Union[Unset, bool] = False
    variant: Union[Unset, ApiBoardSeekBodyVariant] = ApiBoardSeekBodyVariant.STANDARD
    rating_range: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rated = self.rated

        variant: Union[Unset, str] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.value


        rating_range = self.rating_range


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rated is not UNSET:
            field_dict["rated"] = rated
        if variant is not UNSET:
            field_dict["variant"] = variant
        if rating_range is not UNSET:
            field_dict["ratingRange"] = rating_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rated = d.pop("rated", UNSET)

        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, ApiBoardSeekBodyVariant]
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = ApiBoardSeekBodyVariant(_variant)




        rating_range = d.pop("ratingRange", UNSET)

        api_board_seek_body = cls(
            rated=rated,
            variant=variant,
            rating_range=rating_range,
        )


        api_board_seek_body.additional_properties = d
        return api_board_seek_body

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
