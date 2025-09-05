from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bulk_pairing_list_response_200_item_variant import BulkPairingListResponse200ItemVariant
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.bulk_pairing_list_response_200_item_games_item import BulkPairingListResponse200ItemGamesItem
  from ..models.bulk_pairing_list_response_200_item_clock import BulkPairingListResponse200ItemClock





T = TypeVar("T", bound="BulkPairingListResponse200Item")



@_attrs_define
class BulkPairingListResponse200Item:
    """ 
        Example:
            {'id': 'RVAcwgg7', 'games': [{'id': 'NKop9IyD', 'black': 'lizen1', 'white': 'thibault'}, {'id': 'KT8374ut',
                'black': 'lizen3', 'white': 'lizen2'}, {'id': 'wInQr8Sk', 'black': 'lizen5', 'white': 'lizen4'}], 'variant':
                'standard', 'clock': {'increment': 0, 'limit': 300}, 'pairAt': 1612289869919, 'pairedAt': None, 'rated': False,
                'startClocksAt': 1612200422971, 'scheduledAt': 1612203514628}

        Attributes:
            id (str):
            games (list['BulkPairingListResponse200ItemGamesItem']):
            variant (BulkPairingListResponse200ItemVariant):  Default: BulkPairingListResponse200ItemVariant.STANDARD.
                Example: standard.
            clock (BulkPairingListResponse200ItemClock):
            pair_at (int):
            paired_at (Union[None, int]):
            rated (bool):
            start_clocks_at (int):
            scheduled_at (int):
     """

    id: str
    games: list['BulkPairingListResponse200ItemGamesItem']
    clock: 'BulkPairingListResponse200ItemClock'
    pair_at: int
    paired_at: Union[None, int]
    rated: bool
    start_clocks_at: int
    scheduled_at: int
    variant: BulkPairingListResponse200ItemVariant = BulkPairingListResponse200ItemVariant.STANDARD
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_pairing_list_response_200_item_games_item import BulkPairingListResponse200ItemGamesItem
        from ..models.bulk_pairing_list_response_200_item_clock import BulkPairingListResponse200ItemClock
        id = self.id

        games = []
        for games_item_data in self.games:
            games_item = games_item_data.to_dict()
            games.append(games_item)



        variant = self.variant.value

        clock = self.clock.to_dict()

        pair_at = self.pair_at

        paired_at: Union[None, int]
        paired_at = self.paired_at

        rated = self.rated

        start_clocks_at = self.start_clocks_at

        scheduled_at = self.scheduled_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "games": games,
            "variant": variant,
            "clock": clock,
            "pairAt": pair_at,
            "pairedAt": paired_at,
            "rated": rated,
            "startClocksAt": start_clocks_at,
            "scheduledAt": scheduled_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_pairing_list_response_200_item_games_item import BulkPairingListResponse200ItemGamesItem
        from ..models.bulk_pairing_list_response_200_item_clock import BulkPairingListResponse200ItemClock
        d = dict(src_dict)
        id = d.pop("id")

        games = []
        _games = d.pop("games")
        for games_item_data in (_games):
            games_item = BulkPairingListResponse200ItemGamesItem.from_dict(games_item_data)



            games.append(games_item)


        variant = BulkPairingListResponse200ItemVariant(d.pop("variant"))




        clock = BulkPairingListResponse200ItemClock.from_dict(d.pop("clock"))




        pair_at = d.pop("pairAt")

        def _parse_paired_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        paired_at = _parse_paired_at(d.pop("pairedAt"))


        rated = d.pop("rated")

        start_clocks_at = d.pop("startClocksAt")

        scheduled_at = d.pop("scheduledAt")

        bulk_pairing_list_response_200_item = cls(
            id=id,
            games=games,
            variant=variant,
            clock=clock,
            pair_at=pair_at,
            paired_at=paired_at,
            rated=rated,
            start_clocks_at=start_clocks_at,
            scheduled_at=scheduled_at,
        )


        bulk_pairing_list_response_200_item.additional_properties = d
        return bulk_pairing_list_response_200_item

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
