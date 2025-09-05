from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.tv_channels_response_200_bullet import TvChannelsResponse200Bullet
  from ..models.tv_channels_response_200_horde import TvChannelsResponse200Horde
  from ..models.tv_channels_response_200_ultra_bullet import TvChannelsResponse200UltraBullet
  from ..models.tv_channels_response_200_bot import TvChannelsResponse200Bot
  from ..models.tv_channels_response_200_chess_960 import TvChannelsResponse200Chess960
  from ..models.tv_channels_response_200_atomic import TvChannelsResponse200Atomic
  from ..models.tv_channels_response_200_king_of_the_hill import TvChannelsResponse200KingOfTheHill
  from ..models.tv_channels_response_200_crazyhouse import TvChannelsResponse200Crazyhouse
  from ..models.tv_channels_response_200_classical import TvChannelsResponse200Classical
  from ..models.tv_channels_response_200_racing_kings import TvChannelsResponse200RacingKings
  from ..models.tv_channels_response_200_computer import TvChannelsResponse200Computer
  from ..models.tv_channels_response_200_rapid import TvChannelsResponse200Rapid
  from ..models.tv_channels_response_200_best import TvChannelsResponse200Best
  from ..models.tv_channels_response_200_blitz import TvChannelsResponse200Blitz
  from ..models.tv_channels_response_200_antichess import TvChannelsResponse200Antichess
  from ..models.tv_channels_response_200_three_check import TvChannelsResponse200ThreeCheck





T = TypeVar("T", bound="TvChannelsResponse200")



