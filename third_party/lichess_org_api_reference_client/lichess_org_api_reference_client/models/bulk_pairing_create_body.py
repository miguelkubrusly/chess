from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bulk_pairing_create_body_days import BulkPairingCreateBodyDays
from ..models.bulk_pairing_create_body_rules import BulkPairingCreateBodyRules
from ..models.bulk_pairing_create_body_variant import BulkPairingCreateBodyVariant
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="BulkPairingCreateBody")



@_attrs_define
class BulkPairingCreateBody:
    """ 
        Attributes:
            players (Union[Unset, str]): OAuth tokens of all the players to pair, with the syntax
                `tokenOfWhitePlayerInGame1:tokenOfBlackPlayerInGame1,tokenOfWhitePlayerInGame2:tokenOfBlackPlayerInGame2,...`.
                The 2 tokens of the players of a game are separated with `:`. The first token gets the white pieces. Games are
                separated with `,`.
                Up to 1000 tokens can be sent, for a max of 500 games.
                Each token must be included at most once.
                Example: `token1:token2,token3:token4,token5:token6`
            clock_limit (Union[Unset, float]): Clock initial time in seconds. Example: `600`
            clock_increment (Union[Unset, int]): Clock increment in seconds. Example: `2`
            days (Union[Unset, BulkPairingCreateBodyDays]): Days per turn. For correspondence games only.
            pair_at (Union[Unset, int]): Date at which the games will be created as a Unix timestamp in milliseconds.
                Up to 7 days in the future.
                Omit, or set to current date and time, to start the games immediately.
                Example: `1612289869919`
            start_clocks_at (Union[Unset, int]): Date at which the clocks will be automatically started as a Unix timestamp
                in milliseconds.
                Up to 7 days in the future.
                Note that the clocks can start earlier than specified, if players start making moves in the game.
                If omitted, the clocks will not start automatically.
                Example: `1612289869919`
            rated (Union[Unset, bool]): Game is rated and impacts players ratings Default: False.
            variant (Union[Unset, BulkPairingCreateBodyVariant]):  Default: BulkPairingCreateBodyVariant.STANDARD. Example:
                standard.
            fen (Union[Unset, str]): Custom initial position (in FEN). Variant must be standard, fromPosition, or chess960
                (if a valid 960 starting position), and the game cannot be rated. Default:
                'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'.
            message (Union[Unset, str]): Message that will be sent to each player, when the game is created.  It is sent
                from your user account.
                `{opponent}` and `{game}` are placeholders that will be replaced with the opponent and the game URLs.
                You can omit this field to send the default message,
                but if you set your own message, it must at least contain the `{game}` placeholder.
                 Default: 'Your game with {opponent} is ready: {game}.'.
            rules (Union[Unset, BulkPairingCreateBodyRules]): Extra game rules separated by commas.
                Example: `noAbort,noRematch`
     """

    players: Union[Unset, str] = UNSET
    clock_limit: Union[Unset, float] = UNSET
    clock_increment: Union[Unset, int] = UNSET
    days: Union[Unset, BulkPairingCreateBodyDays] = UNSET
    pair_at: Union[Unset, int] = UNSET
    start_clocks_at: Union[Unset, int] = UNSET
    rated: Union[Unset, bool] = False
    variant: Union[Unset, BulkPairingCreateBodyVariant] = BulkPairingCreateBodyVariant.STANDARD
    fen: Union[Unset, str] = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    message: Union[Unset, str] = 'Your game with {opponent} is ready: {game}.'
    rules: Union[Unset, BulkPairingCreateBodyRules] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        players = self.players

        clock_limit = self.clock_limit

        clock_increment = self.clock_increment

        days: Union[Unset, int] = UNSET
        if not isinstance(self.days, Unset):
            days = self.days.value


        pair_at = self.pair_at

        start_clocks_at = self.start_clocks_at

        rated = self.rated

        variant: Union[Unset, str] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.value


        fen = self.fen

        message = self.message

        rules: Union[Unset, str] = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if players is not UNSET:
            field_dict["players"] = players
        if clock_limit is not UNSET:
            field_dict["clock.limit"] = clock_limit
        if clock_increment is not UNSET:
            field_dict["clock.increment"] = clock_increment
        if days is not UNSET:
            field_dict["days"] = days
        if pair_at is not UNSET:
            field_dict["pairAt"] = pair_at
        if start_clocks_at is not UNSET:
            field_dict["startClocksAt"] = start_clocks_at
        if rated is not UNSET:
            field_dict["rated"] = rated
        if variant is not UNSET:
            field_dict["variant"] = variant
        if fen is not UNSET:
            field_dict["fen"] = fen
        if message is not UNSET:
            field_dict["message"] = message
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        players = d.pop("players", UNSET)

        clock_limit = d.pop("clock.limit", UNSET)

        clock_increment = d.pop("clock.increment", UNSET)

        _days = d.pop("days", UNSET)
        days: Union[Unset, BulkPairingCreateBodyDays]
        if isinstance(_days,  Unset):
            days = UNSET
        else:
            days = BulkPairingCreateBodyDays(_days)




        pair_at = d.pop("pairAt", UNSET)

        start_clocks_at = d.pop("startClocksAt", UNSET)

        rated = d.pop("rated", UNSET)

        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, BulkPairingCreateBodyVariant]
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = BulkPairingCreateBodyVariant(_variant)




        fen = d.pop("fen", UNSET)

        message = d.pop("message", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: Union[Unset, BulkPairingCreateBodyRules]
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = BulkPairingCreateBodyRules(_rules)




        bulk_pairing_create_body = cls(
            players=players,
            clock_limit=clock_limit,
            clock_increment=clock_increment,
            days=days,
            pair_at=pair_at,
            start_clocks_at=start_clocks_at,
            rated=rated,
            variant=variant,
            fen=fen,
            message=message,
            rules=rules,
        )


        bulk_pairing_create_body.additional_properties = d
        return bulk_pairing_create_body

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
