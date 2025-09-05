from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.study_import_pgn_chapters_chapters_item_players_item import StudyImportPgnChaptersChaptersItemPlayersItem





T = TypeVar("T", bound="StudyImportPgnChaptersChaptersItem")



@_attrs_define
class StudyImportPgnChaptersChaptersItem:
    """ 
        Attributes:
            id (Union[Unset, str]): The chapter ID
            name (Union[Unset, str]): The chapter name
            players (Union[Unset, list['StudyImportPgnChaptersChaptersItemPlayersItem']]):
            status (Union[Unset, str]): The chapter status
     """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    players: Union[Unset, list['StudyImportPgnChaptersChaptersItemPlayersItem']] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.study_import_pgn_chapters_chapters_item_players_item import StudyImportPgnChaptersChaptersItemPlayersItem
        id = self.id

        name = self.name

        players: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)



        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if players is not UNSET:
            field_dict["players"] = players
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.study_import_pgn_chapters_chapters_item_players_item import StudyImportPgnChaptersChaptersItemPlayersItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        players = []
        _players = d.pop("players", UNSET)
        for players_item_data in (_players or []):
            players_item = StudyImportPgnChaptersChaptersItemPlayersItem.from_dict(players_item_data)



            players.append(players_item)


        status = d.pop("status", UNSET)

        study_import_pgn_chapters_chapters_item = cls(
            id=id,
            name=name,
            players=players,
            status=status,
        )


        study_import_pgn_chapters_chapters_item.additional_properties = d
        return study_import_pgn_chapters_chapters_item

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
