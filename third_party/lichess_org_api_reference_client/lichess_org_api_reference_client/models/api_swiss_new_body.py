from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_swiss_new_body_clock_limit import ApiSwissNewBodyClockLimit
from ..models.api_swiss_new_body_conditions_max_rating_rating import ApiSwissNewBodyConditionsMaxRatingRating
from ..models.api_swiss_new_body_conditions_min_rating_rating import ApiSwissNewBodyConditionsMinRatingRating
from ..models.api_swiss_new_body_round_interval import ApiSwissNewBodyRoundInterval
from ..models.api_swiss_new_body_variant import ApiSwissNewBodyVariant
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ApiSwissNewBody")



@_attrs_define
class ApiSwissNewBody:
    """ 
        Attributes:
            clock_limit (ApiSwissNewBodyClockLimit): Clock initial time in seconds Example: 300.
            clock_increment (int): Clock increment in seconds Example: 1.
            nb_rounds (int): Maximum number of rounds to play
            name (Union[Unset, str]): The tournament name. Leave empty to get a random Grandmaster name
            starts_at (Union[Unset, int]): Timestamp in milliseconds to start the tournament at a given date and time. By
                default, it starts 10 minutes after creation.
            round_interval (Union[Unset, ApiSwissNewBodyRoundInterval]): How long to wait between each round, in seconds.
                Set to 99999999 to manually schedule each round from the tournament UI.
                If empty or -1, a sensible value is picked automatically.
            variant (Union[Unset, ApiSwissNewBodyVariant]):  Default: ApiSwissNewBodyVariant.STANDARD. Example: standard.
            position (Union[Unset, str]): Custom initial position (in FEN). Variant must be standard and the game cannot be
                rated. Default: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'.
            description (Union[Unset, str]): Anything you want to tell players about the tournament
            rated (Union[Unset, bool]): Games are rated and impact players ratings Default: True.
            password (Union[Unset, str]): Make the tournament private and restrict access with a password.
            forbidden_pairings (Union[Unset, str]): Usernames of players that must not play together.
                Two usernames per line, separated by a space.
            manual_pairings (Union[Unset, str]): Manual pairings for the next round.
                Two usernames per line, separated by a space. Example:
                ```
                PlayerA PlayerB
                PlayerC PlayerD
                ```
                To give a bye (1 point) to a player instead of a pairing, add a line like so:
                ```
                PlayerE 1
                ```
                Missing players will be considered absent and get zero points.
            chat_for (Union[Unset, float]): Who can read and write in the chat.
                - 0  = No-one
                - 10 = Only team leaders
                - 20 = Only team members
                - 30 = All Lichess players
                 Default: 20.0.
            conditions_min_rating_rating (Union[Unset, ApiSwissNewBodyConditionsMinRatingRating]): Minimum rating to join.
                Leave empty to let everyone join the tournament.
            conditions_max_rating_rating (Union[Unset, ApiSwissNewBodyConditionsMaxRatingRating]): Maximum rating to join.
                Based on best rating reached in the last 7 days. Leave empty to let everyone join the tournament.
            conditions_nb_rated_game_nb (Union[Unset, int]): Minimum number of rated games required to join.
            conditions_play_your_games (Union[Unset, bool]): Only let players join if they have played their last swiss
                game.
                If they failed to show up in a recent swiss event, they won't be able to enter yours.
                This results in a better swiss experience for the players who actually show up.
                 Default: False.
            conditions_allow_list (Union[Unset, str]): Predefined list of usernames that are allowed to join, separated by
                commas.
                If this list is non-empty, then usernames absent from this list will be forbidden to join.
                Adding `%titled` to the list additionally allows any titled player to join.
                Example: `thibault,german11,%titled`
     """

    clock_limit: ApiSwissNewBodyClockLimit
    clock_increment: int
    nb_rounds: int
    name: Union[Unset, str] = UNSET
    starts_at: Union[Unset, int] = UNSET
    round_interval: Union[Unset, ApiSwissNewBodyRoundInterval] = UNSET
    variant: Union[Unset, ApiSwissNewBodyVariant] = ApiSwissNewBodyVariant.STANDARD
    position: Union[Unset, str] = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    description: Union[Unset, str] = UNSET
    rated: Union[Unset, bool] = True
    password: Union[Unset, str] = UNSET
    forbidden_pairings: Union[Unset, str] = UNSET
    manual_pairings: Union[Unset, str] = UNSET
    chat_for: Union[Unset, float] = 20.0
    conditions_min_rating_rating: Union[Unset, ApiSwissNewBodyConditionsMinRatingRating] = UNSET
    conditions_max_rating_rating: Union[Unset, ApiSwissNewBodyConditionsMaxRatingRating] = UNSET
    conditions_nb_rated_game_nb: Union[Unset, int] = UNSET
    conditions_play_your_games: Union[Unset, bool] = False
    conditions_allow_list: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        clock_limit = self.clock_limit.value

        clock_increment = self.clock_increment

        nb_rounds = self.nb_rounds

        name = self.name

        starts_at = self.starts_at

        round_interval: Union[Unset, int] = UNSET
        if not isinstance(self.round_interval, Unset):
            round_interval = self.round_interval.value


        variant: Union[Unset, str] = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.value


        position = self.position

        description = self.description

        rated = self.rated

        password = self.password

        forbidden_pairings = self.forbidden_pairings

        manual_pairings = self.manual_pairings

        chat_for = self.chat_for

        conditions_min_rating_rating: Union[Unset, int] = UNSET
        if not isinstance(self.conditions_min_rating_rating, Unset):
            conditions_min_rating_rating = self.conditions_min_rating_rating.value


        conditions_max_rating_rating: Union[Unset, int] = UNSET
        if not isinstance(self.conditions_max_rating_rating, Unset):
            conditions_max_rating_rating = self.conditions_max_rating_rating.value


        conditions_nb_rated_game_nb = self.conditions_nb_rated_game_nb

        conditions_play_your_games = self.conditions_play_your_games

        conditions_allow_list = self.conditions_allow_list


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "clock.limit": clock_limit,
            "clock.increment": clock_increment,
            "nbRounds": nb_rounds,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at
        if round_interval is not UNSET:
            field_dict["roundInterval"] = round_interval
        if variant is not UNSET:
            field_dict["variant"] = variant
        if position is not UNSET:
            field_dict["position"] = position
        if description is not UNSET:
            field_dict["description"] = description
        if rated is not UNSET:
            field_dict["rated"] = rated
        if password is not UNSET:
            field_dict["password"] = password
        if forbidden_pairings is not UNSET:
            field_dict["forbiddenPairings"] = forbidden_pairings
        if manual_pairings is not UNSET:
            field_dict["manualPairings"] = manual_pairings
        if chat_for is not UNSET:
            field_dict["chatFor"] = chat_for
        if conditions_min_rating_rating is not UNSET:
            field_dict["conditions.minRating.rating"] = conditions_min_rating_rating
        if conditions_max_rating_rating is not UNSET:
            field_dict["conditions.maxRating.rating"] = conditions_max_rating_rating
        if conditions_nb_rated_game_nb is not UNSET:
            field_dict["conditions.nbRatedGame.nb"] = conditions_nb_rated_game_nb
        if conditions_play_your_games is not UNSET:
            field_dict["conditions.playYourGames"] = conditions_play_your_games
        if conditions_allow_list is not UNSET:
            field_dict["conditions.allowList"] = conditions_allow_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clock_limit = ApiSwissNewBodyClockLimit(d.pop("clock.limit"))




        clock_increment = d.pop("clock.increment")

        nb_rounds = d.pop("nbRounds")

        name = d.pop("name", UNSET)

        starts_at = d.pop("startsAt", UNSET)

        _round_interval = d.pop("roundInterval", UNSET)
        round_interval: Union[Unset, ApiSwissNewBodyRoundInterval]
        if isinstance(_round_interval,  Unset):
            round_interval = UNSET
        else:
            round_interval = ApiSwissNewBodyRoundInterval(_round_interval)




        _variant = d.pop("variant", UNSET)
        variant: Union[Unset, ApiSwissNewBodyVariant]
        if isinstance(_variant,  Unset):
            variant = UNSET
        else:
            variant = ApiSwissNewBodyVariant(_variant)




        position = d.pop("position", UNSET)

        description = d.pop("description", UNSET)

        rated = d.pop("rated", UNSET)

        password = d.pop("password", UNSET)

        forbidden_pairings = d.pop("forbiddenPairings", UNSET)

        manual_pairings = d.pop("manualPairings", UNSET)

        chat_for = d.pop("chatFor", UNSET)

        _conditions_min_rating_rating = d.pop("conditions.minRating.rating", UNSET)
        conditions_min_rating_rating: Union[Unset, ApiSwissNewBodyConditionsMinRatingRating]
        if isinstance(_conditions_min_rating_rating,  Unset):
            conditions_min_rating_rating = UNSET
        else:
            conditions_min_rating_rating = ApiSwissNewBodyConditionsMinRatingRating(_conditions_min_rating_rating)




        _conditions_max_rating_rating = d.pop("conditions.maxRating.rating", UNSET)
        conditions_max_rating_rating: Union[Unset, ApiSwissNewBodyConditionsMaxRatingRating]
        if isinstance(_conditions_max_rating_rating,  Unset):
            conditions_max_rating_rating = UNSET
        else:
            conditions_max_rating_rating = ApiSwissNewBodyConditionsMaxRatingRating(_conditions_max_rating_rating)




        conditions_nb_rated_game_nb = d.pop("conditions.nbRatedGame.nb", UNSET)

        conditions_play_your_games = d.pop("conditions.playYourGames", UNSET)

        conditions_allow_list = d.pop("conditions.allowList", UNSET)

        api_swiss_new_body = cls(
            clock_limit=clock_limit,
            clock_increment=clock_increment,
            nb_rounds=nb_rounds,
            name=name,
            starts_at=starts_at,
            round_interval=round_interval,
            variant=variant,
            position=position,
            description=description,
            rated=rated,
            password=password,
            forbidden_pairings=forbidden_pairings,
            manual_pairings=manual_pairings,
            chat_for=chat_for,
            conditions_min_rating_rating=conditions_min_rating_rating,
            conditions_max_rating_rating=conditions_max_rating_rating,
            conditions_nb_rated_game_nb=conditions_nb_rated_game_nb,
            conditions_play_your_games=conditions_play_your_games,
            conditions_allow_list=conditions_allow_list,
        )


        api_swiss_new_body.additional_properties = d
        return api_swiss_new_body

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
