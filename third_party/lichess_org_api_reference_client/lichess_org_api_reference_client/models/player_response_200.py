from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.player_response_200_crazyhouse_item import PlayerResponse200CrazyhouseItem
  from ..models.player_response_200_rapid_item import PlayerResponse200RapidItem
  from ..models.player_response_200_horde_item import PlayerResponse200HordeItem
  from ..models.player_response_200_racing_kings_item import PlayerResponse200RacingKingsItem
  from ..models.player_response_200_classical_item import PlayerResponse200ClassicalItem
  from ..models.player_response_200_atomic_item import PlayerResponse200AtomicItem
  from ..models.player_response_200_ultra_bullet_item import PlayerResponse200UltraBulletItem
  from ..models.player_response_200_three_check_item import PlayerResponse200ThreeCheckItem
  from ..models.player_response_200_king_of_the_hill_item import PlayerResponse200KingOfTheHillItem
  from ..models.player_response_200_blitz_item import PlayerResponse200BlitzItem
  from ..models.player_response_200_chess_960_item import PlayerResponse200Chess960Item
  from ..models.player_response_200_bullet_item import PlayerResponse200BulletItem
  from ..models.player_response_200_antichess_item import PlayerResponse200AntichessItem





T = TypeVar("T", bound="PlayerResponse200")



