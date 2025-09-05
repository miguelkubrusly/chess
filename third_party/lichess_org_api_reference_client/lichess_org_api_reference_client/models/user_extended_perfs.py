from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.user_extended_perfs_chess_960 import UserExtendedPerfsChess960
  from ..models.user_extended_perfs_correspondence import UserExtendedPerfsCorrespondence
  from ..models.user_extended_perfs_rapid import UserExtendedPerfsRapid
  from ..models.user_extended_perfs_antichess import UserExtendedPerfsAntichess
  from ..models.user_extended_perfs_bullet import UserExtendedPerfsBullet
  from ..models.user_extended_perfs_crazyhouse import UserExtendedPerfsCrazyhouse
  from ..models.user_extended_perfs_racing_kings import UserExtendedPerfsRacingKings
  from ..models.user_extended_perfs_horde import UserExtendedPerfsHorde
  from ..models.user_extended_perfs_ultra_bullet import UserExtendedPerfsUltraBullet
  from ..models.user_extended_perfs_puzzle import UserExtendedPerfsPuzzle
  from ..models.user_extended_perfs_king_of_the_hill import UserExtendedPerfsKingOfTheHill
  from ..models.user_extended_perfs_storm import UserExtendedPerfsStorm
  from ..models.user_extended_perfs_racer import UserExtendedPerfsRacer
  from ..models.user_extended_perfs_streak import UserExtendedPerfsStreak
  from ..models.user_extended_perfs_blitz import UserExtendedPerfsBlitz
  from ..models.user_extended_perfs_atomic import UserExtendedPerfsAtomic
  from ..models.user_extended_perfs_classical import UserExtendedPerfsClassical
  from ..models.user_extended_perfs_three_check import UserExtendedPerfsThreeCheck





T = TypeVar("T", bound="UserExtendedPerfs")



