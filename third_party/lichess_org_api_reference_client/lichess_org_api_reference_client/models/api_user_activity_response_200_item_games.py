from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.api_user_activity_response_200_item_games_ultra_bullet import ApiUserActivityResponse200ItemGamesUltraBullet
  from ..models.api_user_activity_response_200_item_games_racing_kings import ApiUserActivityResponse200ItemGamesRacingKings
  from ..models.api_user_activity_response_200_item_games_correspondence import ApiUserActivityResponse200ItemGamesCorrespondence
  from ..models.api_user_activity_response_200_item_games_bullet import ApiUserActivityResponse200ItemGamesBullet
  from ..models.api_user_activity_response_200_item_games_atomic import ApiUserActivityResponse200ItemGamesAtomic
  from ..models.api_user_activity_response_200_item_games_chess_960 import ApiUserActivityResponse200ItemGamesChess960
  from ..models.api_user_activity_response_200_item_games_puzzle import ApiUserActivityResponse200ItemGamesPuzzle
  from ..models.api_user_activity_response_200_item_games_classical import ApiUserActivityResponse200ItemGamesClassical
  from ..models.api_user_activity_response_200_item_games_horde import ApiUserActivityResponse200ItemGamesHorde
  from ..models.api_user_activity_response_200_item_games_rapid import ApiUserActivityResponse200ItemGamesRapid
  from ..models.api_user_activity_response_200_item_games_king_of_the_hill import ApiUserActivityResponse200ItemGamesKingOfTheHill
  from ..models.api_user_activity_response_200_item_games_blitz import ApiUserActivityResponse200ItemGamesBlitz





T = TypeVar("T", bound="ApiUserActivityResponse200ItemGames")



