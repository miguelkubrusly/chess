from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.team_request_with_user_user_perfs_three_check import TeamRequestWithUserUserPerfsThreeCheck
  from ..models.team_request_with_user_user_perfs_rapid import TeamRequestWithUserUserPerfsRapid
  from ..models.team_request_with_user_user_perfs_storm import TeamRequestWithUserUserPerfsStorm
  from ..models.team_request_with_user_user_perfs_ultra_bullet import TeamRequestWithUserUserPerfsUltraBullet
  from ..models.team_request_with_user_user_perfs_atomic import TeamRequestWithUserUserPerfsAtomic
  from ..models.team_request_with_user_user_perfs_antichess import TeamRequestWithUserUserPerfsAntichess
  from ..models.team_request_with_user_user_perfs_horde import TeamRequestWithUserUserPerfsHorde
  from ..models.team_request_with_user_user_perfs_streak import TeamRequestWithUserUserPerfsStreak
  from ..models.team_request_with_user_user_perfs_racing_kings import TeamRequestWithUserUserPerfsRacingKings
  from ..models.team_request_with_user_user_perfs_correspondence import TeamRequestWithUserUserPerfsCorrespondence
  from ..models.team_request_with_user_user_perfs_classical import TeamRequestWithUserUserPerfsClassical
  from ..models.team_request_with_user_user_perfs_racer import TeamRequestWithUserUserPerfsRacer
  from ..models.team_request_with_user_user_perfs_puzzle import TeamRequestWithUserUserPerfsPuzzle
  from ..models.team_request_with_user_user_perfs_blitz import TeamRequestWithUserUserPerfsBlitz
  from ..models.team_request_with_user_user_perfs_king_of_the_hill import TeamRequestWithUserUserPerfsKingOfTheHill
  from ..models.team_request_with_user_user_perfs_bullet import TeamRequestWithUserUserPerfsBullet
  from ..models.team_request_with_user_user_perfs_crazyhouse import TeamRequestWithUserUserPerfsCrazyhouse
  from ..models.team_request_with_user_user_perfs_chess_960 import TeamRequestWithUserUserPerfsChess960





T = TypeVar("T", bound="TeamRequestWithUserUserPerfs")