@_attrs_define
class TvChannelsResponse200:
    """ 
        Attributes:
            bot (TvChannelsResponse200Bot):
            blitz (TvChannelsResponse200Blitz):
            racing_kings (TvChannelsResponse200RacingKings):
            ultra_bullet (TvChannelsResponse200UltraBullet):
            bullet (TvChannelsResponse200Bullet):
            classical (TvChannelsResponse200Classical):
            three_check (TvChannelsResponse200ThreeCheck):
            antichess (TvChannelsResponse200Antichess):
            computer (TvChannelsResponse200Computer):
            horde (TvChannelsResponse200Horde):
            rapid (TvChannelsResponse200Rapid):
            atomic (TvChannelsResponse200Atomic):
            crazyhouse (TvChannelsResponse200Crazyhouse):
            chess960 (TvChannelsResponse200Chess960):
            king_of_the_hill (TvChannelsResponse200KingOfTheHill):
            best (TvChannelsResponse200Best):
     """

    bot: 'TvChannelsResponse200Bot'
    blitz: 'TvChannelsResponse200Blitz'
    racing_kings: 'TvChannelsResponse200RacingKings'
    ultra_bullet: 'TvChannelsResponse200UltraBullet'
    bullet: 'TvChannelsResponse200Bullet'
    classical: 'TvChannelsResponse200Classical'
    three_check: 'TvChannelsResponse200ThreeCheck'
    antichess: 'TvChannelsResponse200Antichess'
    computer: 'TvChannelsResponse200Computer'
    horde: 'TvChannelsResponse200Horde'
    rapid: 'TvChannelsResponse200Rapid'
    atomic: 'TvChannelsResponse200Atomic'
    crazyhouse: 'TvChannelsResponse200Crazyhouse'
    chess960: 'TvChannelsResponse200Chess960'
    king_of_the_hill: 'TvChannelsResponse200KingOfTheHill'
    best: 'TvChannelsResponse200Best'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tv_channels_response_200_bullet import TvChannelsResponse200Bullet
        from ..models.tv_channels_response_200_horde import TvChannelsResponse200Horde
        from ..models.tv_channels_response_200_ultra_bullet import TvChannelsResponse200UltraBullet
        from ..models.tv_channels_response_200_bot import TvChannelsResponse200Bot
        from ..models.tv_channels_response_200_chess_960 import TvChannelsResponse200Chess960
        from ..models.tv_channels_response_200_atomic import TvChannelsResponse200Atomic
        from ..models.tv_channels_response_200_king_of_the_hill import TvChannelsResponse200KingOfTheHill
        from ..models.tv_channels_response_200_crazyhouse import TvChannelsResponse200Crazyhouse
        from ..models.tv_channels_response_200_classical import TvChannelsResponse200Classical
        from ..models.tv_channels_response_200_racing_kings import TvChannelsResponse200RacingKings
        from ..models.tv_channels_response_200_computer import TvChannelsResponse200Computer
        from ..models.tv_channels_response_200_rapid import TvChannelsResponse200Rapid
        from ..models.tv_channels_response_200_best import TvChannelsResponse200Best
        from ..models.tv_channels_response_200_blitz import TvChannelsResponse200Blitz
        from ..models.tv_channels_response_200_antichess import TvChannelsResponse200Antichess
        from ..models.tv_channels_response_200_three_check import TvChannelsResponse200ThreeCheck
        bot = self.bot.to_dict()

        blitz = self.blitz.to_dict()

        racing_kings = self.racing_kings.to_dict()

        ultra_bullet = self.ultra_bullet.to_dict()

        bullet = self.bullet.to_dict()

        classical = self.classical.to_dict()

        three_check = self.three_check.to_dict()

        antichess = self.antichess.to_dict()

        computer = self.computer.to_dict()

        horde = self.horde.to_dict()

        rapid = self.rapid.to_dict()

        atomic = self.atomic.to_dict()

        crazyhouse = self.crazyhouse.to_dict()

        chess960 = self.chess960.to_dict()

        king_of_the_hill = self.king_of_the_hill.to_dict()

        best = self.best.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "bot": bot,
            "blitz": blitz,
            "racingKings": racing_kings,
            "ultraBullet": ultra_bullet,
            "bullet": bullet,
            "classical": classical,
            "threeCheck": three_check,
            "antichess": antichess,
            "computer": computer,
            "horde": horde,
            "rapid": rapid,
            "atomic": atomic,
            "crazyhouse": crazyhouse,
            "chess960": chess960,
            "kingOfTheHill": king_of_the_hill,
            "best": best,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tv_channels_response_200_bullet import TvChannelsResponse200Bullet
        from ..models.tv_channels_response_200_horde import TvChannelsResponse200Horde
        from ..models.tv_channels_response_200_ultra_bullet import TvChannelsResponse200UltraBullet
        from ..models.tv_channels_response_200_bot import TvChannelsResponse200Bot
        from ..models.tv_channels_response_200_chess_960 import TvChannelsResponse200Chess960
        from ..models.tv_channels_response_200_atomic import TvChannelsResponse200Atomic
        from ..models.tv_channels_response_200_king_of_the_hill import TvChannelsResponse200KingOfTheHill
        from ..models.tv_channels_response_200_crazyhouse import TvChannelsResponse200Crazyhouse
        from ..models.tv_channels_response_200_classical import TvChannelsResponse200Classical
        from ..models.tv_channels_response_200_racing_kings import TvChannelsResponse200RacingKings
        from ..models.tv_channels_response_200_computer import TvChannelsResponse200Computer
        from ..models.tv_channels_response_200_rapid import TvChannelsResponse200Rapid
        from ..models.tv_channels_response_200_best import TvChannelsResponse200Best
        from ..models.tv_channels_response_200_blitz import TvChannelsResponse200Blitz
        from ..models.tv_channels_response_200_antichess import TvChannelsResponse200Antichess
        from ..models.tv_channels_response_200_three_check import TvChannelsResponse200ThreeCheck
        d = dict(src_dict)
        bot = TvChannelsResponse200Bot.from_dict(d.pop("bot"))




        blitz = TvChannelsResponse200Blitz.from_dict(d.pop("blitz"))




        racing_kings = TvChannelsResponse200RacingKings.from_dict(d.pop("racingKings"))




        ultra_bullet = TvChannelsResponse200UltraBullet.from_dict(d.pop("ultraBullet"))




        bullet = TvChannelsResponse200Bullet.from_dict(d.pop("bullet"))




        classical = TvChannelsResponse200Classical.from_dict(d.pop("classical"))




        three_check = TvChannelsResponse200ThreeCheck.from_dict(d.pop("threeCheck"))




        antichess = TvChannelsResponse200Antichess.from_dict(d.pop("antichess"))




        computer = TvChannelsResponse200Computer.from_dict(d.pop("computer"))




        horde = TvChannelsResponse200Horde.from_dict(d.pop("horde"))




        rapid = TvChannelsResponse200Rapid.from_dict(d.pop("rapid"))




        atomic = TvChannelsResponse200Atomic.from_dict(d.pop("atomic"))




        crazyhouse = TvChannelsResponse200Crazyhouse.from_dict(d.pop("crazyhouse"))




        chess960 = TvChannelsResponse200Chess960.from_dict(d.pop("chess960"))




        king_of_the_hill = TvChannelsResponse200KingOfTheHill.from_dict(d.pop("kingOfTheHill"))




        best = TvChannelsResponse200Best.from_dict(d.pop("best"))




        tv_channels_response_200 = cls(
            bot=bot,
            blitz=blitz,
            racing_kings=racing_kings,
            ultra_bullet=ultra_bullet,
            bullet=bullet,
            classical=classical,
            three_check=three_check,
            antichess=antichess,
            computer=computer,
            horde=horde,
            rapid=rapid,
            atomic=atomic,
            crazyhouse=crazyhouse,
            chess960=chess960,
            king_of_the_hill=king_of_the_hill,
            best=best,
        )


        tv_channels_response_200.additional_properties = d
        return tv_channels_response_200

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
