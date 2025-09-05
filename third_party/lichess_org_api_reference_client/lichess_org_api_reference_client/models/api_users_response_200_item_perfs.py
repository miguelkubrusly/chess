from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_users_response_200_item_perfs_rapid import ApiUsersResponse200ItemPerfsRapid
  from ..models.api_users_response_200_item_perfs_storm import ApiUsersResponse200ItemPerfsStorm
  from ..models.api_users_response_200_item_perfs_puzzle import ApiUsersResponse200ItemPerfsPuzzle
  from ..models.api_users_response_200_item_perfs_atomic import ApiUsersResponse200ItemPerfsAtomic
  from ..models.api_users_response_200_item_perfs_racer import ApiUsersResponse200ItemPerfsRacer
  from ..models.api_users_response_200_item_perfs_ultra_bullet import ApiUsersResponse200ItemPerfsUltraBullet
  from ..models.api_users_response_200_item_perfs_king_of_the_hill import ApiUsersResponse200ItemPerfsKingOfTheHill
  from ..models.api_users_response_200_item_perfs_bullet import ApiUsersResponse200ItemPerfsBullet
  from ..models.api_users_response_200_item_perfs_correspondence import ApiUsersResponse200ItemPerfsCorrespondence
  from ..models.api_users_response_200_item_perfs_racing_kings import ApiUsersResponse200ItemPerfsRacingKings
  from ..models.api_users_response_200_item_perfs_classical import ApiUsersResponse200ItemPerfsClassical
  from ..models.api_users_response_200_item_perfs_blitz import ApiUsersResponse200ItemPerfsBlitz
  from ..models.api_users_response_200_item_perfs_crazyhouse import ApiUsersResponse200ItemPerfsCrazyhouse
  from ..models.api_users_response_200_item_perfs_antichess import ApiUsersResponse200ItemPerfsAntichess
  from ..models.api_users_response_200_item_perfs_horde import ApiUsersResponse200ItemPerfsHorde
  from ..models.api_users_response_200_item_perfs_streak import ApiUsersResponse200ItemPerfsStreak
  from ..models.api_users_response_200_item_perfs_three_check import ApiUsersResponse200ItemPerfsThreeCheck
  from ..models.api_users_response_200_item_perfs_chess_960 import ApiUsersResponse200ItemPerfsChess960





T = TypeVar("T", bound="ApiUsersResponse200ItemPerfs")