@_attrs_define
class ApiUserActivityResponse200ItemGames:
    """ 
        Attributes:
            chess960 (Union[Unset, ApiUserActivityResponse200ItemGamesChess960]):
            atomic (Union[Unset, ApiUserActivityResponse200ItemGamesAtomic]):
            racing_kings (Union[Unset, ApiUserActivityResponse200ItemGamesRacingKings]):
            ultra_bullet (Union[Unset, ApiUserActivityResponse200ItemGamesUltraBullet]):
            blitz (Union[Unset, ApiUserActivityResponse200ItemGamesBlitz]):
            king_of_the_hill (Union[Unset, ApiUserActivityResponse200ItemGamesKingOfTheHill]):
            bullet (Union[Unset, ApiUserActivityResponse200ItemGamesBullet]):
            correspondence (Union[Unset, ApiUserActivityResponse200ItemGamesCorrespondence]):
            horde (Union[Unset, ApiUserActivityResponse200ItemGamesHorde]):
            puzzle (Union[Unset, ApiUserActivityResponse200ItemGamesPuzzle]):
            classical (Union[Unset, ApiUserActivityResponse200ItemGamesClassical]):
            rapid (Union[Unset, ApiUserActivityResponse200ItemGamesRapid]):
     """

    chess960: Union[Unset, 'ApiUserActivityResponse200ItemGamesChess960'] = UNSET
    atomic: Union[Unset, 'ApiUserActivityResponse200ItemGamesAtomic'] = UNSET
    racing_kings: Union[Unset, 'ApiUserActivityResponse200ItemGamesRacingKings'] = UNSET
    ultra_bullet: Union[Unset, 'ApiUserActivityResponse200ItemGamesUltraBullet'] = UNSET
    blitz: Union[Unset, 'ApiUserActivityResponse200ItemGamesBlitz'] = UNSET
    king_of_the_hill: Union[Unset, 'ApiUserActivityResponse200ItemGamesKingOfTheHill'] = UNSET
    bullet: Union[Unset, 'ApiUserActivityResponse200ItemGamesBullet'] = UNSET
    correspondence: Union[Unset, 'ApiUserActivityResponse200ItemGamesCorrespondence'] = UNSET
    horde: Union[Unset, 'ApiUserActivityResponse200ItemGamesHorde'] = UNSET
    puzzle: Union[Unset, 'ApiUserActivityResponse200ItemGamesPuzzle'] = UNSET
    classical: Union[Unset, 'ApiUserActivityResponse200ItemGamesClassical'] = UNSET
    rapid: Union[Unset, 'ApiUserActivityResponse200ItemGamesRapid'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_user_activity_response_200_item_games_ultra_bullet import ApiUserActivityResponse200ItemGamesUltraBullet
        from ..models.api_user_activity_response_200_item_games_racing_kings import ApiUserActivityResponse200ItemGamesRacingKings
        from ..models.api_user_activity_response_200_item_games_correspondence import ApiUserActivityResponse200ItemGamesCorrespondence
        from ..models.api_user_activity_response_200_item_games_bullet import ApiUserActivityResponse200ItemGamesBullet
        from ..models.api_user_activity_response_200_item_games_atomic import ApiUserActivityResponse200ItemGamesAtomic
        from ..models.api_user_activity_response_200_item_games_chess_960 import ApiUserActivityResponse200ItemGamesChess960
        from ..models.api_user_activity_response_200_item_games_puzzle import ApiUserActivityResponse200ItemGamesPuzzle
        from ..models.api_user_activity_response_200_item_games_classical import ApiUserActivityResponse200ItemGamesClassical
        from ..models.api_user_activity_response_200_item_games_horde import ApiUserActivityResponse200ItemGamesHorde
        from ..models.api_user_activity_response_200_item_games_rapid import ApiUserActivityResponse200ItemGamesRapid
        from ..models.api_user_activity_response_200_item_games_king_of_the_hill import ApiUserActivityResponse200ItemGamesKingOfTheHill
        from ..models.api_user_activity_response_200_item_games_blitz import ApiUserActivityResponse200ItemGamesBlitz
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_user_activity_response_200_item_games_ultra_bullet import ApiUserActivityResponse200ItemGamesUltraBullet
        from ..models.api_user_activity_response_200_item_games_racing_kings import ApiUserActivityResponse200ItemGamesRacingKings
        from ..models.api_user_activity_response_200_item_games_correspondence import ApiUserActivityResponse200ItemGamesCorrespondence
        from ..models.api_user_activity_response_200_item_games_bullet import ApiUserActivityResponse200ItemGamesBullet
        from ..models.api_user_activity_response_200_item_games_atomic import ApiUserActivityResponse200ItemGamesAtomic
        from ..models.api_user_activity_response_200_item_games_chess_960 import ApiUserActivityResponse200ItemGamesChess960
        from ..models.api_user_activity_response_200_item_games_puzzle import ApiUserActivityResponse200ItemGamesPuzzle
        from ..models.api_user_activity_response_200_item_games_classical import ApiUserActivityResponse200ItemGamesClassical
        from ..models.api_user_activity_response_200_item_games_horde import ApiUserActivityResponse200ItemGamesHorde
        from ..models.api_user_activity_response_200_item_games_rapid import ApiUserActivityResponse200ItemGamesRapid
        from ..models.api_user_activity_response_200_item_games_king_of_the_hill import ApiUserActivityResponse200ItemGamesKingOfTheHill
        from ..models.api_user_activity_response_200_item_games_blitz import ApiUserActivityResponse200ItemGamesBlitz
        d = dict(src_dict)
        _chess960 = d.pop("chess960", UNSET)
        chess960: Union[Unset, ApiUserActivityResponse200ItemGamesChess960]
        if isinstance(_chess960,  Unset):
            chess960 = UNSET
        else:
            chess960 = ApiUserActivityResponse200ItemGamesChess960.from_dict(_chess960)




        _atomic = d.pop("atomic", UNSET)
        atomic: Union[Unset, ApiUserActivityResponse200ItemGamesAtomic]
        if isinstance(_atomic,  Unset):
            atomic = UNSET
        else:
            atomic = ApiUserActivityResponse200ItemGamesAtomic.from_dict(_atomic)




        _racing_kings = d.pop("racingKings", UNSET)
        racing_kings: Union[Unset, ApiUserActivityResponse200ItemGamesRacingKings]
        if isinstance(_racing_kings,  Unset):
            racing_kings = UNSET
        else:
            racing_kings = ApiUserActivityResponse200ItemGamesRacingKings.from_dict(_racing_kings)




        _ultra_bullet = d.pop("ultraBullet", UNSET)
        ultra_bullet: Union[Unset, ApiUserActivityResponse200ItemGamesUltraBullet]
        if isinstance(_ultra_bullet,  Unset):
            ultra_bullet = UNSET
        else:
            ultra_bullet = ApiUserActivityResponse200ItemGamesUltraBullet.from_dict(_ultra_bullet)




        _blitz = d.pop("blitz", UNSET)
        blitz: Union[Unset, ApiUserActivityResponse200ItemGamesBlitz]
        if isinstance(_blitz,  Unset):
            blitz = UNSET
        else:
            blitz = ApiUserActivityResponse200ItemGamesBlitz.from_dict(_blitz)




        _king_of_the_hill = d.pop("kingOfTheHill", UNSET)
        king_of_the_hill: Union[Unset, ApiUserActivityResponse200ItemGamesKingOfTheHill]
        if isinstance(_king_of_the_hill,  Unset):
            king_of_the_hill = UNSET
        else:
            king_of_the_hill = ApiUserActivityResponse200ItemGamesKingOfTheHill.from_dict(_king_of_the_hill)




        _bullet = d.pop("bullet", UNSET)
        bullet: Union[Unset, ApiUserActivityResponse200ItemGamesBullet]
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = ApiUserActivityResponse200ItemGamesBullet.from_dict(_bullet)




        _correspondence = d.pop("correspondence", UNSET)
        correspondence: Union[Unset, ApiUserActivityResponse200ItemGamesCorrespondence]
        if isinstance(_correspondence,  Unset):
            correspondence = UNSET
        else:
            correspondence = ApiUserActivityResponse200ItemGamesCorrespondence.from_dict(_correspondence)




        _horde = d.pop("horde", UNSET)
        horde: Union[Unset, ApiUserActivityResponse200ItemGamesHorde]
        if isinstance(_horde,  Unset):
            horde = UNSET
        else:
            horde = ApiUserActivityResponse200ItemGamesHorde.from_dict(_horde)




        _puzzle = d.pop("puzzle", UNSET)
        puzzle: Union[Unset, ApiUserActivityResponse200ItemGamesPuzzle]
        if isinstance(_puzzle,  Unset):
            puzzle = UNSET
        else:
            puzzle = ApiUserActivityResponse200ItemGamesPuzzle.from_dict(_puzzle)




        _classical = d.pop("classical", UNSET)
        classical: Union[Unset, ApiUserActivityResponse200ItemGamesClassical]
        if isinstance(_classical,  Unset):
            classical = UNSET
        else:
            classical = ApiUserActivityResponse200ItemGamesClassical.from_dict(_classical)




        _rapid = d.pop("rapid", UNSET)
        rapid: Union[Unset, ApiUserActivityResponse200ItemGamesRapid]
        if isinstance(_rapid,  Unset):
            rapid = UNSET
        else:
            rapid = ApiUserActivityResponse200ItemGamesRapid.from_dict(_rapid)




        api_user_activity_response_200_item_games = cls(
            chess960=chess960,
            atomic=atomic,
            racing_kings=racing_kings,
            ultra_bullet=ultra_bullet,
            blitz=blitz,
            king_of_the_hill=king_of_the_hill,
            bullet=bullet,
            correspondence=correspondence,
            horde=horde,
            puzzle=puzzle,
            classical=classical,
            rapid=rapid,
        )


        api_user_activity_response_200_item_games.additional_properties = d
        return api_user_activity_response_200_item_games

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
