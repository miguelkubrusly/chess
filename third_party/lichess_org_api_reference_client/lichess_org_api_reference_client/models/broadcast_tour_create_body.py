from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.broadcast_tour_create_body_info_fide_tc import BroadcastTourCreateBodyInfoFideTc
from ..models.broadcast_tour_create_body_tiebreaks_item import BroadcastTourCreateBodyTiebreaksItem
from ..models.broadcast_tour_create_body_tier import BroadcastTourCreateBodyTier
from ..models.broadcast_tour_create_body_visibility import BroadcastTourCreateBodyVisibility
from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="BroadcastTourCreateBody")



@_attrs_define
class BroadcastTourCreateBody:
    """ 
        Attributes:
            name (str): Name of the broadcast tournament.

                Example: `Sinquefield Cup`
            info_format (Union[Unset, str]): Tournament format.
                Example: `"8-player round-robin" or "5-round Swiss"`
            info_location (Union[Unset, str]): Tournament Location
            info_tc (Union[Unset, str]): Time control.
                Example: `"Classical" or "Rapid" or "Rapid & Blitz"`
            info_fide_tc (Union[Unset, BroadcastTourCreateBodyInfoFideTc]): FIDE rating category. Which FIDE ratings to use
            info_time_zone (Union[Unset, str]): Timezone of the tournament. Example: `America/New_York`.
                See [list of possible timezone identifiers](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for
                more.
            info_players (Union[Unset, str]): Mention up to 4 of the best players participating.
            info_website (Union[Unset, str]): Official website. External website URL
            info_standings (Union[Unset, str]): Official Standings. External website URL, e.g. chess-results.com, info64.org
            markdown (Union[Unset, str]): Optional long description of the broadcast. Markdown is supported.
            show_scores (Union[Unset, bool]): Show players scores based on game results
                 Default: True.
            show_rating_diffs (Union[Unset, bool]): Show player's rating diffs
                 Default: True.
            team_table (Union[Unset, bool]): Show a team leaderboard. Requires WhiteTeam and BlackTeam PGN tags.
                 Default: False.
            visibility (Union[Unset, BroadcastTourCreateBodyVisibility]): Who can view the broadcast.
                * `public`: Default. Anyone can view the broadcast
                * `unlisted`: Only people with the link can view the broadcast
                * `private`: Only the broadcast owner(s) can view the broadcast
                 Default: BroadcastTourCreateBodyVisibility.PUBLIC.
            players (Union[Unset, str]): Optional replace player names, ratings and titles.

                One line per player, formatted as such:

                ```txt
                player name = FIDE ID
                ```

                Example:

                ```txt
                Magnus Carlsen = 1503014
                ```

                Player names ignore case and punctuation, and match all possible combinations of 2 words: "Jorge Rick Vito" will
                match "Jorge Rick", "jorge vito", "Rick, Vito", etc.

                If the player is NM or WNM, you can:

                ```txt
                Player Name = FIDE ID / Title
                ```

                Alternatively, you may set tags manually, like so:

                ```txt
                player name / rating / title / new name
                ```

                All values are optional. Example:
                ```txt
                Magnus Carlsen / 2863 / GM
                YouGotLittUp / 1890 / / Louis Litt
                ```
            teams (Union[Unset, str]): Optional: assign players to teams

                One line per player, formatted as such:
                ```txt
                Team name; Fide Id or Player name
                ```

                Example:
                ```txt
                Team Cats ; 3408230
                Team Dogs ; Scooby Doo
                ```

                By default the PGN tags WhiteTeam and BlackTeam are used.
            tier (Union[Unset, BroadcastTourCreateBodyTier]): Optional, for Lichess admins only, used to feature on
                /broadcast.

                * `3` for Official: normal tier
                * `4` for Official: high tier
                * `5` for Official: best tier
            tiebreaks (Union[Unset, list[BroadcastTourCreateBodyTiebreaksItem]]):
     """

    name: str
    info_format: Union[Unset, str] = UNSET
    info_location: Union[Unset, str] = UNSET
    info_tc: Union[Unset, str] = UNSET
    info_fide_tc: Union[Unset, BroadcastTourCreateBodyInfoFideTc] = UNSET
    info_time_zone: Union[Unset, str] = UNSET
    info_players: Union[Unset, str] = UNSET
    info_website: Union[Unset, str] = UNSET
    info_standings: Union[Unset, str] = UNSET
    markdown: Union[Unset, str] = UNSET
    show_scores: Union[Unset, bool] = True
    show_rating_diffs: Union[Unset, bool] = True
    team_table: Union[Unset, bool] = False
    visibility: Union[Unset, BroadcastTourCreateBodyVisibility] = BroadcastTourCreateBodyVisibility.PUBLIC
    players: Union[Unset, str] = UNSET
    teams: Union[Unset, str] = UNSET
    tier: Union[Unset, BroadcastTourCreateBodyTier] = UNSET
    tiebreaks: Union[Unset, list[BroadcastTourCreateBodyTiebreaksItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        info_format = self.info_format

        info_location = self.info_location

        info_tc = self.info_tc

        info_fide_tc: Union[Unset, str] = UNSET
        if not isinstance(self.info_fide_tc, Unset):
            info_fide_tc = self.info_fide_tc.value


        info_time_zone = self.info_time_zone

        info_players = self.info_players

        info_website = self.info_website

        info_standings = self.info_standings

        markdown = self.markdown

        show_scores = self.show_scores

        show_rating_diffs = self.show_rating_diffs

        team_table = self.team_table

        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value


        players = self.players

        teams = self.teams

        tier: Union[Unset, int] = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.value


        tiebreaks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tiebreaks, Unset):
            tiebreaks = []
            for tiebreaks_item_data in self.tiebreaks:
                tiebreaks_item = tiebreaks_item_data.value
                tiebreaks.append(tiebreaks_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if info_format is not UNSET:
            field_dict["info.format"] = info_format
        if info_location is not UNSET:
            field_dict["info.location"] = info_location
        if info_tc is not UNSET:
            field_dict["info.tc"] = info_tc
        if info_fide_tc is not UNSET:
            field_dict["info.fideTc"] = info_fide_tc
        if info_time_zone is not UNSET:
            field_dict["info.timeZone"] = info_time_zone
        if info_players is not UNSET:
            field_dict["info.players"] = info_players
        if info_website is not UNSET:
            field_dict["info.website"] = info_website
        if info_standings is not UNSET:
            field_dict["info.standings"] = info_standings
        if markdown is not UNSET:
            field_dict["markdown"] = markdown
        if show_scores is not UNSET:
            field_dict["showScores"] = show_scores
        if show_rating_diffs is not UNSET:
            field_dict["showRatingDiffs"] = show_rating_diffs
        if team_table is not UNSET:
            field_dict["teamTable"] = team_table
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if players is not UNSET:
            field_dict["players"] = players
        if teams is not UNSET:
            field_dict["teams"] = teams
        if tier is not UNSET:
            field_dict["tier"] = tier
        if tiebreaks is not UNSET:
            field_dict["tiebreaks[]"] = tiebreaks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        info_format = d.pop("info.format", UNSET)

        info_location = d.pop("info.location", UNSET)

        info_tc = d.pop("info.tc", UNSET)

        _info_fide_tc = d.pop("info.fideTc", UNSET)
        info_fide_tc: Union[Unset, BroadcastTourCreateBodyInfoFideTc]
        if isinstance(_info_fide_tc,  Unset):
            info_fide_tc = UNSET
        else:
            info_fide_tc = BroadcastTourCreateBodyInfoFideTc(_info_fide_tc)




        info_time_zone = d.pop("info.timeZone", UNSET)

        info_players = d.pop("info.players", UNSET)

        info_website = d.pop("info.website", UNSET)

        info_standings = d.pop("info.standings", UNSET)

        markdown = d.pop("markdown", UNSET)

        show_scores = d.pop("showScores", UNSET)

        show_rating_diffs = d.pop("showRatingDiffs", UNSET)

        team_table = d.pop("teamTable", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, BroadcastTourCreateBodyVisibility]
        if isinstance(_visibility,  Unset):
            visibility = UNSET
        else:
            visibility = BroadcastTourCreateBodyVisibility(_visibility)




        players = d.pop("players", UNSET)

        teams = d.pop("teams", UNSET)

        _tier = d.pop("tier", UNSET)
        tier: Union[Unset, BroadcastTourCreateBodyTier]
        if isinstance(_tier,  Unset):
            tier = UNSET
        else:
            tier = BroadcastTourCreateBodyTier(_tier)




        tiebreaks = []
        _tiebreaks = d.pop("tiebreaks[]", UNSET)
        for tiebreaks_item_data in (_tiebreaks or []):
            tiebreaks_item = BroadcastTourCreateBodyTiebreaksItem(tiebreaks_item_data)



            tiebreaks.append(tiebreaks_item)


        broadcast_tour_create_body = cls(
            name=name,
            info_format=info_format,
            info_location=info_location,
            info_tc=info_tc,
            info_fide_tc=info_fide_tc,
            info_time_zone=info_time_zone,
            info_players=info_players,
            info_website=info_website,
            info_standings=info_standings,
            markdown=markdown,
            show_scores=show_scores,
            show_rating_diffs=show_rating_diffs,
            team_table=team_table,
            visibility=visibility,
            players=players,
            teams=teams,
            tier=tier,
            tiebreaks=tiebreaks,
        )


        broadcast_tour_create_body.additional_properties = d
        return broadcast_tour_create_body

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