@_attrs_define
class ApiUsersResponse200ItemPerfs:
    """ 
        Attributes:
            chess960 (Union[Unset, ApiUsersResponse200ItemPerfsChess960]):
            atomic (Union[Unset, ApiUsersResponse200ItemPerfsAtomic]):
            racing_kings (Union[Unset, ApiUsersResponse200ItemPerfsRacingKings]):
            ultra_bullet (Union[Unset, ApiUsersResponse200ItemPerfsUltraBullet]):
            blitz (Union[Unset, ApiUsersResponse200ItemPerfsBlitz]):
            king_of_the_hill (Union[Unset, ApiUsersResponse200ItemPerfsKingOfTheHill]):
            three_check (Union[Unset, ApiUsersResponse200ItemPerfsThreeCheck]):
            antichess (Union[Unset, ApiUsersResponse200ItemPerfsAntichess]):
            crazyhouse (Union[Unset, ApiUsersResponse200ItemPerfsCrazyhouse]):
            bullet (Union[Unset, ApiUsersResponse200ItemPerfsBullet]):
            correspondence (Union[Unset, ApiUsersResponse200ItemPerfsCorrespondence]):
            horde (Union[Unset, ApiUsersResponse200ItemPerfsHorde]):
            puzzle (Union[Unset, ApiUsersResponse200ItemPerfsPuzzle]):
            classical (Union[Unset, ApiUsersResponse200ItemPerfsClassical]):
            rapid (Union[Unset, ApiUsersResponse200ItemPerfsRapid]):
            storm (Union[Unset, ApiUsersResponse200ItemPerfsStorm]):
            racer (Union[Unset, ApiUsersResponse200ItemPerfsRacer]):
            streak (Union[Unset, ApiUsersResponse200ItemPerfsStreak]):
     """

    chess960: Union[Unset, 'ApiUsersResponse200ItemPerfsChess960'] = UNSET
    atomic: Union[Unset, 'ApiUsersResponse200ItemPerfsAtomic'] = UNSET
    racing_kings: Union[Unset, 'ApiUsersResponse200ItemPerfsRacingKings'] = UNSET
    ultra_bullet: Union[Unset, 'ApiUsersResponse200ItemPerfsUltraBullet'] = UNSET
    blitz: Union[Unset, 'ApiUsersResponse200ItemPerfsBlitz'] = UNSET
    king_of_the_hill: Union[Unset, 'ApiUsersResponse200ItemPerfsKingOfTheHill'] = UNSET
    three_check: Union[Unset, 'ApiUsersResponse200ItemPerfsThreeCheck'] = UNSET
    antichess: Union[Unset, 'ApiUsersResponse200ItemPerfsAntichess'] = UNSET
    crazyhouse: Union[Unset, 'ApiUsersResponse200ItemPerfsCrazyhouse'] = UNSET
    bullet: Union[Unset, 'ApiUsersResponse200ItemPerfsBullet'] = UNSET
    correspondence: Union[Unset, 'ApiUsersResponse200ItemPerfsCorrespondence'] = UNSET
    horde: Union[Unset, 'ApiUsersResponse200ItemPerfsHorde'] = UNSET
    puzzle: Union[Unset, 'ApiUsersResponse200ItemPerfsPuzzle'] = UNSET
    classical: Union[Unset, 'ApiUsersResponse200ItemPerfsClassical'] = UNSET
    rapid: Union[Unset, 'ApiUsersResponse200ItemPerfsRapid'] = UNSET
    storm: Union[Unset, 'ApiUsersResponse200ItemPerfsStorm'] = UNSET
    racer: Union[Unset, 'ApiUsersResponse200ItemPerfsRacer'] = UNSET
    streak: Union[Unset, 'ApiUsersResponse200ItemPerfsStreak'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_users_response_200_item_perfs_rapid import ApiUsersResponse200ItemPerfsRapid
        from ..models.api_users_response_200_item_perfs_storm import ApiUsersResponse200ItemPerfsStorm
        from ..models.api_users_response_200_item_perfs_puzzle import ApiUsersResponse200ItemPerfsPuzzle
        from ..models.api_users_response_200_item_perfs_atomic import ApiUsersResponse200ItemPerfsAtomic
        from ..models.api_users_response_200_item_perfs_racer import ApiUsersResponse200ItemPerfsRacer
        from ..models.api_users_response_200_item_perfs_ultra_bullet import ApiUsersResponse200ItemPerfsUltraBullet
        from ..models.api_users_response_200_item_perfs_king_of_the_hill import ApiUsersResponse200ItemPerfsKingOfTheHill
        from ..models.api_users_response_200_item_perfs_bullet import ApiUsersResponse200ItemPerfsBullet
        from ..models.api_users_response_200_item_perfs_correspondence import ApiUsersResponse200ItemPerfsCorrespondence
        from ..models.api_users_response_200_item_perfs_racing_kings import ApiUsersResponse200ItemPerfsRacingKings
        from ..models.api_users_response_200_item_perfs_classical import ApiUsersResponse200ItemPerfsClassical
        from ..models.api_users_response_200_item_perfs_blitz import ApiUsersResponse200ItemPerfsBlitz
        from ..models.api_users_response_200_item_perfs_crazyhouse import ApiUsersResponse200ItemPerfsCrazyhouse
        from ..models.api_users_response_200_item_perfs_antichess import ApiUsersResponse200ItemPerfsAntichess
        from ..models.api_users_response_200_item_perfs_horde import ApiUsersResponse200ItemPerfsHorde
        from ..models.api_users_response_200_item_perfs_streak import ApiUsersResponse200ItemPerfsStreak
        from ..models.api_users_response_200_item_perfs_three_check import ApiUsersResponse200ItemPerfsThreeCheck
        from ..models.api_users_response_200_item_perfs_chess_960 import ApiUsersResponse200ItemPerfsChess960
        chess960: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chess960, Unset):
            chess960 = self.chess960.to_dict()

        atomic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.atomic, Unset):
            atomic = self.atomic.to_dict()

        racing_kings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.racing_kings, Unset):
            racing_kings = self.racing_kings.to_dict()

        ultra_bullet: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ultra_bullet, Unset):
            ultra_bullet = self.ultra_bullet.to_dict()

        blitz: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.blitz, Unset):
            blitz = self.blitz.to_dict()

        king_of_the_hill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.king_of_the_hill, Unset):
            king_of_the_hill = self.king_of_the_hill.to_dict()

        three_check: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.three_check, Unset):
            three_check = self.three_check.to_dict()

        antichess: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.antichess, Unset):
            antichess = self.antichess.to_dict()

        crazyhouse: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.crazyhouse, Unset):
            crazyhouse = self.crazyhouse.to_dict()

        bullet: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bullet, Unset):
            bullet = self.bullet.to_dict()

        correspondence: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.correspondence, Unset):
            correspondence = self.correspondence.to_dict()

        horde: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.horde, Unset):
            horde = self.horde.to_dict()

        puzzle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.puzzle, Unset):
            puzzle = self.puzzle.to_dict()

        classical: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.classical, Unset):
            classical = self.classical.to_dict()

        rapid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rapid, Unset):
            rapid = self.rapid.to_dict()

        storm: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.storm, Unset):
            storm = self.storm.to_dict()

        racer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.racer, Unset):
            racer = self.racer.to_dict()

        streak: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.streak, Unset):
            streak = self.streak.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chess960 is not UNSET:
            field_dict["chess960"] = chess960
        if atomic is not UNSET:
            field_dict["atomic"] = atomic
        if racing_kings is not UNSET:
            field_dict["racingKings"] = racing_kings
        if ultra_bullet is not UNSET:
            field_dict["ultraBullet"] = ultra_bullet
        if blitz is not UNSET:
            field_dict["blitz"] = blitz
        if king_of_the_hill is not UNSET:
            field_dict["kingOfTheHill"] = king_of_the_hill
        if three_check is not UNSET:
            field_dict["threeCheck"] = three_check
        if antichess is not UNSET:
            field_dict["antichess"] = antichess
        if crazyhouse is not UNSET:
            field_dict["crazyhouse"] = crazyhouse
        if bullet is not UNSET:
            field_dict["bullet"] = bullet
        if correspondence is not UNSET:
            field_dict["correspondence"] = correspondence
        if horde is not UNSET:
            field_dict["horde"] = horde
        if puzzle is not UNSET:
            field_dict["puzzle"] = puzzle
        if classical is not UNSET:
            field_dict["classical"] = classical
        if rapid is not UNSET:
            field_dict["rapid"] = rapid
        if storm is not UNSET:
            field_dict["storm"] = storm
        if racer is not UNSET:
            field_dict["racer"] = racer
        if streak is not UNSET:
            field_dict["streak"] = streak

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_users_response_200_item_perfs_rapid import ApiUsersResponse200ItemPerfsRapid
        from ..models.api_users_response_200_item_perfs_storm import ApiUsersResponse200ItemPerfsStorm
        from ..models.api_users_response_200_item_perfs_puzzle import ApiUsersResponse200ItemPerfsPuzzle
        from ..models.api_users_response_200_item_perfs_atomic import ApiUsersResponse200ItemPerfsAtomic
        from ..models.api_users_response_200_item_perfs_racer import ApiUsersResponse200ItemPerfsRacer
        from ..models.api_users_response_200_item_perfs_ultra_bullet import ApiUsersResponse200ItemPerfsUltraBullet
        from ..models.api_users_response_200_item_perfs_king_of_the_hill import ApiUsersResponse200ItemPerfsKingOfTheHill
        from ..models.api_users_response_200_item_perfs_bullet import ApiUsersResponse200ItemPerfsBullet
        from ..models.api_users_response_200_item_perfs_correspondence import ApiUsersResponse200ItemPerfsCorrespondence
        from ..models.api_users_response_200_item_perfs_racing_kings import ApiUsersResponse200ItemPerfsRacingKings
        from ..models.api_users_response_200_item_perfs_classical import ApiUsersResponse200ItemPerfsClassical
        from ..models.api_users_response_200_item_perfs_blitz import ApiUsersResponse200ItemPerfsBlitz
        from ..models.api_users_response_200_item_perfs_crazyhouse import ApiUsersResponse200ItemPerfsCrazyhouse
        from ..models.api_users_response_200_item_perfs_antichess import ApiUsersResponse200ItemPerfsAntichess
        from ..models.api_users_response_200_item_perfs_horde import ApiUsersResponse200ItemPerfsHorde
        from ..models.api_users_response_200_item_perfs_streak import ApiUsersResponse200ItemPerfsStreak
        from ..models.api_users_response_200_item_perfs_three_check import ApiUsersResponse200ItemPerfsThreeCheck
        from ..models.api_users_response_200_item_perfs_chess_960 import ApiUsersResponse200ItemPerfsChess960
        d = dict(src_dict)
        _chess960 = d.pop("chess960", UNSET)
        chess960: Union[Unset, ApiUsersResponse200ItemPerfsChess960]
        if isinstance(_chess960,  Unset):
            chess960 = UNSET
        else:
            chess960 = ApiUsersResponse200ItemPerfsChess960.from_dict(_chess960)




        _atomic = d.pop("atomic", UNSET)
        atomic: Union[Unset, ApiUsersResponse200ItemPerfsAtomic]
        if isinstance(_atomic,  Unset):
            atomic = UNSET
        else:
            atomic = ApiUsersResponse200ItemPerfsAtomic.from_dict(_atomic)




        _racing_kings = d.pop("racingKings", UNSET)
        racing_kings: Union[Unset, ApiUsersResponse200ItemPerfsRacingKings]
        if isinstance(_racing_kings,  Unset):
            racing_kings = UNSET
        else:
            racing_kings = ApiUsersResponse200ItemPerfsRacingKings.from_dict(_racing_kings)




        _ultra_bullet = d.pop("ultraBullet", UNSET)
        ultra_bullet: Union[Unset, ApiUsersResponse200ItemPerfsUltraBullet]
        if isinstance(_ultra_bullet,  Unset):
            ultra_bullet = UNSET
        else:
            ultra_bullet = ApiUsersResponse200ItemPerfsUltraBullet.from_dict(_ultra_bullet)




        _blitz = d.pop("blitz", UNSET)
        blitz: Union[Unset, ApiUsersResponse200ItemPerfsBlitz]
        if isinstance(_blitz,  Unset):
            blitz = UNSET
        else:
            blitz = ApiUsersResponse200ItemPerfsBlitz.from_dict(_blitz)




        _king_of_the_hill = d.pop("kingOfTheHill", UNSET)
        king_of_the_hill: Union[Unset, ApiUsersResponse200ItemPerfsKingOfTheHill]
        if isinstance(_king_of_the_hill,  Unset):
            king_of_the_hill = UNSET
        else:
            king_of_the_hill = ApiUsersResponse200ItemPerfsKingOfTheHill.from_dict(_king_of_the_hill)




        _three_check = d.pop("threeCheck", UNSET)
        three_check: Union[Unset, ApiUsersResponse200ItemPerfsThreeCheck]
        if isinstance(_three_check,  Unset):
            three_check = UNSET
        else:
            three_check = ApiUsersResponse200ItemPerfsThreeCheck.from_dict(_three_check)




        _antichess = d.pop("antichess", UNSET)
        antichess: Union[Unset, ApiUsersResponse200ItemPerfsAntichess]
        if isinstance(_antichess,  Unset):
            antichess = UNSET
        else:
            antichess = ApiUsersResponse200ItemPerfsAntichess.from_dict(_antichess)




        _crazyhouse = d.pop("crazyhouse", UNSET)
        crazyhouse: Union[Unset, ApiUsersResponse200ItemPerfsCrazyhouse]
        if isinstance(_crazyhouse,  Unset):
            crazyhouse = UNSET
        else:
            crazyhouse = ApiUsersResponse200ItemPerfsCrazyhouse.from_dict(_crazyhouse)




        _bullet = d.pop("bullet", UNSET)
        bullet: Union[Unset, ApiUsersResponse200ItemPerfsBullet]
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = ApiUsersResponse200ItemPerfsBullet.from_dict(_bullet)




        _correspondence = d.pop("correspondence", UNSET)
        correspondence: Union[Unset, ApiUsersResponse200ItemPerfsCorrespondence]
        if isinstance(_correspondence,  Unset):
            correspondence = UNSET
        else:
            correspondence = ApiUsersResponse200ItemPerfsCorrespondence.from_dict(_correspondence)




        _horde = d.pop("horde", UNSET)
        horde: Union[Unset, ApiUsersResponse200ItemPerfsHorde]
        if isinstance(_horde,  Unset):
            horde = UNSET
        else:
            horde = ApiUsersResponse200ItemPerfsHorde.from_dict(_horde)




        _puzzle = d.pop("puzzle", UNSET)
        puzzle: Union[Unset, ApiUsersResponse200ItemPerfsPuzzle]
        if isinstance(_puzzle,  Unset):
            puzzle = UNSET
        else:
            puzzle = ApiUsersResponse200ItemPerfsPuzzle.from_dict(_puzzle)




        _classical = d.pop("classical", UNSET)
        classical: Union[Unset, ApiUsersResponse200ItemPerfsClassical]
        if isinstance(_classical,  Unset):
            classical = UNSET
        else:
            classical = ApiUsersResponse200ItemPerfsClassical.from_dict(_classical)




        _rapid = d.pop("rapid", UNSET)
        rapid: Union[Unset, ApiUsersResponse200ItemPerfsRapid]
        if isinstance(_rapid,  Unset):
            rapid = UNSET
        else:
            rapid = ApiUsersResponse200ItemPerfsRapid.from_dict(_rapid)




        _storm = d.pop("storm", UNSET)
        storm: Union[Unset, ApiUsersResponse200ItemPerfsStorm]
        if isinstance(_storm,  Unset):
            storm = UNSET
        else:
            storm = ApiUsersResponse200ItemPerfsStorm.from_dict(_storm)




        _racer = d.pop("racer", UNSET)
        racer: Union[Unset, ApiUsersResponse200ItemPerfsRacer]
        if isinstance(_racer,  Unset):
            racer = UNSET
        else:
            racer = ApiUsersResponse200ItemPerfsRacer.from_dict(_racer)




        _streak = d.pop("streak", UNSET)
        streak: Union[Unset, ApiUsersResponse200ItemPerfsStreak]
        if isinstance(_streak,  Unset):
            streak = UNSET
        else:
            streak = ApiUsersResponse200ItemPerfsStreak.from_dict(_streak)




        api_users_response_200_item_perfs = cls(
            chess960=chess960,
            atomic=atomic,
            racing_kings=racing_kings,
            ultra_bullet=ultra_bullet,
            blitz=blitz,
            king_of_the_hill=king_of_the_hill,
            three_check=three_check,
            antichess=antichess,
            crazyhouse=crazyhouse,
            bullet=bullet,
            correspondence=correspondence,
            horde=horde,
            puzzle=puzzle,
            classical=classical,
            rapid=rapid,
            storm=storm,
            racer=racer,
            streak=streak,
        )


        api_users_response_200_item_perfs.additional_properties = d
        return api_users_response_200_item_perfs

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
