from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.challenge_create_body_color import ChallengeCreateBodyColor
from ..models.challenge_create_body_rules import ChallengeCreateBodyRules
from ..models.challenge_create_body_variant import ChallengeCreateBodyVariant
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ChallengeCreateBody")



@_attrs_define
class ChallengeCreateBody:
    """ 
        Attributes:
            rated (Union[Unset, bool]): Game is rated and impacts players ratings Default: False.
            color (Union[Unset, ChallengeCreateBodyColor]): Which color you get to play Default:
                ChallengeCreateBodyColor.RANDOM.
            variant (Union[Unset, ChallengeCreateBodyVariant]):  Default: ChallengeCreateBodyVariant.STANDARD. Example:
                standard.
            fen (Union[Unset, str]): Custom initial position (in FEN). Variant must be standard, fromPosition, or chess960
                (if a valid 960 starting position), and the game cannot be rated. Default:
                'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'.
            keep_alive_stream (Union[Unset, bool]): If set, the response is streamed as
                [ndjson](#section/Introduction/Streaming-with-ND-JSON).
                The challenge is kept alive until the connection is closed by the client.
                When the challenge is accepted, declined or canceled, a message of the form `{"done":"accepted"}` is sent,
                then the connection is closed by the server.
                If not set, the response is not streamed, and the challenge expires after 20s if not accepted.
            rules (Union[Unset, ChallengeCreateBodyRules]): Extra game rules separated by commas.
                Example: `noAbort,noRematch`
     """

    rated: Union[Unset, bool] = False
    color: Union[Unset, ChallengeCreateBodyColor] = ChallengeCreateBodyColor.RANDOM
    variant: Union[Unset, ChallengeCreateBodyVariant] = ChallengeCreateBodyVariant.STANDARD
    fen: Union[Unset, str] = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    keep_alive_stream: Union[Unset, bool] = UNSET
    rules: Union[Unset, ChallengeCreateBodyRules] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rated = self.rated

        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value


        variant: Union[Unset, str] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.value


        fen = self.fen

        keep_alive_stream = self.keep_alive_stream

        rules: Union[Unset, str] = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rated is not UNSET:
            field_dict["rated"] = rated
        if color is not UNSET:
            field_dict["color"] = color
        if variant is not UNSET:
            field_dict["variant"] = variant
        if fen is not UNSET:
            field_dict["fen"] = fen
        if keep_alive_stream is not UNSET:
            field_dict["keepAliveStream"] = keep_alive_stream
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rated = d.pop("rated", UNSET)

        _color = d.pop("color", UNSET)
        color: Union[Unset, ChallengeCreateBodyColor]
        if isinstance(_color,  Unset):
            color = UNSET
        else:
            color = ChallengeCreateBodyColor(_color)




        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, ChallengeCreateBodyVariant]
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = ChallengeCreateBodyVariant(_variant)




        fen = d.pop("fen", UNSET)

        keep_alive_stream = d.pop("keepAliveStream", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: Union[Unset, ChallengeCreateBodyRules]
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = ChallengeCreateBodyRules(_rules)




        challenge_create_body = cls(
            rated=rated,
            color=color,
            variant=variant,
            fen=fen,
            keep_alive_stream=keep_alive_stream,
            rules=rules,
        )


        challenge_create_body.additional_properties = d
        return challenge_create_body

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