@_attrs_define
class TeamRequestWithUserUserPerfs:
    """ 
        Attributes:
            chess960 (Union[Unset, TeamRequestWithUserUserPerfsChess960]):
            atomic (Union[Unset, TeamRequestWithUserUserPerfsAtomic]):
            racing_kings (Union[Unset, TeamRequestWithUserUserPerfsRacingKings]):
            ultra_bullet (Union[Unset, TeamRequestWithUserUserPerfsUltraBullet]):
            blitz (Union[Unset, TeamRequestWithUserUserPerfsBlitz]):
            king_of_the_hill (Union[Unset, TeamRequestWithUserUserPerfsKingOfTheHill]):
            three_check (Union[Unset, TeamRequestWithUserUserPerfsThreeCheck]):
            antichess (Union[Unset, TeamRequestWithUserUserPerfsAntichess]):
            crazyhouse (Union[Unset, TeamRequestWithUserUserPerfsCrazyhouse]):
            bullet (Union[Unset, TeamRequestWithUserUserPerfsBullet]):
            correspondence (Union[Unset, TeamRequestWithUserUserPerfsCorrespondence]):
            horde (Union[Unset, TeamRequestWithUserUserPerfsHorde]):
            puzzle (Union[Unset, TeamRequestWithUserUserPerfsPuzzle]):
            classical (Union[Unset, TeamRequestWithUserUserPerfsClassical]):
            rapid (Union[Unset, TeamRequestWithUserUserPerfsRapid]):
            storm (Union[Unset, TeamRequestWithUserUserPerfsStorm]):
            racer (Union[Unset, TeamRequestWithUserUserPerfsRacer]):
            streak (Union[Unset, TeamRequestWithUserUserPerfsStreak]):
     """

    chess960: Union[Unset, 'TeamRequestWithUserUserPerfsChess960'] = UNSET
    atomic: Union[Unset, 'TeamRequestWithUserUserPerfsAtomic'] = UNSET
    racing_kings: Union[Unset, 'TeamRequestWithUserUserPerfsRacingKings'] = UNSET
    ultra_bullet: Union[Unset, 'TeamRequestWithUserUserPerfsUltraBullet'] = UNSET
    blitz: Union[Unset, 'TeamRequestWithUserUserPerfsBlitz'] = UNSET
    king_of_the_hill: Union[Unset, 'TeamRequestWithUserUserPerfsKingOfTheHill'] = UNSET
    three_check: Union[Unset, 'TeamRequestWithUserUserPerfsThreeCheck'] = UNSET
    antichess: Union[Unset, 'TeamRequestWithUserUserPerfsAntichess'] = UNSET
    crazyhouse: Union[Unset, 'TeamRequestWithUserUserPerfsCrazyhouse'] = UNSET
    bullet: Union[Unset, 'TeamRequestWithUserUserPerfsBullet'] = UNSET
    correspondence: Union[Unset, 'TeamRequestWithUserUserPerfsCorrespondence'] = UNSET
    horde: Union[Unset, 'TeamRequestWithUserUserPerfsHorde'] = UNSET
    puzzle: Union[Unset, 'TeamRequestWithUserUserPerfsPuzzle'] = UNSET
    classical: Union[Unset, 'TeamRequestWithUserUserPerfsClassical'] = UNSET
    rapid: Union[Unset, 'TeamRequestWithUserUserPerfsRapid'] = UNSET
    storm: Union[Unset, 'TeamRequestWithUserUserPerfsStorm'] = UNSET
    racer: Union[Unset, 'TeamRequestWithUserUserPerfsRacer'] = UNSET
    streak: Union[Unset, 'TeamRequestWithUserUserPerfsStreak'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_request_with_user_user_perfs_three_check import TeamRequestWithUserUserPerfsThreeCheck
        from ..models.team_request_with_user_user_perfs_rapid import TeamRequestWithUserUserPerfsRapid
        from ..models.team_request_with_user_user_perfs_storm import TeamRequestWithUserUserPerfsStorm
        from ..models.team_request_with_user_user_perfs_ultra_bullet import TeamRequestWithUserUserPerfsUltraBullet
        from ..models.team_request_with_user_user_perfs_atomic import TeamRequestWithUserUserPerfsAtomic
        from ..models.team_request_with_user_user_perfs_antichess import TeamRequestWithUserUserPerfsAntichess
        from ..models.team_request_with_user_user_perfs_horde import TeamRequestWithUserUserPerfsHorde
        from ..models.team_request_with_user_user_perfs_streak import TeamRequestWithUserUserPerfsStreak
        from ..models.team_request_with_user_user_perfs_racing_kings import TeamRequestWithUserUserPerfsRacingKings
        from ..models.team_request_with_user_user_perfs_correspondence import TeamRequestWithUserUserPerfsCorrespondence
        from ..models.team_request_with_user_user_perfs_classical import TeamRequestWithUserUserPerfsClassical
        from ..models.team_request_with_user_user_perfs_racer import TeamRequestWithUserUserPerfsRacer
        from ..models.team_request_with_user_user_perfs_puzzle import TeamRequestWithUserUserPerfsPuzzle
        from ..models.team_request_with_user_user_perfs_blitz import TeamRequestWithUserUserPerfsBlitz
        from ..models.team_request_with_user_user_perfs_king_of_the_hill import TeamRequestWithUserUserPerfsKingOfTheHill
        from ..models.team_request_with_user_user_perfs_bullet import TeamRequestWithUserUserPerfsBullet
        from ..models.team_request_with_user_user_perfs_crazyhouse import TeamRequestWithUserUserPerfsCrazyhouse
        from ..models.team_request_with_user_user_perfs_chess_960 import TeamRequestWithUserUserPerfsChess960
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
        from ..models.team_request_with_user_user_perfs_three_check import TeamRequestWithUserUserPerfsThreeCheck
        from ..models.team_request_with_user_user_perfs_rapid import TeamRequestWithUserUserPerfsRapid
        from ..models.team_request_with_user_user_perfs_storm import TeamRequestWithUserUserPerfsStorm
        from ..models.team_request_with_user_user_perfs_ultra_bullet import TeamRequestWithUserUserPerfsUltraBullet
        from ..models.team_request_with_user_user_perfs_atomic import TeamRequestWithUserUserPerfsAtomic
        from ..models.team_request_with_user_user_perfs_antichess import TeamRequestWithUserUserPerfsAntichess
        from ..models.team_request_with_user_user_perfs_horde import TeamRequestWithUserUserPerfsHorde
        from ..models.team_request_with_user_user_perfs_streak import TeamRequestWithUserUserPerfsStreak
        from ..models.team_request_with_user_user_perfs_racing_kings import TeamRequestWithUserUserPerfsRacingKings
        from ..models.team_request_with_user_user_perfs_correspondence import TeamRequestWithUserUserPerfsCorrespondence
        from ..models.team_request_with_user_user_perfs_classical import TeamRequestWithUserUserPerfsClassical
        from ..models.team_request_with_user_user_perfs_racer import TeamRequestWithUserUserPerfsRacer
        from ..models.team_request_with_user_user_perfs_puzzle import TeamRequestWithUserUserPerfsPuzzle
        from ..models.team_request_with_user_user_perfs_blitz import TeamRequestWithUserUserPerfsBlitz
        from ..models.team_request_with_user_user_perfs_king_of_the_hill import TeamRequestWithUserUserPerfsKingOfTheHill
        from ..models.team_request_with_user_user_perfs_bullet import TeamRequestWithUserUserPerfsBullet
        from ..models.team_request_with_user_user_perfs_crazyhouse import TeamRequestWithUserUserPerfsCrazyhouse
        from ..models.team_request_with_user_user_perfs_chess_960 import TeamRequestWithUserUserPerfsChess960
        d = dict(src_dict)
        _chess960 = d.pop("chess960", UNSET)
        chess960: Union[Unset, TeamRequestWithUserUserPerfsChess960]
        if isinstance(_chess960,  Unset):
            chess960 = UNSET
        else:
            chess960 = TeamRequestWithUserUserPerfsChess960.from_dict(_chess960)




        _atomic = d.pop("atomic", UNSET)
        atomic: Union[Unset, TeamRequestWithUserUserPerfsAtomic]
        if isinstance(_atomic,  Unset):
            atomic = UNSET
        else:
            atomic = TeamRequestWithUserUserPerfsAtomic.from_dict(_atomic)




        _racing_kings = d.pop("racingKings", UNSET)
        racing_kings: Union[Unset, TeamRequestWithUserUserPerfsRacingKings]
        if isinstance(_racing_kings,  Unset):
            racing_kings = UNSET
        else:
            racing_kings = TeamRequestWithUserUserPerfsRacingKings.from_dict(_racing_kings)




        _ultra_bullet = d.pop("ultraBullet", UNSET)
        ultra_bullet: Union[Unset, TeamRequestWithUserUserPerfsUltraBullet]
        if isinstance(_ultra_bullet,  Unset):
            ultra_bullet = UNSET
        else:
            ultra_bullet = TeamRequestWithUserUserPerfsUltraBullet.from_dict(_ultra_bullet)




        _blitz = d.pop("blitz", UNSET)
        blitz: Union[Unset, TeamRequestWithUserUserPerfsBlitz]
        if isinstance(_blitz,  Unset):
            blitz = UNSET
        else:
            blitz = TeamRequestWithUserUserPerfsBlitz.from_dict(_blitz)




        _king_of_the_hill = d.pop("kingOfTheHill", UNSET)
        king_of_the_hill: Union[Unset, TeamRequestWithUserUserPerfsKingOfTheHill]
        if isinstance(_king_of_the_hill,  Unset):
            king_of_the_hill = UNSET
        else:
            king_of_the_hill = TeamRequestWithUserUserPerfsKingOfTheHill.from_dict(_king_of_the_hill)




        _three_check = d.pop("threeCheck", UNSET)
        three_check: Union[Unset, TeamRequestWithUserUserPerfsThreeCheck]
        if isinstance(_three_check,  Unset):
            three_check = UNSET
        else:
            three_check = TeamRequestWithUserUserPerfsThreeCheck.from_dict(_three_check)




        _antichess = d.pop("antichess", UNSET)
        antichess: Union[Unset, TeamRequestWithUserUserPerfsAntichess]
        if isinstance(_antichess,  Unset):
            antichess = UNSET
        else:
            antichess = TeamRequestWithUserUserPerfsAntichess.from_dict(_antichess)




        _crazyhouse = d.pop("crazyhouse", UNSET)
        crazyhouse: Union[Unset, TeamRequestWithUserUserPerfsCrazyhouse]
        if isinstance(_crazyhouse,  Unset):
            crazyhouse = UNSET
        else:
            crazyhouse = TeamRequestWithUserUserPerfsCrazyhouse.from_dict(_crazyhouse)




        _bullet = d.pop("bullet", UNSET)
        bullet: Union[Unset, TeamRequestWithUserUserPerfsBullet]
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = TeamRequestWithUserUserPerfsBullet.from_dict(_bullet)




        _correspondence = d.pop("correspondence", UNSET)
        correspondence: Union[Unset, TeamRequestWithUserUserPerfsCorrespondence]
        if isinstance(_correspondence,  Unset):
            correspondence = UNSET
        else:
            correspondence = TeamRequestWithUserUserPerfsCorrespondence.from_dict(_correspondence)




        _horde = d.pop("horde", UNSET)
        horde: Union[Unset, TeamRequestWithUserUserPerfsHorde]
        if isinstance(_horde,  Unset):
            horde = UNSET
        else:
            horde = TeamRequestWithUserUserPerfsHorde.from_dict(_horde)




        _puzzle = d.pop("puzzle", UNSET)
        puzzle: Union[Unset, TeamRequestWithUserUserPerfsPuzzle]
        if isinstance(_puzzle,  Unset):
            puzzle = UNSET
        else:
            puzzle = TeamRequestWithUserUserPerfsPuzzle.from_dict(_puzzle)




        _classical = d.pop("classical", UNSET)
        classical: Union[Unset, TeamRequestWithUserUserPerfsClassical]
        if isinstance(_classical,  Unset):
            classical = UNSET
        else:
            classical = TeamRequestWithUserUserPerfsClassical.from_dict(_classical)




        _rapid = d.pop("rapid", UNSET)
        rapid: Union[Unset, TeamRequestWithUserUserPerfsRapid]
        if isinstance(_rapid,  Unset):
            rapid = UNSET
        else:
            rapid = TeamRequestWithUserUserPerfsRapid.from_dict(_rapid)




        _storm = d.pop("storm", UNSET)
        storm: Union[Unset, TeamRequestWithUserUserPerfsStorm]
        if isinstance(_storm,  Unset):
            storm = UNSET
        else:
            storm = TeamRequestWithUserUserPerfsStorm.from_dict(_storm)




        _racer = d.pop("racer", UNSET)
        racer: Union[Unset, TeamRequestWithUserUserPerfsRacer]
        if isinstance(_racer,  Unset):
            racer = UNSET
        else:
            racer = TeamRequestWithUserUserPerfsRacer.from_dict(_racer)




        _streak = d.pop("streak", UNSET)
        streak: Union[Unset, TeamRequestWithUserUserPerfsStreak]
        if isinstance(_streak,  Unset):
            streak = UNSET
        else:
            streak = TeamRequestWithUserUserPerfsStreak.from_dict(_streak)




        team_request_with_user_user_perfs = cls(
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


        team_request_with_user_user_perfs.additional_properties = d
        return team_request_with_user_user_perfs

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
