from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.team_requests_response_200_item_user_perfs_atomic import TeamRequestsResponse200ItemUserPerfsAtomic
  from ..models.team_requests_response_200_item_user_perfs_rapid import TeamRequestsResponse200ItemUserPerfsRapid
  from ..models.team_requests_response_200_item_user_perfs_antichess import TeamRequestsResponse200ItemUserPerfsAntichess
  from ..models.team_requests_response_200_item_user_perfs_bullet import TeamRequestsResponse200ItemUserPerfsBullet
  from ..models.team_requests_response_200_item_user_perfs_chess_960 import TeamRequestsResponse200ItemUserPerfsChess960
  from ..models.team_requests_response_200_item_user_perfs_horde import TeamRequestsResponse200ItemUserPerfsHorde
  from ..models.team_requests_response_200_item_user_perfs_storm import TeamRequestsResponse200ItemUserPerfsStorm
  from ..models.team_requests_response_200_item_user_perfs_crazyhouse import TeamRequestsResponse200ItemUserPerfsCrazyhouse
  from ..models.team_requests_response_200_item_user_perfs_classical import TeamRequestsResponse200ItemUserPerfsClassical
  from ..models.team_requests_response_200_item_user_perfs_puzzle import TeamRequestsResponse200ItemUserPerfsPuzzle
  from ..models.team_requests_response_200_item_user_perfs_streak import TeamRequestsResponse200ItemUserPerfsStreak
  from ..models.team_requests_response_200_item_user_perfs_blitz import TeamRequestsResponse200ItemUserPerfsBlitz
  from ..models.team_requests_response_200_item_user_perfs_racing_kings import TeamRequestsResponse200ItemUserPerfsRacingKings
  from ..models.team_requests_response_200_item_user_perfs_king_of_the_hill import TeamRequestsResponse200ItemUserPerfsKingOfTheHill
  from ..models.team_requests_response_200_item_user_perfs_three_check import TeamRequestsResponse200ItemUserPerfsThreeCheck
  from ..models.team_requests_response_200_item_user_perfs_racer import TeamRequestsResponse200ItemUserPerfsRacer
  from ..models.team_requests_response_200_item_user_perfs_correspondence import TeamRequestsResponse200ItemUserPerfsCorrespondence
  from ..models.team_requests_response_200_item_user_perfs_ultra_bullet import TeamRequestsResponse200ItemUserPerfsUltraBullet





T = TypeVar("T", bound="TeamRequestsResponse200ItemUserPerfs")



