from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.account_me_response_200_perfs_three_check import AccountMeResponse200PerfsThreeCheck
  from ..models.account_me_response_200_perfs_king_of_the_hill import AccountMeResponse200PerfsKingOfTheHill
  from ..models.account_me_response_200_perfs_storm import AccountMeResponse200PerfsStorm
  from ..models.account_me_response_200_perfs_puzzle import AccountMeResponse200PerfsPuzzle
  from ..models.account_me_response_200_perfs_rapid import AccountMeResponse200PerfsRapid
  from ..models.account_me_response_200_perfs_chess_960 import AccountMeResponse200PerfsChess960
  from ..models.account_me_response_200_perfs_correspondence import AccountMeResponse200PerfsCorrespondence
  from ..models.account_me_response_200_perfs_racer import AccountMeResponse200PerfsRacer
  from ..models.account_me_response_200_perfs_blitz import AccountMeResponse200PerfsBlitz
  from ..models.account_me_response_200_perfs_racing_kings import AccountMeResponse200PerfsRacingKings
  from ..models.account_me_response_200_perfs_crazyhouse import AccountMeResponse200PerfsCrazyhouse
  from ..models.account_me_response_200_perfs_streak import AccountMeResponse200PerfsStreak
  from ..models.account_me_response_200_perfs_ultra_bullet import AccountMeResponse200PerfsUltraBullet
  from ..models.account_me_response_200_perfs_atomic import AccountMeResponse200PerfsAtomic
  from ..models.account_me_response_200_perfs_antichess import AccountMeResponse200PerfsAntichess
  from ..models.account_me_response_200_perfs_bullet import AccountMeResponse200PerfsBullet
  from ..models.account_me_response_200_perfs_horde import AccountMeResponse200PerfsHorde
  from ..models.account_me_response_200_perfs_classical import AccountMeResponse200PerfsClassical





T = TypeVar("T", bound="AccountMeResponse200Perfs")



