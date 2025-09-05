from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_user_response_200_perfs_rapid import ApiUserResponse200PerfsRapid
  from ..models.api_user_response_200_perfs_antichess import ApiUserResponse200PerfsAntichess
  from ..models.api_user_response_200_perfs_bullet import ApiUserResponse200PerfsBullet
  from ..models.api_user_response_200_perfs_racing_kings import ApiUserResponse200PerfsRacingKings
  from ..models.api_user_response_200_perfs_chess_960 import ApiUserResponse200PerfsChess960
  from ..models.api_user_response_200_perfs_three_check import ApiUserResponse200PerfsThreeCheck
  from ..models.api_user_response_200_perfs_storm import ApiUserResponse200PerfsStorm
  from ..models.api_user_response_200_perfs_ultra_bullet import ApiUserResponse200PerfsUltraBullet
  from ..models.api_user_response_200_perfs_classical import ApiUserResponse200PerfsClassical
  from ..models.api_user_response_200_perfs_racer import ApiUserResponse200PerfsRacer
  from ..models.api_user_response_200_perfs_streak import ApiUserResponse200PerfsStreak
  from ..models.api_user_response_200_perfs_king_of_the_hill import ApiUserResponse200PerfsKingOfTheHill
  from ..models.api_user_response_200_perfs_blitz import ApiUserResponse200PerfsBlitz
  from ..models.api_user_response_200_perfs_puzzle import ApiUserResponse200PerfsPuzzle
  from ..models.api_user_response_200_perfs_crazyhouse import ApiUserResponse200PerfsCrazyhouse
  from ..models.api_user_response_200_perfs_atomic import ApiUserResponse200PerfsAtomic
  from ..models.api_user_response_200_perfs_correspondence import ApiUserResponse200PerfsCorrespondence
  from ..models.api_user_response_200_perfs_horde import ApiUserResponse200PerfsHorde





T = TypeVar("T", bound="ApiUserResponse200Perfs")