@_attrs_define
class PlayerResponse200:
    """ 
        Attributes:
            bullet (list['PlayerResponse200BulletItem']):
            blitz (list['PlayerResponse200BlitzItem']):
            rapid (list['PlayerResponse200RapidItem']):
            classical (list['PlayerResponse200ClassicalItem']):
            ultra_bullet (list['PlayerResponse200UltraBulletItem']):
            crazyhouse (list['PlayerResponse200CrazyhouseItem']):
            chess960 (list['PlayerResponse200Chess960Item']):
            king_of_the_hill (list['PlayerResponse200KingOfTheHillItem']):
            three_check (list['PlayerResponse200ThreeCheckItem']):
            antichess (list['PlayerResponse200AntichessItem']):
            atomic (list['PlayerResponse200AtomicItem']):
            horde (list['PlayerResponse200HordeItem']):
            racing_kings (list['PlayerResponse200RacingKingsItem']):
     """

    bullet: list['PlayerResponse200BulletItem']
    blitz: list['PlayerResponse200BlitzItem']
    rapid: list['PlayerResponse200RapidItem']
    classical: list['PlayerResponse200ClassicalItem']
    ultra_bullet: list['PlayerResponse200UltraBulletItem']
    crazyhouse: list['PlayerResponse200CrazyhouseItem']
    chess960: list['PlayerResponse200Chess960Item']
    king_of_the_hill: list['PlayerResponse200KingOfTheHillItem']
    three_check: list['PlayerResponse200ThreeCheckItem']
    antichess: list['PlayerResponse200AntichessItem']
    atomic: list['PlayerResponse200AtomicItem']
    horde: list['PlayerResponse200HordeItem']
    racing_kings: list['PlayerResponse200RacingKingsItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.player_response_200_crazyhouse_item import PlayerResponse200CrazyhouseItem
        from ..models.player_response_200_rapid_item import PlayerResponse200RapidItem
        from ..models.player_response_200_horde_item import PlayerResponse200HordeItem
        from ..models.player_response_200_racing_kings_item import PlayerResponse200RacingKingsItem
        from ..models.player_response_200_classical_item import PlayerResponse200ClassicalItem
        from ..models.player_response_200_atomic_item import PlayerResponse200AtomicItem
        from ..models.player_response_200_ultra_bullet_item import PlayerResponse200UltraBulletItem
        from ..models.player_response_200_three_check_item import PlayerResponse200ThreeCheckItem
        from ..models.player_response_200_king_of_the_hill_item import PlayerResponse200KingOfTheHillItem
        from ..models.player_response_200_blitz_item import PlayerResponse200BlitzItem
        from ..models.player_response_200_chess_960_item import PlayerResponse200Chess960Item
        from ..models.player_response_200_bullet_item import PlayerResponse200BulletItem
        from ..models.player_response_200_antichess_item import PlayerResponse200AntichessItem
        bullet = []
        for bullet_item_data in self.bullet:
            bullet_item = bullet_item_data.to_dict()
            bullet.append(bullet_item)



        blitz = []
        for blitz_item_data in self.blitz:
            blitz_item = blitz_item_data.to_dict()
            blitz.append(blitz_item)



        rapid = []
        for rapid_item_data in self.rapid:
            rapid_item = rapid_item_data.to_dict()
            rapid.append(rapid_item)



        classical = []
        for classical_item_data in self.classical:
            classical_item = classical_item_data.to_dict()
            classical.append(classical_item)



        ultra_bullet = []
        for ultra_bullet_item_data in self.ultra_bullet:
            ultra_bullet_item = ultra_bullet_item_data.to_dict()
            ultra_bullet.append(ultra_bullet_item)



        crazyhouse = []
        for crazyhouse_item_data in self.crazyhouse:
            crazyhouse_item = crazyhouse_item_data.to_dict()
            crazyhouse.append(crazyhouse_item)



        chess960 = []
        for chess960_item_data in self.chess960:
            chess960_item = chess960_item_data.to_dict()
            chess960.append(chess960_item)



        king_of_the_hill = []
        for king_of_the_hill_item_data in self.king_of_the_hill:
            king_of_the_hill_item = king_of_the_hill_item_data.to_dict()
            king_of_the_hill.append(king_of_the_hill_item)



        three_check = []
        for three_check_item_data in self.three_check:
            three_check_item = three_check_item_data.to_dict()
            three_check.append(three_check_item)



        antichess = []
        for antichess_item_data in self.antichess:
            antichess_item = antichess_item_data.to_dict()
            antichess.append(antichess_item)



        atomic = []
        for atomic_item_data in self.atomic:
            atomic_item = atomic_item_data.to_dict()
            atomic.append(atomic_item)



        horde = []
        for horde_item_data in self.horde:
            horde_item = horde_item_data.to_dict()
            horde.append(horde_item)



        racing_kings = []
        for racing_kings_item_data in self.racing_kings:
            racing_kings_item = racing_kings_item_data.to_dict()
            racing_kings.append(racing_kings_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "bullet": bullet,
            "blitz": blitz,
            "rapid": rapid,
            "classical": classical,
            "ultraBullet": ultra_bullet,
            "crazyhouse": crazyhouse,
            "chess960": chess960,
            "kingOfTheHill": king_of_the_hill,
            "threeCheck": three_check,
            "antichess": antichess,
            "atomic": atomic,
            "horde": horde,
            "racingKings": racing_kings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.player_response_200_crazyhouse_item import PlayerResponse200CrazyhouseItem
        from ..models.player_response_200_rapid_item import PlayerResponse200RapidItem
        from ..models.player_response_200_horde_item import PlayerResponse200HordeItem
        from ..models.player_response_200_racing_kings_item import PlayerResponse200RacingKingsItem
        from ..models.player_response_200_classical_item import PlayerResponse200ClassicalItem
        from ..models.player_response_200_atomic_item import PlayerResponse200AtomicItem
        from ..models.player_response_200_ultra_bullet_item import PlayerResponse200UltraBulletItem
        from ..models.player_response_200_three_check_item import PlayerResponse200ThreeCheckItem
        from ..models.player_response_200_king_of_the_hill_item import PlayerResponse200KingOfTheHillItem
        from ..models.player_response_200_blitz_item import PlayerResponse200BlitzItem
        from ..models.player_response_200_chess_960_item import PlayerResponse200Chess960Item
        from ..models.player_response_200_bullet_item import PlayerResponse200BulletItem
        from ..models.player_response_200_antichess_item import PlayerResponse200AntichessItem
        d = dict(src_dict)
        bullet = []
        _bullet = d.pop("bullet")
        for bullet_item_data in (_bullet):
            bullet_item = PlayerResponse200BulletItem.from_dict(bullet_item_data)



            bullet.append(bullet_item)


        blitz = []
        _blitz = d.pop("blitz")
        for blitz_item_data in (_blitz):
            blitz_item = PlayerResponse200BlitzItem.from_dict(blitz_item_data)



            blitz.append(blitz_item)


        rapid = []
        _rapid = d.pop("rapid")
        for rapid_item_data in (_rapid):
            rapid_item = PlayerResponse200RapidItem.from_dict(rapid_item_data)



            rapid.append(rapid_item)


        classical = []
        _classical = d.pop("classical")
        for classical_item_data in (_classical):
            classical_item = PlayerResponse200ClassicalItem.from_dict(classical_item_data)



            classical.append(classical_item)


        ultra_bullet = []
        _ultra_bullet = d.pop("ultraBullet")
        for ultra_bullet_item_data in (_ultra_bullet):
            ultra_bullet_item = PlayerResponse200UltraBulletItem.from_dict(ultra_bullet_item_data)



            ultra_bullet.append(ultra_bullet_item)


        crazyhouse = []
        _crazyhouse = d.pop("crazyhouse")
        for crazyhouse_item_data in (_crazyhouse):
            crazyhouse_item = PlayerResponse200CrazyhouseItem.from_dict(crazyhouse_item_data)



            crazyhouse.append(crazyhouse_item)


        chess960 = []
        _chess960 = d.pop("chess960")
        for chess960_item_data in (_chess960):
            chess960_item = PlayerResponse200Chess960Item.from_dict(chess960_item_data)



            chess960.append(chess960_item)


        king_of_the_hill = []
        _king_of_the_hill = d.pop("kingOfTheHill")
        for king_of_the_hill_item_data in (_king_of_the_hill):
            king_of_the_hill_item = PlayerResponse200KingOfTheHillItem.from_dict(king_of_the_hill_item_data)



            king_of_the_hill.append(king_of_the_hill_item)


        three_check = []
        _three_check = d.pop("threeCheck")
        for three_check_item_data in (_three_check):
            three_check_item = PlayerResponse200ThreeCheckItem.from_dict(three_check_item_data)



            three_check.append(three_check_item)


        antichess = []
        _antichess = d.pop("antichess")
        for antichess_item_data in (_antichess):
            antichess_item = PlayerResponse200AntichessItem.from_dict(antichess_item_data)



            antichess.append(antichess_item)


        atomic = []
        _atomic = d.pop("atomic")
        for atomic_item_data in (_atomic):
            atomic_item = PlayerResponse200AtomicItem.from_dict(atomic_item_data)



            atomic.append(atomic_item)


        horde = []
        _horde = d.pop("horde")
        for horde_item_data in (_horde):
            horde_item = PlayerResponse200HordeItem.from_dict(horde_item_data)



            horde.append(horde_item)


        racing_kings = []
        _racing_kings = d.pop("racingKings")
        for racing_kings_item_data in (_racing_kings):
            racing_kings_item = PlayerResponse200RacingKingsItem.from_dict(racing_kings_item_data)



            racing_kings.append(racing_kings_item)


        player_response_200 = cls(
            bullet=bullet,
            blitz=blitz,
            rapid=rapid,
            classical=classical,
            ultra_bullet=ultra_bullet,
            crazyhouse=crazyhouse,
            chess960=chess960,
            king_of_the_hill=king_of_the_hill,
            three_check=three_check,
            antichess=antichess,
            atomic=atomic,
            horde=horde,
            racing_kings=racing_kings,
        )


        player_response_200.additional_properties = d
        return player_response_200

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
