from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_ai_body_color import ChallengeAiBodyColor
from ..models.challenge_ai_body_days import ChallengeAiBodyDays
from ..models.challenge_ai_body_variant import ChallengeAiBodyVariant
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ChallengeAiBody")



@_attrs_define
class ChallengeAiBody:
    """ 
        Attributes:
            level (float): AI strength
            clock_limit (Union[Unset, float]): Clock initial time in seconds. If empty, a correspondence game is created.
                Example: 300.
            clock_increment (Union[Unset, int]): Clock increment in seconds. If empty, a correspondence game is created.
                Example: 1.
            days (Union[Unset, ChallengeAiBodyDays]): Days per move, for correspondence games. Clock settings must be
                omitted.
            color (Union[Unset, ChallengeAiBodyColor]): Which color you get to play Default: ChallengeAiBodyColor.RANDOM.
            variant (Union[Unset, ChallengeAiBodyVariant]):  Default: ChallengeAiBodyVariant.STANDARD. Example: standard.
            fen (Union[Unset, str]): Custom initial position (in FEN). Variant must be standard, fromPosition, or chess960
                (if a valid 960 starting position), and the game cannot be rated. Default:
                'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'.
     """

    level: float
    clock_limit: Union[Unset, float] = UNSET
    clock_increment: Union[Unset, int] = UNSET
    days: Union[Unset, ChallengeAiBodyDays] = UNSET
    color: Union[Unset, ChallengeAiBodyColor] = ChallengeAiBodyColor.RANDOM
    variant: Union[Unset, ChallengeAiBodyVariant] = ChallengeAiBodyVariant.STANDARD
    fen: Union[Unset, str] = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        level = self.level

        clock_limit = self.clock_limit

        clock_increment = self.clock_increment

        days: Union[Unset, int] = UNSET
        if not isinstance(self.days, Unset):
            days = self.days.value


        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value


        variant: Union[Unset, str] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.value


        fen = self.fen


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "level": level,
        })
        if clock_limit is not UNSET:
            field_dict["clock.limit"] = clock_limit
        if clock_increment is not UNSET:
            field_dict["clock.increment"] = clock_increment
        if days is not UNSET:
            field_dict["days"] = days
        if color is not UNSET:
            field_dict["color"] = color
        if variant is not UNSET:
            field_dict["variant"] = variant
        if fen is not UNSET:
            field_dict["fen"] = fen

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        level = d.pop("level")

        clock_limit = d.pop("clock.limit", UNSET)

        clock_increment = d.pop("clock.increment", UNSET)

        _days = d.pop("days", UNSET)
        days: Union[Unset, ChallengeAiBodyDays]
        if isinstance(_days,  Unset):
            days = UNSET
        else:
            days = ChallengeAiBodyDays(_days)




        _color = d.pop("color", UNSET)
        color: Union[Unset, ChallengeAiBodyColor]
        if isinstance(_color,  Unset):
            color = UNSET
        else:
            color = ChallengeAiBodyColor(_color)




        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, ChallengeAiBodyVariant]
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = ChallengeAiBodyVariant(_variant)




        fen = d.pop("fen", UNSET)

        challenge_ai_body = cls(
            level=level,
            clock_limit=clock_limit,
            clock_increment=clock_increment,
            days=days,
            color=color,
            variant=variant,
            fen=fen,
        )


        challenge_ai_body.additional_properties = d
        return challenge_ai_body

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
