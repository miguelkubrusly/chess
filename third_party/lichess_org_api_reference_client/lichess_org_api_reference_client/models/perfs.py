from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.perfs_ultra_bullet import PerfsUltraBullet
  from ..models.perfs_blitz import PerfsBlitz
  from ..models.perfs_rapid import PerfsRapid
  from ..models.perfs_antichess import PerfsAntichess
  from ..models.perfs_racer import PerfsRacer
  from ..models.perfs_racing_kings import PerfsRacingKings
  from ..models.perfs_chess_960 import PerfsChess960
  from ..models.perfs_three_check import PerfsThreeCheck
  from ..models.perfs_streak import PerfsStreak
  from ..models.perfs_storm import PerfsStorm
  from ..models.perfs_classical import PerfsClassical
  from ..models.perfs_bullet import PerfsBullet
  from ..models.perfs_horde import PerfsHorde
  from ..models.perfs_king_of_the_hill import PerfsKingOfTheHill
  from ..models.perfs_puzzle import PerfsPuzzle
  from ..models.perfs_crazyhouse import PerfsCrazyhouse
  from ..models.perfs_correspondence import PerfsCorrespondence
  from ..models.perfs_atomic import PerfsAtomic





T = TypeVar("T", bound="Perfs")



@_attrs_define
class Perfs:
    """ 
        Attributes:
            chess960 (Union[Unset, PerfsChess960]):
            atomic (Union[Unset, PerfsAtomic]):
            racing_kings (Union[Unset, PerfsRacingKings]):
            ultra_bullet (Union[Unset, PerfsUltraBullet]):
            blitz (Union[Unset, PerfsBlitz]):
            king_of_the_hill (Union[Unset, PerfsKingOfTheHill]):
            three_check (Union[Unset, PerfsThreeCheck]):
            antichess (Union[Unset, PerfsAntichess]):
            crazyhouse (Union[Unset, PerfsCrazyhouse]):
            bullet (Union[Unset, PerfsBullet]):
            correspondence (Union[Unset, PerfsCorrespondence]):
            horde (Union[Unset, PerfsHorde]):
            puzzle (Union[Unset, PerfsPuzzle]):
            classical (Union[Unset, PerfsClassical]):
            rapid (Union[Unset, PerfsRapid]):
            storm (Union[Unset, PerfsStorm]):
            racer (Union[Unset, PerfsRacer]):
            streak (Union[Unset, PerfsStreak]):
     """

    chess960: Union[Unset, 'PerfsChess960'] = UNSET
    atomic: Union[Unset, 'PerfsAtomic'] = UNSET
    racing_kings: Union[Unset, 'PerfsRacingKings'] = UNSET
    ultra_bullet: Union[Unset, 'PerfsUltraBullet'] = UNSET
    blitz: Union[Unset, 'PerfsBlitz'] = UNSET
    king_of_the_hill: Union[Unset, 'PerfsKingOfTheHill'] = UNSET
    three_check: Union[Unset, 'PerfsThreeCheck'] = UNSET
    antichess: Union[Unset, 'PerfsAntichess'] = UNSET
    crazyhouse: Union[Unset, 'PerfsCrazyhouse'] = UNSET
    bullet: Union[Unset, 'PerfsBullet'] = UNSET
    correspondence: Union[Unset, 'PerfsCorrespondence'] = UNSET
    horde: Union[Unset, 'PerfsHorde'] = UNSET
    puzzle: Union[Unset, 'PerfsPuzzle'] = UNSET
    classical: Union[Unset, 'PerfsClassical'] = UNSET
    rapid: Union[Unset, 'PerfsRapid'] = UNSET
    storm: Union[Unset, 'PerfsStorm'] = UNSET
    racer: Union[Unset, 'PerfsRacer'] = UNSET
    streak: Union[Unset, 'PerfsStreak'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.perfs_ultra_bullet import PerfsUltraBullet
        from ..models.perfs_blitz import PerfsBlitz
        from ..models.perfs_rapid import PerfsRapid
        from ..models.perfs_antichess import PerfsAntichess
        from ..models.perfs_racer import PerfsRacer
        from ..models.perfs_racing_kings import PerfsRacingKings
        from ..models.perfs_chess_960 import PerfsChess960
        from ..models.perfs_three_check import PerfsThreeCheck
        from ..models.perfs_streak import PerfsStreak
        from ..models.perfs_storm import PerfsStorm
        from ..models.perfs_classical import PerfsClassical
        from ..models.perfs_bullet import PerfsBullet
        from ..models.perfs_horde import PerfsHorde
        from ..models.perfs_king_of_the_hill import PerfsKingOfTheHill
        from ..models.perfs_puzzle import PerfsPuzzle
        from ..models.perfs_crazyhouse import PerfsCrazyhouse
        from ..models.perfs_correspondence import PerfsCorrespondence
        from ..models.perfs_atomic import PerfsAtomic
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
        from ..models.perfs_ultra_bullet import PerfsUltraBullet
        from ..models.perfs_blitz import PerfsBlitz
        from ..models.perfs_rapid import PerfsRapid
        from ..models.perfs_antichess import PerfsAntichess
        from ..models.perfs_racer import PerfsRacer
        from ..models.perfs_racing_kings import PerfsRacingKings
        from ..models.perfs_chess_960 import PerfsChess960
        from ..models.perfs_three_check import PerfsThreeCheck
        from ..models.perfs_streak import PerfsStreak
        from ..models.perfs_storm import PerfsStorm
        from ..models.perfs_classical import PerfsClassical
        from ..models.perfs_bullet import PerfsBullet
        from ..models.perfs_horde import PerfsHorde
        from ..models.perfs_king_of_the_hill import PerfsKingOfTheHill
        from ..models.perfs_puzzle import PerfsPuzzle
        from ..models.perfs_crazyhouse import PerfsCrazyhouse
        from ..models.perfs_correspondence import PerfsCorrespondence
        from ..models.perfs_atomic import PerfsAtomic
        d = dict(src_dict)
        _chess960 = d.pop("chess960", UNSET)
        chess960: Union[Unset, PerfsChess960]
        if isinstance(_chess960,  Unset):
            chess960 = UNSET
        else:
            chess960 = PerfsChess960.from_dict(_chess960)




        _atomic = d.pop("atomic", UNSET)
        atomic: Union[Unset, PerfsAtomic]
        if isinstance(_atomic,  Unset):
            atomic = UNSET
        else:
            atomic = PerfsAtomic.from_dict(_atomic)




        _racing_kings = d.pop("racingKings", UNSET)
        racing_kings: Union[Unset, PerfsRacingKings]
        if isinstance(_racing_kings,  Unset):
            racing_kings = UNSET
        else:
            racing_kings = PerfsRacingKings.from_dict(_racing_kings)




        _ultra_bullet = d.pop("ultraBullet", UNSET)
        ultra_bullet: Union[Unset, PerfsUltraBullet]
        if isinstance(_ultra_bullet,  Unset):
            ultra_bullet = UNSET
        else:
            ultra_bullet = PerfsUltraBullet.from_dict(_ultra_bullet)




        _blitz = d.pop("blitz", UNSET)
        blitz: Union[Unset, PerfsBlitz]
        if isinstance(_blitz,  Unset):
            blitz = UNSET
        else:
            blitz = PerfsBlitz.from_dict(_blitz)




        _king_of_the_hill = d.pop("kingOfTheHill", UNSET)
        king_of_the_hill: Union[Unset, PerfsKingOfTheHill]
        if isinstance(_king_of_the_hill,  Unset):
            king_of_the_hill = UNSET
        else:
            king_of_the_hill = PerfsKingOfTheHill.from_dict(_king_of_the_hill)




        _three_check = d.pop("threeCheck", UNSET)
        three_check: Union[Unset, PerfsThreeCheck]
        if isinstance(_three_check,  Unset):
            three_check = UNSET
        else:
            three_check = PerfsThreeCheck.from_dict(_three_check)




        _antichess = d.pop("antichess", UNSET)
        antichess: Union[Unset, PerfsAntichess]
        if isinstance(_antichess,  Unset):
            antichess = UNSET
        else:
            antichess = PerfsAntichess.from_dict(_antichess)




        _crazyhouse = d.pop("crazyhouse", UNSET)
        crazyhouse: Union[Unset, PerfsCrazyhouse]
        if isinstance(_crazyhouse,  Unset):
            crazyhouse = UNSET
        else:
            crazyhouse = PerfsCrazyhouse.from_dict(_crazyhouse)




        _bullet = d.pop("bullet", UNSET)
        bullet: Union[Unset, PerfsBullet]
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = PerfsBullet.from_dict(_bullet)




        _correspondence = d.pop("correspondence", UNSET)
        correspondence: Union[Unset, PerfsCorrespondence]
        if isinstance(_correspondence,  Unset):
            correspondence = UNSET
        else:
            correspondence = PerfsCorrespondence.from_dict(_correspondence)




        _horde = d.pop("horde", UNSET)
        horde: Union[Unset, PerfsHorde]
        if isinstance(_horde,  Unset):
            horde = UNSET
        else:
            horde = PerfsHorde.from_dict(_horde)




        _puzzle = d.pop("puzzle", UNSET)
        puzzle: Union[Unset, PerfsPuzzle]
        if isinstance(_puzzle,  Unset):
            puzzle = UNSET
        else:
            puzzle = PerfsPuzzle.from_dict(_puzzle)




        _classical = d.pop("classical", UNSET)
        classical: Union[Unset, PerfsClassical]
        if isinstance(_classical,  Unset):
            classical = UNSET
        else:
            classical = PerfsClassical.from_dict(_classical)




        _rapid = d.pop("rapid", UNSET)
        rapid: Union[Unset, PerfsRapid]
        if isinstance(_rapid,  Unset):
            rapid = UNSET
        else:
            rapid = PerfsRapid.from_dict(_rapid)




        _storm = d.pop("storm", UNSET)
        storm: Union[Unset, PerfsStorm]
        if isinstance(_storm,  Unset):
            storm = UNSET
        else:
            storm = PerfsStorm.from_dict(_storm)




        _racer = d.pop("racer", UNSET)
        racer: Union[Unset, PerfsRacer]
        if isinstance(_racer,  Unset):
            racer = UNSET
        else:
            racer = PerfsRacer.from_dict(_racer)




        _streak = d.pop("streak", UNSET)
        streak: Union[Unset, PerfsStreak]
        if isinstance(_streak,  Unset):
            streak = UNSET
        else:
            streak = PerfsStreak.from_dict(_streak)




        perfs = cls(
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


        perfs.additional_properties = d
        return perfs

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