@_attrs_define
class ApiUserResponse200Perfs:
    """ 
        Attributes:
            chess960 (Union[Unset, ApiUserResponse200PerfsChess960]):
            atomic (Union[Unset, ApiUserResponse200PerfsAtomic]):
            racing_kings (Union[Unset, ApiUserResponse200PerfsRacingKings]):
            ultra_bullet (Union[Unset, ApiUserResponse200PerfsUltraBullet]):
            blitz (Union[Unset, ApiUserResponse200PerfsBlitz]):
            king_of_the_hill (Union[Unset, ApiUserResponse200PerfsKingOfTheHill]):
            three_check (Union[Unset, ApiUserResponse200PerfsThreeCheck]):
            antichess (Union[Unset, ApiUserResponse200PerfsAntichess]):
            crazyhouse (Union[Unset, ApiUserResponse200PerfsCrazyhouse]):
            bullet (Union[Unset, ApiUserResponse200PerfsBullet]):
            correspondence (Union[Unset, ApiUserResponse200PerfsCorrespondence]):
            horde (Union[Unset, ApiUserResponse200PerfsHorde]):
            puzzle (Union[Unset, ApiUserResponse200PerfsPuzzle]):
            classical (Union[Unset, ApiUserResponse200PerfsClassical]):
            rapid (Union[Unset, ApiUserResponse200PerfsRapid]):
            storm (Union[Unset, ApiUserResponse200PerfsStorm]):
            racer (Union[Unset, ApiUserResponse200PerfsRacer]):
            streak (Union[Unset, ApiUserResponse200PerfsStreak]):
     """

    chess960: Union[Unset, 'ApiUserResponse200PerfsChess960'] = UNSET
    atomic: Union[Unset, 'ApiUserResponse200PerfsAtomic'] = UNSET
    racing_kings: Union[Unset, 'ApiUserResponse200PerfsRacingKings'] = UNSET
    ultra_bullet: Union[Unset, 'ApiUserResponse200PerfsUltraBullet'] = UNSET
    blitz: Union[Unset, 'ApiUserResponse200PerfsBlitz'] = UNSET
    king_of_the_hill: Union[Unset, 'ApiUserResponse200PerfsKingOfTheHill'] = UNSET
    three_check: Union[Unset, 'ApiUserResponse200PerfsThreeCheck'] = UNSET
    antichess: Union[Unset, 'ApiUserResponse200PerfsAntichess'] = UNSET
    crazyhouse: Union[Unset, 'ApiUserResponse200PerfsCrazyhouse'] = UNSET
    bullet: Union[Unset, 'ApiUserResponse200PerfsBullet'] = UNSET
    correspondence: Union[Unset, 'ApiUserResponse200PerfsCorrespondence'] = UNSET
    horde: Union[Unset, 'ApiUserResponse200PerfsHorde'] = UNSET
    puzzle: Union[Unset, 'ApiUserResponse200PerfsPuzzle'] = UNSET
    classical: Union[Unset, 'ApiUserResponse200PerfsClassical'] = UNSET
    rapid: Union[Unset, 'ApiUserResponse200PerfsRapid'] = UNSET
    storm: Union[Unset, 'ApiUserResponse200PerfsStorm'] = UNSET
    racer: Union[Unset, 'ApiUserResponse200PerfsRacer'] = UNSET
    streak: Union[Unset, 'ApiUserResponse200PerfsStreak'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_response_200_perfs_rapid import ApiUserResponse200PerfsRapid
        from ..models.api_user_response_200_perfs_antichess import ApiUserResponse200PerfsAntichess
        from ..models.api_user_response_200_perfs_bullet import ApiUserResponse200PerfsBullet
        from ..models.api_user_response_200_perfs_racing_kings import ApiUserResponse200PerfsRacingKings
        from ..models.api_user_response_200_perfs_chess_960 import ApiUserResponse200PerfsChess960
        from ..models.api_user_response_200_perfs_three_check import ApiUserResponse200PerfsThreeCheck
        from ..models.api_user_response_200_perfs_storm import ApiUserResponse200PerfsStorm
        from ..models.api_user_response_200_perfs_ultra_bullet import ApiUserResponse200PerfsUltraBullet
        from ..models.api_user_response_200_perfs_classical import ApiUserResponse200PerfsClassical
        from ..models.api_user_response_200_perfs_racer import ApiUserResponse200PerfsRacer
        from ..models.api_user_response_200_perfs_streak import ApiUserResponse200PerfsStreak
        from ..models.api_user_response_200_perfs_king_of_the_hill import ApiUserResponse200PerfsKingOfTheHill
        from ..models.api_user_response_200_perfs_blitz import ApiUserResponse200PerfsBlitz
        from ..models.api_user_response_200_perfs_puzzle import ApiUserResponse200PerfsPuzzle
        from ..models.api_user_response_200_perfs_crazyhouse import ApiUserResponse200PerfsCrazyhouse
        from ..models.api_user_response_200_perfs_atomic import ApiUserResponse200PerfsAtomic
        from ..models.api_user_response_200_perfs_correspondence import ApiUserResponse200PerfsCorrespondence
        from ..models.api_user_response_200_perfs_horde import ApiUserResponse200PerfsHorde
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
        from ..models.api_user_response_200_perfs_rapid import ApiUserResponse200PerfsRapid
        from ..models.api_user_response_200_perfs_antichess import ApiUserResponse200PerfsAntichess
        from ..models.api_user_response_200_perfs_bullet import ApiUserResponse200PerfsBullet
        from ..models.api_user_response_200_perfs_racing_kings import ApiUserResponse200PerfsRacingKings
        from ..models.api_user_response_200_perfs_chess_960 import ApiUserResponse200PerfsChess960
        from ..models.api_user_response_200_perfs_three_check import ApiUserResponse200PerfsThreeCheck
        from ..models.api_user_response_200_perfs_storm import ApiUserResponse200PerfsStorm
        from ..models.api_user_response_200_perfs_ultra_bullet import ApiUserResponse200PerfsUltraBullet
        from ..models.api_user_response_200_perfs_classical import ApiUserResponse200PerfsClassical
        from ..models.api_user_response_200_perfs_racer import ApiUserResponse200PerfsRacer
        from ..models.api_user_response_200_perfs_streak import ApiUserResponse200PerfsStreak
        from ..models.api_user_response_200_perfs_king_of_the_hill import ApiUserResponse200PerfsKingOfTheHill
        from ..models.api_user_response_200_perfs_blitz import ApiUserResponse200PerfsBlitz
        from ..models.api_user_response_200_perfs_puzzle import ApiUserResponse200PerfsPuzzle
        from ..models.api_user_response_200_perfs_crazyhouse import ApiUserResponse200PerfsCrazyhouse
        from ..models.api_user_response_200_perfs_atomic import ApiUserResponse200PerfsAtomic
        from ..models.api_user_response_200_perfs_correspondence import ApiUserResponse200PerfsCorrespondence
        from ..models.api_user_response_200_perfs_horde import ApiUserResponse200PerfsHorde
        d = dict(src_dict)
        _chess960 = d.pop("chess960", UNSET)
        chess960: Union[Unset, ApiUserResponse200PerfsChess960]
        if isinstance(_chess960,  Unset):
            chess960 = UNSET
        else:
            chess960 = ApiUserResponse200PerfsChess960.from_dict(_chess960)




        _atomic = d.pop("atomic", UNSET)
        atomic: Union[Unset, ApiUserResponse200PerfsAtomic]
        if isinstance(_atomic,  Unset):
            atomic = UNSET
        else:
            atomic = ApiUserResponse200PerfsAtomic.from_dict(_atomic)




        _racing_kings = d.pop("racingKings", UNSET)
        racing_kings: Union[Unset, ApiUserResponse200PerfsRacingKings]
        if isinstance(_racing_kings,  Unset):
            racing_kings = UNSET
        else:
            racing_kings = ApiUserResponse200PerfsRacingKings.from_dict(_racing_kings)




        _ultra_bullet = d.pop("ultraBullet", UNSET)
        ultra_bullet: Union[Unset, ApiUserResponse200PerfsUltraBullet]
        if isinstance(_ultra_bullet,  Unset):
            ultra_bullet = UNSET
        else:
            ultra_bullet = ApiUserResponse200PerfsUltraBullet.from_dict(_ultra_bullet)




        _blitz = d.pop("blitz", UNSET)
        blitz: Union[Unset, ApiUserResponse200PerfsBlitz]
        if isinstance(_blitz,  Unset):
            blitz = UNSET
        else:
            blitz = ApiUserResponse200PerfsBlitz.from_dict(_blitz)




        _king_of_the_hill = d.pop("kingOfTheHill", UNSET)
        king_of_the_hill: Union[Unset, ApiUserResponse200PerfsKingOfTheHill]
        if isinstance(_king_of_the_hill,  Unset):
            king_of_the_hill = UNSET
        else:
            king_of_the_hill = ApiUserResponse200PerfsKingOfTheHill.from_dict(_king_of_the_hill)




        _three_check = d.pop("threeCheck", UNSET)
        three_check: Union[Unset, ApiUserResponse200PerfsThreeCheck]
        if isinstance(_three_check,  Unset):
            three_check = UNSET
        else:
            three_check = ApiUserResponse200PerfsThreeCheck.from_dict(_three_check)




        _antichess = d.pop("antichess", UNSET)
        antichess: Union[Unset, ApiUserResponse200PerfsAntichess]
        if isinstance(_antichess,  Unset):
            antichess = UNSET
        else:
            antichess = ApiUserResponse200PerfsAntichess.from_dict(_antichess)




        _crazyhouse = d.pop("crazyhouse", UNSET)
        crazyhouse: Union[Unset, ApiUserResponse200PerfsCrazyhouse]
        if isinstance(_crazyhouse,  Unset):
            crazyhouse = UNSET
        else:
            crazyhouse = ApiUserResponse200PerfsCrazyhouse.from_dict(_crazyhouse)




        _bullet = d.pop("bullet", UNSET)
        bullet: Union[Unset, ApiUserResponse200PerfsBullet]
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = ApiUserResponse200PerfsBullet.from_dict(_bullet)




        _correspondence = d.pop("correspondence", UNSET)
        correspondence: Union[Unset, ApiUserResponse200PerfsCorrespondence]
        if isinstance(_correspondence,  Unset):
            correspondence = UNSET
        else:
            correspondence = ApiUserResponse200PerfsCorrespondence.from_dict(_correspondence)




        _horde = d.pop("horde", UNSET)
        horde: Union[Unset, ApiUserResponse200PerfsHorde]
        if isinstance(_horde,  Unset):
            horde = UNSET
        else:
            horde = ApiUserResponse200PerfsHorde.from_dict(_horde)




        _puzzle = d.pop("puzzle", UNSET)
        puzzle: Union[Unset, ApiUserResponse200PerfsPuzzle]
        if isinstance(_puzzle,  Unset):
            puzzle = UNSET
        else:
            puzzle = ApiUserResponse200PerfsPuzzle.from_dict(_puzzle)




        _classical = d.pop("classical", UNSET)
        classical: Union[Unset, ApiUserResponse200PerfsClassical]
        if isinstance(_classical,  Unset):
            classical = UNSET
        else:
            classical = ApiUserResponse200PerfsClassical.from_dict(_classical)




        _rapid = d.pop("rapid", UNSET)
        rapid: Union[Unset, ApiUserResponse200PerfsRapid]
        if isinstance(_rapid,  Unset):
            rapid = UNSET
        else:
            rapid = ApiUserResponse200PerfsRapid.from_dict(_rapid)




        _storm = d.pop("storm", UNSET)
        storm: Union[Unset, ApiUserResponse200PerfsStorm]
        if isinstance(_storm,  Unset):
            storm = UNSET
        else:
            storm = ApiUserResponse200PerfsStorm.from_dict(_storm)




        _racer = d.pop("racer", UNSET)
        racer: Union[Unset, ApiUserResponse200PerfsRacer]
        if isinstance(_racer,  Unset):
            racer = UNSET
        else:
            racer = ApiUserResponse200PerfsRacer.from_dict(_racer)




        _streak = d.pop("streak", UNSET)
        streak: Union[Unset, ApiUserResponse200PerfsStreak]
        if isinstance(_streak,  Unset):
            streak = UNSET
        else:
            streak = ApiUserResponse200PerfsStreak.from_dict(_streak)




        api_user_response_200_perfs = cls(
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


        api_user_response_200_perfs.additional_properties = d
        return api_user_response_200_perfs

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
