from __future__ import annotations

from typing import Literal, Mapping, TypedDict, NotRequired
from enum import Enum
from lichess_org_api_reference_client.models.api_games_user_color import ApiGamesUserColor
from lichess_org_api_reference_client.models.api_games_user_sort import ApiGamesUserSort


# HTTP typing primitives
HTTPMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
Headers = Mapping[str, str]
Query = Mapping[str, object]


class PerfType(str, Enum):
    """Lichess performance types for filtering game exports."""

    ULTRABULLET = "ultraBullet"
    BULLET = "bullet"
    BLITZ = "blitz"
    RAPID = "rapid"
    CLASSICAL = "classical"
    CORRESPONDENCE = "correspondence"

    CRAZYHOUSE = "crazyhouse"
    CHESS960 = "chess960"
    KING_OF_THE_HILL = "kingOfTheHill"
    THREE_CHECK = "threeCheck"
    ANTICHESS = "antichess"
    ATOMIC = "atomic"
    HORDE = "horde"
    RACING_KINGS = "racingKings"


# NDJSON types used by download helpers
class PlayerUser(TypedDict, total=False):
    id: str
    name: str
    title: NotRequired[str]
    patron: NotRequired[bool]


class PlayerAnalysis(TypedDict, total=False):
    inaccuracy: NotRequired[int]
    mistake: NotRequired[int]
    blunder: NotRequired[int]
    acpl: NotRequired[int]
    accuracy: NotRequired[int]


class PlayerSide(TypedDict, total=False):
    user: NotRequired[PlayerUser]
    rating: NotRequired[int]
    ratingDiff: NotRequired[int]
    analysis: NotRequired[PlayerAnalysis]


class Players(TypedDict):
    white: PlayerSide
    black: PlayerSide


class Opening(TypedDict, total=False):
    eco: NotRequired[str]
    name: NotRequired[str]
    ply: NotRequired[int]


class Judgment(TypedDict, total=False):
    name: NotRequired[str]  # Inaccuracy|Mistake|Blunder
    comment: NotRequired[str]


class AnalysisPly(TypedDict, total=False):
    eval: NotRequired[int]
    best: NotRequired[str]
    variation: NotRequired[str]
    judgment: NotRequired[Judgment]


class Clock(TypedDict, total=False):
    initial: NotRequired[int]
    increment: NotRequired[int]
    totalTime: NotRequired[int]


class Division(TypedDict, total=False):
    middle: NotRequired[int]
    end: NotRequired[int]


Status = Literal[
    "mate",
    "resign",
    "draw",
    "stalemate",
    "timeout",
    "aborted",
    "outoftime",
    "cheat",
    "noStart",
    "unknown",
]


class NdjsonGame(TypedDict, total=False):
    id: str
    rated: bool
    variant: str
    speed: str
    perf: str
    createdAt: int
    lastMoveAt: int
    status: Status | str
    source: NotRequired[str]
    players: Players
    winner: NotRequired[Literal["white", "black"]]
    opening: NotRequired[Opening]
    moves: NotRequired[str]
    analysis: NotRequired[list[AnalysisPly]]
    tournament: NotRequired[str]
    clock: NotRequired[Clock]
    division: NotRequired[Division]


class DownloadParams(TypedDict, total=False):
    max: int
    since: int
    until: int
    rated: bool
    perfType: PerfType
    color: ApiGamesUserColor
    vs: str
    analysed: bool
    ongoing: bool
    finished: bool
    sort: ApiGamesUserSort
    moves: bool
    tags: bool
    clocks: bool
    evals: bool
    opening: bool
    accuracy: bool
    lastFen: bool
