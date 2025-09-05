"""Unified Lichess SDK: lightweight client, helpers, and types.

Public API re-exports a small surface for ergonomic imports:

    from lichess_sdk import (
        LichessClient, download_games, create_request,
        HTTPMethod, Headers, Query, PerfType,
        ApiGamesUserColor, ApiGamesUserSort, ApiGamesUserPerfType,
        UNSET, Unset, LichessResponse,
    )
"""

from .client import LichessClient
from .types import HTTPMethod, Headers, Query, PerfType
from .create_request import create_request
from .download_games import download_games

# Re-export selected official types/enums for stable imports within this repo
try:
    from lichess_org_api_reference_client.types import UNSET, Unset, Response as LichessResponse
    from lichess_org_api_reference_client.models.api_games_user_color import ApiGamesUserColor
    from lichess_org_api_reference_client.models.api_games_user_sort import ApiGamesUserSort
    from lichess_org_api_reference_client.models.api_games_user_perf_type import (
        ApiGamesUserPerfType,
    )
except Exception:  # pragma: no cover - optional at runtime
    UNSET = None  # type: ignore
    Unset = object  # type: ignore
    LichessResponse = object  # type: ignore
    ApiGamesUserColor = object  # type: ignore
    ApiGamesUserSort = object  # type: ignore
    ApiGamesUserPerfType = object  # type: ignore

__all__ = [
    "__version__",
    # Local client/types
    "LichessClient",
    "HTTPMethod",
    "Headers",
    "Query",
    "PerfType",
    # Helpers
    "create_request",
    "download_games",
    # Official client types/enums
    "UNSET",
    "Unset",
    "LichessResponse",
    "ApiGamesUserColor",
    "ApiGamesUserSort",
    "ApiGamesUserPerfType",
]

__version__ = "0.2.0"