@_attrs_define
class AccountMeResponse200Perfs:
    """ 
        Attributes:
            chess960 (Union[Unset, AccountMeResponse200PerfsChess960]):
            atomic (Union[Unset, AccountMeResponse200PerfsAtomic]):
            racing_kings (Union[Unset, AccountMeResponse200PerfsRacingKings]):
            ultra_bullet (Union[Unset, AccountMeResponse200PerfsUltraBullet]):
            blitz (Union[Unset, AccountMeResponse200PerfsBlitz]):
            king_of_the_hill (Union[Unset, AccountMeResponse200PerfsKingOfTheHill]):
            three_check (Union[Unset, AccountMeResponse200PerfsThreeCheck]):
            antichess (Union[Unset, AccountMeResponse200PerfsAntichess]):
            crazyhouse (Union[Unset, AccountMeResponse200PerfsCrazyhouse]):
            bullet (Union[Unset, AccountMeResponse200PerfsBullet]):
            correspondence (Union[Unset, AccountMeResponse200PerfsCorrespondence]):
            horde (Union[Unset, AccountMeResponse200PerfsHorde]):
            puzzle (Union[Unset, AccountMeResponse200PerfsPuzzle]):
            classical (Union[Unset, AccountMeResponse200PerfsClassical]):
            rapid (Union[Unset, AccountMeResponse200PerfsRapid]):
            storm (Union[Unset, AccountMeResponse200PerfsStorm]):
            racer (Union[Unset, AccountMeResponse200PerfsRacer]):
            streak (Union[Unset, AccountMeResponse200PerfsStreak]):
     """

    chess960: Union[Unset, 'AccountMeResponse200PerfsChess960'] = UNSET
    atomic: Union[Unset, 'AccountMeResponse200PerfsAtomic'] = UNSET
    racing_kings: Union[Unset, 'AccountMeResponse200PerfsRacingKings'] = UNSET
    ultra_bullet: Union[Unset, 'AccountMeResponse200PerfsUltraBullet'] = UNSET
    blitz: Union[Unset, 'AccountMeResponse200PerfsBlitz'] = UNSET
    king_of_the_hill: Union[Unset, 'AccountMeResponse200PerfsKingOfTheHill'] = UNSET
    three_check: Union[Unset, 'AccountMeResponse200PerfsThreeCheck'] = UNSET
    antichess: Union[Unset, 'AccountMeResponse200PerfsAntichess'] = UNSET
    crazyhouse: Union[Unset, 'AccountMeResponse200PerfsCrazyhouse'] = UNSET
    bullet: Union[Unset, 'AccountMeResponse200PerfsBullet'] = UNSET
    correspondence: Union[Unset, 'AccountMeResponse200PerfsCorrespondence'] = UNSET
    horde: Union[Unset, 'AccountMeResponse200PerfsHorde'] = UNSET
    puzzle: Union[Unset, 'AccountMeResponse200PerfsPuzzle'] = UNSET
    classical: Union[Unset, 'AccountMeResponse200PerfsClassical'] = UNSET
    rapid: Union[Unset, 'AccountMeResponse200PerfsRapid'] = UNSET
    storm: Union[Unset, 'AccountMeResponse200PerfsStorm'] = UNSET
    racer: Union[Unset, 'AccountMeResponse200PerfsRacer'] = UNSET
    streak: Union[Unset, 'AccountMeResponse200PerfsStreak'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_me_response_200_perfs_three_check import AccountMeResponse200PerfsThreeCheck
        from ..models.account_me_response_200_perfs_king_of_the_hill import AccountMeResponse200PerfsKingOfTheHill
        from ..models.account_me_response_200_perfs_storm import AccountMeResponse200PerfsStorm
        from ..models.account_me_response_200_perfs_puzzle import AccountMeResponse200PerfsPuzzle
        from ..models.account_me_response_200_perfs_rapid import AccountMeResponse200PerfsRapid
        from ..models.account_me_response_200_perfs_chess_960 import AccountMeResponse200PerfsChess960
        from ..models.account_me_response_200_perfs_correspondence import AccountMeResponse200PerfsCorrespondence
        from ..models.account_me_response_200_perfs_racer import AccountMeResponse200PerfsRacer
        from ..models.account_me_response_200_perfs_blitz import AccountMeResponse200PerfsBlitz
        from ..models.account_me_response_200_perfs_racing_kings import AccountMeResponse200PerfsRacingKings
        from ..models.account_me_response_200_perfs_crazyhouse import AccountMeResponse200PerfsCrazyhouse
        from ..models.account_me_response_200_perfs_streak import AccountMeResponse200PerfsStreak
        from ..models.account_me_response_200_perfs_ultra_bullet import AccountMeResponse200PerfsUltraBullet
        from ..models.account_me_response_200_perfs_atomic import AccountMeResponse200PerfsAtomic
        from ..models.account_me_response_200_perfs_antichess import AccountMeResponse200PerfsAntichess
        from ..models.account_me_response_200_perfs_bullet import AccountMeResponse200PerfsBullet
        from ..models.account_me_response_200_perfs_horde import AccountMeResponse200PerfsHorde
        from ..models.account_me_response_200_perfs_classical import AccountMeResponse200PerfsClassical
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
        from ..models.account_me_response_200_perfs_three_check import AccountMeResponse200PerfsThreeCheck
        from ..models.account_me_response_200_perfs_king_of_the_hill import AccountMeResponse200PerfsKingOfTheHill
        from ..models.account_me_response_200_perfs_storm import AccountMeResponse200PerfsStorm
        from ..models.account_me_response_200_perfs_puzzle import AccountMeResponse200PerfsPuzzle
        from ..models.account_me_response_200_perfs_rapid import AccountMeResponse200PerfsRapid
        from ..models.account_me_response_200_perfs_chess_960 import AccountMeResponse200PerfsChess960
        from ..models.account_me_response_200_perfs_correspondence import AccountMeResponse200PerfsCorrespondence
        from ..models.account_me_response_200_perfs_racer import AccountMeResponse200PerfsRacer
        from ..models.account_me_response_200_perfs_blitz import AccountMeResponse200PerfsBlitz
        from ..models.account_me_response_200_perfs_racing_kings import AccountMeResponse200PerfsRacingKings
        from ..models.account_me_response_200_perfs_crazyhouse import AccountMeResponse200PerfsCrazyhouse
        from ..models.account_me_response_200_perfs_streak import AccountMeResponse200PerfsStreak
        from ..models.account_me_response_200_perfs_ultra_bullet import AccountMeResponse200PerfsUltraBullet
        from ..models.account_me_response_200_perfs_atomic import AccountMeResponse200PerfsAtomic
        from ..models.account_me_response_200_perfs_antichess import AccountMeResponse200PerfsAntichess
        from ..models.account_me_response_200_perfs_bullet import AccountMeResponse200PerfsBullet
        from ..models.account_me_response_200_perfs_horde import AccountMeResponse200PerfsHorde
        from ..models.account_me_response_200_perfs_classical import AccountMeResponse200PerfsClassical
        d = dict(src_dict)
        _chess960 = d.pop("chess960", UNSET)
        chess960: Union[Unset, AccountMeResponse200PerfsChess960]
        if isinstance(_chess960,  Unset):
            chess960 = UNSET
        else:
            chess960 = AccountMeResponse200PerfsChess960.from_dict(_chess960)




        _atomic = d.pop("atomic", UNSET)
        atomic: Union[Unset, AccountMeResponse200PerfsAtomic]
        if isinstance(_atomic,  Unset):
            atomic = UNSET
        else:
            atomic = AccountMeResponse200PerfsAtomic.from_dict(_atomic)




        _racing_kings = d.pop("racingKings", UNSET)
        racing_kings: Union[Unset, AccountMeResponse200PerfsRacingKings]
        if isinstance(_racing_kings,  Unset):
            racing_kings = UNSET
        else:
            racing_kings = AccountMeResponse200PerfsRacingKings.from_dict(_racing_kings)




        _ultra_bullet = d.pop("ultraBullet", UNSET)
        ultra_bullet: Union[Unset, AccountMeResponse200PerfsUltraBullet]
        if isinstance(_ultra_bullet,  Unset):
            ultra_bullet = UNSET
        else:
            ultra_bullet = AccountMeResponse200PerfsUltraBullet.from_dict(_ultra_bullet)




        _blitz = d.pop("blitz", UNSET)
        blitz: Union[Unset, AccountMeResponse200PerfsBlitz]
        if isinstance(_blitz,  Unset):
            blitz = UNSET
        else:
            blitz = AccountMeResponse200PerfsBlitz.from_dict(_blitz)




        _king_of_the_hill = d.pop("kingOfTheHill", UNSET)
        king_of_the_hill: Union[Unset, AccountMeResponse200PerfsKingOfTheHill]
        if isinstance(_king_of_the_hill,  Unset):
            king_of_the_hill = UNSET
        else:
            king_of_the_hill = AccountMeResponse200PerfsKingOfTheHill.from_dict(_king_of_the_hill)




        _three_check = d.pop("threeCheck", UNSET)
        three_check: Union[Unset, AccountMeResponse200PerfsThreeCheck]
        if isinstance(_three_check,  Unset):
            three_check = UNSET
        else:
            three_check = AccountMeResponse200PerfsThreeCheck.from_dict(_three_check)




        _antichess = d.pop("antichess", UNSET)
        antichess: Union[Unset, AccountMeResponse200PerfsAntichess]
        if isinstance(_antichess,  Unset):
            antichess = UNSET
        else:
            antichess = AccountMeResponse200PerfsAntichess.from_dict(_antichess)




        _crazyhouse = d.pop("crazyhouse", UNSET)
        crazyhouse: Union[Unset, AccountMeResponse200PerfsCrazyhouse]
        if isinstance(_crazyhouse,  Unset):
            crazyhouse = UNSET
        else:
            crazyhouse = AccountMeResponse200PerfsCrazyhouse.from_dict(_crazyhouse)




        _bullet = d.pop("bullet", UNSET)
        bullet: Union[Unset, AccountMeResponse200PerfsBullet]
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = AccountMeResponse200PerfsBullet.from_dict(_bullet)




        _correspondence = d.pop("correspondence", UNSET)
        correspondence: Union[Unset, AccountMeResponse200PerfsCorrespondence]
        if isinstance(_correspondence,  Unset):
            correspondence = UNSET
        else:
            correspondence = AccountMeResponse200PerfsCorrespondence.from_dict(_correspondence)




        _horde = d.pop("horde", UNSET)
        horde: Union[Unset, AccountMeResponse200PerfsHorde]
        if isinstance(_horde,  Unset):
            horde = UNSET
        else:
            horde = AccountMeResponse200PerfsHorde.from_dict(_horde)




        _puzzle = d.pop("puzzle", UNSET)
        puzzle: Union[Unset, AccountMeResponse200PerfsPuzzle]
        if isinstance(_puzzle,  Unset):
            puzzle = UNSET
        else:
            puzzle = AccountMeResponse200PerfsPuzzle.from_dict(_puzzle)




        _classical = d.pop("classical", UNSET)
        classical: Union[Unset, AccountMeResponse200PerfsClassical]
        if isinstance(_classical,  Unset):
            classical = UNSET
        else:
            classical = AccountMeResponse200PerfsClassical.from_dict(_classical)




        _rapid = d.pop("rapid", UNSET)
        rapid: Union[Unset, AccountMeResponse200PerfsRapid]
        if isinstance(_rapid,  Unset):
            rapid = UNSET
        else:
            rapid = AccountMeResponse200PerfsRapid.from_dict(_rapid)




        _storm = d.pop("storm", UNSET)
        storm: Union[Unset, AccountMeResponse200PerfsStorm]
        if isinstance(_storm,  Unset):
            storm = UNSET
        else:
            storm = AccountMeResponse200PerfsStorm.from_dict(_storm)




        _racer = d.pop("racer", UNSET)
        racer: Union[Unset, AccountMeResponse200PerfsRacer]
        if isinstance(_racer,  Unset):
            racer = UNSET
        else:
            racer = AccountMeResponse200PerfsRacer.from_dict(_racer)




        _streak = d.pop("streak", UNSET)
        streak: Union[Unset, AccountMeResponse200PerfsStreak]
        if isinstance(_streak,  Unset):
            streak = UNSET
        else:
            streak = AccountMeResponse200PerfsStreak.from_dict(_streak)




        account_me_response_200_perfs = cls(
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


        account_me_response_200_perfs.additional_properties = d
        return account_me_response_200_perfs

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
