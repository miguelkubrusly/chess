from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.arena_tournament_full_featured_white import ArenaTournamentFullFeaturedWhite
  from ..models.arena_tournament_full_featured_black import ArenaTournamentFullFeaturedBlack
  from ..models.arena_tournament_full_featured_c import ArenaTournamentFullFeaturedC





T = TypeVar("T", bound="ArenaTournamentFullFeatured")



@_attrs_define
class ArenaTournamentFullFeatured:
    """ 
        Attributes:
            id (Union[Unset, str]):
            fen (Union[Unset, str]):
            orientation (Union[Unset, str]):
            color (Union[Unset, str]):
            last_move (Union[Unset, str]):
            white (Union[Unset, ArenaTournamentFullFeaturedWhite]):
            black (Union[Unset, ArenaTournamentFullFeaturedBlack]):
            c (Union[Unset, ArenaTournamentFullFeaturedC]):
     """

    id: Union[Unset, str] = UNSET
    fen: Union[Unset, str] = UNSET
    orientation: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    last_move: Union[Unset, str] = UNSET
    white: Union[Unset, 'ArenaTournamentFullFeaturedWhite'] = UNSET
    black: Union[Unset, 'ArenaTournamentFullFeaturedBlack'] = UNSET
    c: Union[Unset, 'ArenaTournamentFullFeaturedC'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.arena_tournament_full_featured_white import ArenaTournamentFullFeaturedWhite
        from ..models.arena_tournament_full_featured_black import ArenaTournamentFullFeaturedBlack
        from ..models.arena_tournament_full_featured_c import ArenaTournamentFullFeaturedC
        id = self.id

        fen = self.fen

        orientation = self.orientation

        color = self.color

        last_move = self.last_move

        white: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.white, Unset):
            white = self.white.to_dict()

        black: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.black, Unset):
            black = self.black.to_dict()

        c: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.c, Unset):
            c = self.c.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if fen is not UNSET:
            field_dict["fen"] = fen
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if color is not UNSET:
            field_dict["color"] = color
        if last_move is not UNSET:
            field_dict["lastMove"] = last_move
        if white is not UNSET:
            field_dict["white"] = white
        if black is not UNSET:
            field_dict["black"] = black
        if c is not UNSET:
            field_dict["c"] = c

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.arena_tournament_full_featured_white import ArenaTournamentFullFeaturedWhite
        from ..models.arena_tournament_full_featured_black import ArenaTournamentFullFeaturedBlack
        from ..models.arena_tournament_full_featured_c import ArenaTournamentFullFeaturedC
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        fen = d.pop("fen", UNSET)

        orientation = d.pop("orientation", UNSET)

        color = d.pop("color", UNSET)

        last_move = d.pop("lastMove", UNSET)

        _white = d.pop("white", UNSET)
        white: Union[Unset, ArenaTournamentFullFeaturedWhite]
        if isinstance(_white,  Unset):
            white = UNSET
        else:
            white = ArenaTournamentFullFeaturedWhite.from_dict(_white)




        _black = d.pop("black", UNSET)
        black: Union[Unset, ArenaTournamentFullFeaturedBlack]
        if isinstance(_black,  Unset):
            black = UNSET
        else:
            black = ArenaTournamentFullFeaturedBlack.from_dict(_black)




        _c = d.pop("c", UNSET)
        c: Union[Unset, ArenaTournamentFullFeaturedC]
        if isinstance(_c,  Unset):
            c = UNSET
        else:
            c = ArenaTournamentFullFeaturedC.from_dict(_c)




        arena_tournament_full_featured = cls(
            id=id,
            fen=fen,
            orientation=orientation,
            color=color,
            last_move=last_move,
            white=white,
            black=black,
            c=c,
        )


        arena_tournament_full_featured.additional_properties = d
        return arena_tournament_full_featured

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