@_attrs_define
class TeamRequestsResponse200ItemUserPerfs:
    """ 
        Attributes:
            chess960 (Union[Unset, TeamRequestsResponse200ItemUserPerfsChess960]):
            atomic (Union[Unset, TeamRequestsResponse200ItemUserPerfsAtomic]):
            racing_kings (Union[Unset, TeamRequestsResponse200ItemUserPerfsRacingKings]):
            ultra_bullet (Union[Unset, TeamRequestsResponse200ItemUserPerfsUltraBullet]):
            blitz (Union[Unset, TeamRequestsResponse200ItemUserPerfsBlitz]):
            king_of_the_hill (Union[Unset, TeamRequestsResponse200ItemUserPerfsKingOfTheHill]):
            three_check (Union[Unset, TeamRequestsResponse200ItemUserPerfsThreeCheck]):
            antichess (Union[Unset, TeamRequestsResponse200ItemUserPerfsAntichess]):
            crazyhouse (Union[Unset, TeamRequestsResponse200ItemUserPerfsCrazyhouse]):
            bullet (Union[Unset, TeamRequestsResponse200ItemUserPerfsBullet]):
            correspondence (Union[Unset, TeamRequestsResponse200ItemUserPerfsCorrespondence]):
            horde (Union[Unset, TeamRequestsResponse200ItemUserPerfsHorde]):
            puzzle (Union[Unset, TeamRequestsResponse200ItemUserPerfsPuzzle]):
            classical (Union[Unset, TeamRequestsResponse200ItemUserPerfsClassical]):
            rapid (Union[Unset, TeamRequestsResponse200ItemUserPerfsRapid]):
            storm (Union[Unset, TeamRequestsResponse200ItemUserPerfsStorm]):
            racer (Union[Unset, TeamRequestsResponse200ItemUserPerfsRacer]):
            streak (Union[Unset, TeamRequestsResponse200ItemUserPerfsStreak]):
     """

    chess960: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsChess960'] = UNSET
    atomic: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsAtomic'] = UNSET
    racing_kings: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsRacingKings'] = UNSET
    ultra_bullet: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsUltraBullet'] = UNSET
    blitz: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsBlitz'] = UNSET
    king_of_the_hill: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsKingOfTheHill'] = UNSET
    three_check: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsThreeCheck'] = UNSET
    antichess: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsAntichess'] = UNSET
    crazyhouse: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsCrazyhouse'] = UNSET
    bullet: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsBullet'] = UNSET
    correspondence: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsCorrespondence'] = UNSET
    horde: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsHorde'] = UNSET
    puzzle: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsPuzzle'] = UNSET
    classical: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsClassical'] = UNSET
    rapid: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsRapid'] = UNSET
    storm: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsStorm'] = UNSET
    racer: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsRacer'] = UNSET
    streak: Union[Unset, 'TeamRequestsResponse200ItemUserPerfsStreak'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_requests_response_200_item_user_perfs_atomic import TeamRequestsResponse200ItemUserPerfsAtomic
        from ..models.team_requests_response_200_item_user_perfs_rapid import TeamRequestsResponse200ItemUserPerfsRapid
        from ..models.team_requests_response_200_item_user_perfs_antichess import TeamRequestsResponse200ItemUserPerfsAntichess
        from ..models.team_requests_response_200_item_user_perfs_bullet import TeamRequestsResponse200ItemUserPerfsBullet
        from ..models.team_requests_response_200_item_user_perfs_chess_960 import TeamRequestsResponse200ItemUserPerfsChess960
        from ..models.team_requests_response_200_item_user_perfs_horde import TeamRequestsResponse200ItemUserPerfsHorde
        from ..models.team_requests_response_200_item_user_perfs_storm import TeamRequestsResponse200ItemUserPerfsStorm
        from ..models.team_requests_response_200_item_user_perfs_crazyhouse import TeamRequestsResponse200ItemUserPerfsCrazyhouse
        from ..models.team_requests_response_200_item_user_perfs_classical import TeamRequestsResponse200ItemUserPerfsClassical
        from ..models.team_requests_response_200_item_user_perfs_puzzle import TeamRequestsResponse200ItemUserPerfsPuzzle
        from ..models.team_requests_response_200_item_user_perfs_streak import TeamRequestsResponse200ItemUserPerfsStreak
        from ..models.team_requests_response_200_item_user_perfs_blitz import TeamRequestsResponse200ItemUserPerfsBlitz
        from ..models.team_requests_response_200_item_user_perfs_racing_kings import TeamRequestsResponse200ItemUserPerfsRacingKings
        from ..models.team_requests_response_200_item_user_perfs_king_of_the_hill import TeamRequestsResponse200ItemUserPerfsKingOfTheHill
        from ..models.team_requests_response_200_item_user_perfs_three_check import TeamRequestsResponse200ItemUserPerfsThreeCheck
        from ..models.team_requests_response_200_item_user_perfs_racer import TeamRequestsResponse200ItemUserPerfsRacer
        from ..models.team_requests_response_200_item_user_perfs_correspondence import TeamRequestsResponse200ItemUserPerfsCorrespondence
        from ..models.team_requests_response_200_item_user_perfs_ultra_bullet import TeamRequestsResponse200ItemUserPerfsUltraBullet
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
        from ..models.team_requests_response_200_item_user_perfs_atomic import TeamRequestsResponse200ItemUserPerfsAtomic
        from ..models.team_requests_response_200_item_user_perfs_rapid import TeamRequestsResponse200ItemUserPerfsRapid
        from ..models.team_requests_response_200_item_user_perfs_antichess import TeamRequestsResponse200ItemUserPerfsAntichess
        from ..models.team_requests_response_200_item_user_perfs_bullet import TeamRequestsResponse200ItemUserPerfsBullet
        from ..models.team_requests_response_200_item_user_perfs_chess_960 import TeamRequestsResponse200ItemUserPerfsChess960
        from ..models.team_requests_response_200_item_user_perfs_horde import TeamRequestsResponse200ItemUserPerfsHorde
        from ..models.team_requests_response_200_item_user_perfs_storm import TeamRequestsResponse200ItemUserPerfsStorm
        from ..models.team_requests_response_200_item_user_perfs_crazyhouse import TeamRequestsResponse200ItemUserPerfsCrazyhouse
        from ..models.team_requests_response_200_item_user_perfs_classical import TeamRequestsResponse200ItemUserPerfsClassical
        from ..models.team_requests_response_200_item_user_perfs_puzzle import TeamRequestsResponse200ItemUserPerfsPuzzle
        from ..models.team_requests_response_200_item_user_perfs_streak import TeamRequestsResponse200ItemUserPerfsStreak
        from ..models.team_requests_response_200_item_user_perfs_blitz import TeamRequestsResponse200ItemUserPerfsBlitz
        from ..models.team_requests_response_200_item_user_perfs_racing_kings import TeamRequestsResponse200ItemUserPerfsRacingKings
        from ..models.team_requests_response_200_item_user_perfs_king_of_the_hill import TeamRequestsResponse200ItemUserPerfsKingOfTheHill
        from ..models.team_requests_response_200_item_user_perfs_three_check import TeamRequestsResponse200ItemUserPerfsThreeCheck
        from ..models.team_requests_response_200_item_user_perfs_racer import TeamRequestsResponse200ItemUserPerfsRacer
        from ..models.team_requests_response_200_item_user_perfs_correspondence import TeamRequestsResponse200ItemUserPerfsCorrespondence
        from ..models.team_requests_response_200_item_user_perfs_ultra_bullet import TeamRequestsResponse200ItemUserPerfsUltraBullet
        d = dict(src_dict)
        _chess960 = d.pop("chess960", UNSET)
        chess960: Union[Unset, TeamRequestsResponse200ItemUserPerfsChess960]
        if isinstance(_chess960,  Unset):
            chess960 = UNSET
        else:
            chess960 = TeamRequestsResponse200ItemUserPerfsChess960.from_dict(_chess960)




        _atomic = d.pop("atomic", UNSET)
        atomic: Union[Unset, TeamRequestsResponse200ItemUserPerfsAtomic]
        if isinstance(_atomic,  Unset):
            atomic = UNSET
        else:
            atomic = TeamRequestsResponse200ItemUserPerfsAtomic.from_dict(_atomic)




        _racing_kings = d.pop("racingKings", UNSET)
        racing_kings: Union[Unset, TeamRequestsResponse200ItemUserPerfsRacingKings]
        if isinstance(_racing_kings,  Unset):
            racing_kings = UNSET
        else:
            racing_kings = TeamRequestsResponse200ItemUserPerfsRacingKings.from_dict(_racing_kings)




        _ultra_bullet = d.pop("ultraBullet", UNSET)
        ultra_bullet: Union[Unset, TeamRequestsResponse200ItemUserPerfsUltraBullet]
        if isinstance(_ultra_bullet,  Unset):
            ultra_bullet = UNSET
        else:
            ultra_bullet = TeamRequestsResponse200ItemUserPerfsUltraBullet.from_dict(_ultra_bullet)




        _blitz = d.pop("blitz", UNSET)
        blitz: Union[Unset, TeamRequestsResponse200ItemUserPerfsBlitz]
        if isinstance(_blitz,  Unset):
            blitz = UNSET
        else:
            blitz = TeamRequestsResponse200ItemUserPerfsBlitz.from_dict(_blitz)




        _king_of_the_hill = d.pop("kingOfTheHill", UNSET)
        king_of_the_hill: Union[Unset, TeamRequestsResponse200ItemUserPerfsKingOfTheHill]
        if isinstance(_king_of_the_hill,  Unset):
            king_of_the_hill = UNSET
        else:
            king_of_the_hill = TeamRequestsResponse200ItemUserPerfsKingOfTheHill.from_dict(_king_of_the_hill)




        _three_check = d.pop("threeCheck", UNSET)
        three_check: Union[Unset, TeamRequestsResponse200ItemUserPerfsThreeCheck]
        if isinstance(_three_check,  Unset):
            three_check = UNSET
        else:
            three_check = TeamRequestsResponse200ItemUserPerfsThreeCheck.from_dict(_three_check)




        _antichess = d.pop("antichess", UNSET)
        antichess: Union[Unset, TeamRequestsResponse200ItemUserPerfsAntichess]
        if isinstance(_antichess,  Unset):
            antichess = UNSET
        else:
            antichess = TeamRequestsResponse200ItemUserPerfsAntichess.from_dict(_antichess)




        _crazyhouse = d.pop("crazyhouse", UNSET)
        crazyhouse: Union[Unset, TeamRequestsResponse200ItemUserPerfsCrazyhouse]
        if isinstance(_crazyhouse,  Unset):
            crazyhouse = UNSET
        else:
            crazyhouse = TeamRequestsResponse200ItemUserPerfsCrazyhouse.from_dict(_crazyhouse)




        _bullet = d.pop("bullet", UNSET)
        bullet: Union[Unset, TeamRequestsResponse200ItemUserPerfsBullet]
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = TeamRequestsResponse200ItemUserPerfsBullet.from_dict(_bullet)




        _correspondence = d.pop("correspondence", UNSET)
        correspondence: Union[Unset, TeamRequestsResponse200ItemUserPerfsCorrespondence]
        if isinstance(_correspondence,  Unset):
            correspondence = UNSET
        else:
            correspondence = TeamRequestsResponse200ItemUserPerfsCorrespondence.from_dict(_correspondence)




        _horde = d.pop("horde", UNSET)
        horde: Union[Unset, TeamRequestsResponse200ItemUserPerfsHorde]
        if isinstance(_horde,  Unset):
            horde = UNSET
        else:
            horde = TeamRequestsResponse200ItemUserPerfsHorde.from_dict(_horde)




        _puzzle = d.pop("puzzle", UNSET)
        puzzle: Union[Unset, TeamRequestsResponse200ItemUserPerfsPuzzle]
        if isinstance(_puzzle,  Unset):
            puzzle = UNSET
        else:
            puzzle = TeamRequestsResponse200ItemUserPerfsPuzzle.from_dict(_puzzle)




        _classical = d.pop("classical", UNSET)
        classical: Union[Unset, TeamRequestsResponse200ItemUserPerfsClassical]
        if isinstance(_classical,  Unset):
            classical = UNSET
        else:
            classical = TeamRequestsResponse200ItemUserPerfsClassical.from_dict(_classical)




        _rapid = d.pop("rapid", UNSET)
        rapid: Union[Unset, TeamRequestsResponse200ItemUserPerfsRapid]
        if isinstance(_rapid,  Unset):
            rapid = UNSET
        else:
            rapid = TeamRequestsResponse200ItemUserPerfsRapid.from_dict(_rapid)




        _storm = d.pop("storm", UNSET)
        storm: Union[Unset, TeamRequestsResponse200ItemUserPerfsStorm]
        if isinstance(_storm,  Unset):
            storm = UNSET
        else:
            storm = TeamRequestsResponse200ItemUserPerfsStorm.from_dict(_storm)




        _racer = d.pop("racer", UNSET)
        racer: Union[Unset, TeamRequestsResponse200ItemUserPerfsRacer]
        if isinstance(_racer,  Unset):
            racer = UNSET
        else:
            racer = TeamRequestsResponse200ItemUserPerfsRacer.from_dict(_racer)




        _streak = d.pop("streak", UNSET)
        streak: Union[Unset, TeamRequestsResponse200ItemUserPerfsStreak]
        if isinstance(_streak,  Unset):
            streak = UNSET
        else:
            streak = TeamRequestsResponse200ItemUserPerfsStreak.from_dict(_streak)




        team_requests_response_200_item_user_perfs = cls(
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


        team_requests_response_200_item_user_perfs.additional_properties = d
        return team_requests_response_200_item_user_perfs

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