@_attrs_define
class UserExtendedPerfs:
    """ 
        Attributes:
            chess960 (Union[Unset, UserExtendedPerfsChess960]):
            atomic (Union[Unset, UserExtendedPerfsAtomic]):
            racing_kings (Union[Unset, UserExtendedPerfsRacingKings]):
            ultra_bullet (Union[Unset, UserExtendedPerfsUltraBullet]):
            blitz (Union[Unset, UserExtendedPerfsBlitz]):
            king_of_the_hill (Union[Unset, UserExtendedPerfsKingOfTheHill]):
            three_check (Union[Unset, UserExtendedPerfsThreeCheck]):
            antichess (Union[Unset, UserExtendedPerfsAntichess]):
            crazyhouse (Union[Unset, UserExtendedPerfsCrazyhouse]):
            bullet (Union[Unset, UserExtendedPerfsBullet]):
            correspondence (Union[Unset, UserExtendedPerfsCorrespondence]):
            horde (Union[Unset, UserExtendedPerfsHorde]):
            puzzle (Union[Unset, UserExtendedPerfsPuzzle]):
            classical (Union[Unset, UserExtendedPerfsClassical]):
            rapid (Union[Unset, UserExtendedPerfsRapid]):
            storm (Union[Unset, UserExtendedPerfsStorm]):
            racer (Union[Unset, UserExtendedPerfsRacer]):
            streak (Union[Unset, UserExtendedPerfsStreak]):
     """

    chess960: Union[Unset, 'UserExtendedPerfsChess960'] = UNSET
    atomic: Union[Unset, 'UserExtendedPerfsAtomic'] = UNSET
    racing_kings: Union[Unset, 'UserExtendedPerfsRacingKings'] = UNSET
    ultra_bullet: Union[Unset, 'UserExtendedPerfsUltraBullet'] = UNSET
    blitz: Union[Unset, 'UserExtendedPerfsBlitz'] = UNSET
    king_of_the_hill: Union[Unset, 'UserExtendedPerfsKingOfTheHill'] = UNSET
    three_check: Union[Unset, 'UserExtendedPerfsThreeCheck'] = UNSET
    antichess: Union[Unset, 'UserExtendedPerfsAntichess'] = UNSET
    crazyhouse: Union[Unset, 'UserExtendedPerfsCrazyhouse'] = UNSET
    bullet: Union[Unset, 'UserExtendedPerfsBullet'] = UNSET
    correspondence: Union[Unset, 'UserExtendedPerfsCorrespondence'] = UNSET
    horde: Union[Unset, 'UserExtendedPerfsHorde'] = UNSET
    puzzle: Union[Unset, 'UserExtendedPerfsPuzzle'] = UNSET
    classical: Union[Unset, 'UserExtendedPerfsClassical'] = UNSET
    rapid: Union[Unset, 'UserExtendedPerfsRapid'] = UNSET
    storm: Union[Unset, 'UserExtendedPerfsStorm'] = UNSET
    racer: Union[Unset, 'UserExtendedPerfsRacer'] = UNSET
    streak: Union[Unset, 'UserExtendedPerfsStreak'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_extended_perfs_chess_960 import UserExtendedPerfsChess960
        from ..models.user_extended_perfs_correspondence import UserExtendedPerfsCorrespondence
        from ..models.user_extended_perfs_rapid import UserExtendedPerfsRapid
        from ..models.user_extended_perfs_antichess import UserExtendedPerfsAntichess
        from ..models.user_extended_perfs_bullet import UserExtendedPerfsBullet
        from ..models.user_extended_perfs_crazyhouse import UserExtendedPerfsCrazyhouse
        from ..models.user_extended_perfs_racing_kings import UserExtendedPerfsRacingKings
        from ..models.user_extended_perfs_horde import UserExtendedPerfsHorde
        from ..models.user_extended_perfs_ultra_bullet import UserExtendedPerfsUltraBullet
        from ..models.user_extended_perfs_puzzle import UserExtendedPerfsPuzzle
        from ..models.user_extended_perfs_king_of_the_hill import UserExtendedPerfsKingOfTheHill
        from ..models.user_extended_perfs_storm import UserExtendedPerfsStorm
        from ..models.user_extended_perfs_racer import UserExtendedPerfsRacer
        from ..models.user_extended_perfs_streak import UserExtendedPerfsStreak
        from ..models.user_extended_perfs_blitz import UserExtendedPerfsBlitz
        from ..models.user_extended_perfs_atomic import UserExtendedPerfsAtomic
        from ..models.user_extended_perfs_classical import UserExtendedPerfsClassical
        from ..models.user_extended_perfs_three_check import UserExtendedPerfsThreeCheck
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
        from ..models.user_extended_perfs_chess_960 import UserExtendedPerfsChess960
        from ..models.user_extended_perfs_correspondence import UserExtendedPerfsCorrespondence
        from ..models.user_extended_perfs_rapid import UserExtendedPerfsRapid
        from ..models.user_extended_perfs_antichess import UserExtendedPerfsAntichess
        from ..models.user_extended_perfs_bullet import UserExtendedPerfsBullet
        from ..models.user_extended_perfs_crazyhouse import UserExtendedPerfsCrazyhouse
        from ..models.user_extended_perfs_racing_kings import UserExtendedPerfsRacingKings
        from ..models.user_extended_perfs_horde import UserExtendedPerfsHorde
        from ..models.user_extended_perfs_ultra_bullet import UserExtendedPerfsUltraBullet
        from ..models.user_extended_perfs_puzzle import UserExtendedPerfsPuzzle
        from ..models.user_extended_perfs_king_of_the_hill import UserExtendedPerfsKingOfTheHill
        from ..models.user_extended_perfs_storm import UserExtendedPerfsStorm
        from ..models.user_extended_perfs_racer import UserExtendedPerfsRacer
        from ..models.user_extended_perfs_streak import UserExtendedPerfsStreak
        from ..models.user_extended_perfs_blitz import UserExtendedPerfsBlitz
        from ..models.user_extended_perfs_atomic import UserExtendedPerfsAtomic
        from ..models.user_extended_perfs_classical import UserExtendedPerfsClassical
        from ..models.user_extended_perfs_three_check import UserExtendedPerfsThreeCheck
        d = dict(src_dict)
        _chess960 = d.pop("chess960", UNSET)
        chess960: Union[Unset, UserExtendedPerfsChess960]
        if isinstance(_chess960,  Unset):
            chess960 = UNSET
        else:
            chess960 = UserExtendedPerfsChess960.from_dict(_chess960)




        _atomic = d.pop("atomic", UNSET)
        atomic: Union[Unset, UserExtendedPerfsAtomic]
        if isinstance(_atomic,  Unset):
            atomic = UNSET
        else:
            atomic = UserExtendedPerfsAtomic.from_dict(_atomic)




        _racing_kings = d.pop("racingKings", UNSET)
        racing_kings: Union[Unset, UserExtendedPerfsRacingKings]
        if isinstance(_racing_kings,  Unset):
            racing_kings = UNSET
        else:
            racing_kings = UserExtendedPerfsRacingKings.from_dict(_racing_kings)




        _ultra_bullet = d.pop("ultraBullet", UNSET)
        ultra_bullet: Union[Unset, UserExtendedPerfsUltraBullet]
        if isinstance(_ultra_bullet,  Unset):
            ultra_bullet = UNSET
        else:
            ultra_bullet = UserExtendedPerfsUltraBullet.from_dict(_ultra_bullet)




        _blitz = d.pop("blitz", UNSET)
        blitz: Union[Unset, UserExtendedPerfsBlitz]
        if isinstance(_blitz,  Unset):
            blitz = UNSET
        else:
            blitz = UserExtendedPerfsBlitz.from_dict(_blitz)




        _king_of_the_hill = d.pop("kingOfTheHill", UNSET)
        king_of_the_hill: Union[Unset, UserExtendedPerfsKingOfTheHill]
        if isinstance(_king_of_the_hill,  Unset):
            king_of_the_hill = UNSET
        else:
            king_of_the_hill = UserExtendedPerfsKingOfTheHill.from_dict(_king_of_the_hill)




        _three_check = d.pop("threeCheck", UNSET)
        three_check: Union[Unset, UserExtendedPerfsThreeCheck]
        if isinstance(_three_check,  Unset):
            three_check = UNSET
        else:
            three_check = UserExtendedPerfsThreeCheck.from_dict(_three_check)




        _antichess = d.pop("antichess", UNSET)
        antichess: Union[Unset, UserExtendedPerfsAntichess]
        if isinstance(_antichess,  Unset):
            antichess = UNSET
        else:
            antichess = UserExtendedPerfsAntichess.from_dict(_antichess)




        _crazyhouse = d.pop("crazyhouse", UNSET)
        crazyhouse: Union[Unset, UserExtendedPerfsCrazyhouse]
        if isinstance(_crazyhouse,  Unset):
            crazyhouse = UNSET
        else:
            crazyhouse = UserExtendedPerfsCrazyhouse.from_dict(_crazyhouse)




        _bullet = d.pop("bullet", UNSET)
        bullet: Union[Unset, UserExtendedPerfsBullet]
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = UserExtendedPerfsBullet.from_dict(_bullet)




        _correspondence = d.pop("correspondence", UNSET)
        correspondence: Union[Unset, UserExtendedPerfsCorrespondence]
        if isinstance(_correspondence,  Unset):
            correspondence = UNSET
        else:
            correspondence = UserExtendedPerfsCorrespondence.from_dict(_correspondence)




        _horde = d.pop("horde", UNSET)
        horde: Union[Unset, UserExtendedPerfsHorde]
        if isinstance(_horde,  Unset):
            horde = UNSET
        else:
            horde = UserExtendedPerfsHorde.from_dict(_horde)




        _puzzle = d.pop("puzzle", UNSET)
        puzzle: Union[Unset, UserExtendedPerfsPuzzle]
        if isinstance(_puzzle,  Unset):
            puzzle = UNSET
        else:
            puzzle = UserExtendedPerfsPuzzle.from_dict(_puzzle)




        _classical = d.pop("classical", UNSET)
        classical: Union[Unset, UserExtendedPerfsClassical]
        if isinstance(_classical,  Unset):
            classical = UNSET
        else:
            classical = UserExtendedPerfsClassical.from_dict(_classical)




        _rapid = d.pop("rapid", UNSET)
        rapid: Union[Unset, UserExtendedPerfsRapid]
        if isinstance(_rapid,  Unset):
            rapid = UNSET
        else:
            rapid = UserExtendedPerfsRapid.from_dict(_rapid)




        _storm = d.pop("storm", UNSET)
        storm: Union[Unset, UserExtendedPerfsStorm]
        if isinstance(_storm,  Unset):
            storm = UNSET
        else:
            storm = UserExtendedPerfsStorm.from_dict(_storm)




        _racer = d.pop("racer", UNSET)
        racer: Union[Unset, UserExtendedPerfsRacer]
        if isinstance(_racer,  Unset):
            racer = UNSET
        else:
            racer = UserExtendedPerfsRacer.from_dict(_racer)




        _streak = d.pop("streak", UNSET)
        streak: Union[Unset, UserExtendedPerfsStreak]
        if isinstance(_streak,  Unset):
            streak = UNSET
        else:
            streak = UserExtendedPerfsStreak.from_dict(_streak)




        user_extended_perfs = cls(
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


        user_extended_perfs.additional_properties = d
        return user_extended_perfs

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
