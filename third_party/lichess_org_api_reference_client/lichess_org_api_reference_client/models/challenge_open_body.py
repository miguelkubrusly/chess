from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_open_body_days import ChallengeOpenBodyDays
from ..models.challenge_open_body_rules import ChallengeOpenBodyRules
from ..models.challenge_open_body_variant import ChallengeOpenBodyVariant
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ChallengeOpenBody")



@_attrs_define
class ChallengeOpenBody:
    """ 
        Attributes:
            rated (Union[Unset, bool]): Game is rated and impacts players ratings Default: False.
            clock_limit (Union[Unset, float]): Clock initial time in seconds. If empty, a correspondence game is created.
                Example: 300.
            clock_increment (Union[Unset, int]): Clock increment in seconds. If empty, a correspondence game is created.
                Example: 1.
            days (Union[Unset, ChallengeOpenBodyDays]): Days per turn. For correspondence challenges.
            variant (Union[Unset, ChallengeOpenBodyVariant]):  Default: ChallengeOpenBodyVariant.STANDARD. Example:
                standard.
            fen (Union[Unset, str]): Custom initial position (in FEN). Variant must be standard, fromPosition, or chess960
                (if a valid 960 starting position), and the game cannot be rated. Default:
                'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'.
            name (Union[Unset, str]): Optional name for the challenge, that players will see on the challenge page.
            rules (Union[Unset, ChallengeOpenBodyRules]): Extra game rules separated by commas.
                Example: `noRematch,noGiveTime`
                The `noAbort` rule is available for Lichess admins only
            users (Union[Unset, str]): Optional pair of usernames, separated by a comma.
                If set, only these users will be allowed to join the game.
                The first username gets the white pieces.
                Example: `Username1,Username2`
            expires_at (Union[Unset, int]): Timestamp in milliseconds to expire the challenge. Defaults to 24h after
                creation. Can't be more than 2 weeks after creation.
     """

    rated: Union[Unset, bool] = False
    clock_limit: Union[Unset, float] = UNSET
    clock_increment: Union[Unset, int] = UNSET
    days: Union[Unset, ChallengeOpenBodyDays] = UNSET
    variant: Union[Unset, ChallengeOpenBodyVariant] = ChallengeOpenBodyVariant.STANDARD
    fen: Union[Unset, str] = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    name: Union[Unset, str] = UNSET
    rules: Union[Unset, ChallengeOpenBodyRules] = UNSET
    users: Union[Unset, str] = UNSET
    expires_at: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rated = self.rated

        clock_limit = self.clock_limit

        clock_increment = self.clock_increment

        days: Union[Unset, int] = UNSET
        if not isinstance(self.days, Unset):
            days = self.days.value


        variant: Union[Unset, str] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.value


        fen = self.fen

        name = self.name

        rules: Union[Unset, str] = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.value


        users = self.users

        expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rated is not UNSET:
            field_dict["rated"] = rated
        if clock_limit is not UNSET:
            field_dict["clock.limit"] = clock_limit
        if clock_increment is not UNSET:
            field_dict["clock.increment"] = clock_increment
        if days is not UNSET:
            field_dict["days"] = days
        if variant is not UNSET:
            field_dict["variant"] = variant
        if fen is not UNSET:
            field_dict["fen"] = fen
        if name is not UNSET:
            field_dict["name"] = name
        if rules is not UNSET:
            field_dict["rules"] = rules
        if users is not UNSET:
            field_dict["users"] = users
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rated = d.pop("rated", UNSET)

        clock_limit = d.pop("clock.limit", UNSET)

        clock_increment = d.pop("clock.increment", UNSET)

        _days = d.pop("days", UNSET)
        days: Union[Unset, ChallengeOpenBodyDays]
        if isinstance(_days,  Unset):
            days = UNSET
        else:
            days = ChallengeOpenBodyDays(_days)




        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, ChallengeOpenBodyVariant]
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = ChallengeOpenBodyVariant(_variant)




        fen = d.pop("fen", UNSET)

        name = d.pop("name", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: Union[Unset, ChallengeOpenBodyRules]
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = ChallengeOpenBodyRules(_rules)




        users = d.pop("users", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        challenge_open_body = cls(
            rated=rated,
            clock_limit=clock_limit,
            clock_increment=clock_increment,
            days=days,
            variant=variant,
            fen=fen,
            name=name,
            rules=rules,
            users=users,
            expires_at=expires_at,
        )


        challenge_open_body.additional_properties = d
        return challenge_open_body

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
