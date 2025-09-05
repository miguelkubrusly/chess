from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_pairing_create_body import BulkPairingCreateBody
from ...models.bulk_pairing_create_response_200 import BulkPairingCreateResponse200
from ...models.bulk_pairing_create_response_400 import BulkPairingCreateResponse400
from typing import cast



def _get_kwargs(
    *,
    body: BulkPairingCreateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/bulk-pairing",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]]:
    if response.status_code == 200:
        response_200 = BulkPairingCreateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BulkPairingCreateResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkPairingCreateBody,

) -> Response[Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]]:
    """ Create a bulk pairing

     Schedule many games at once, up to 24h in advance.
    OAuth tokens are required for all paired players, with the `challenge:write` scope.
    You can schedule up to 500 games every 10 minutes. [Contact us](mailto:contact@lichess.org) if you
    need higher limits.
    If games have a real-time clock, each player must have only one pairing.
    For correspondence games, players can have multiple pairings within the same bulk.

    **The entire bulk is rejected if:**
      - a token is missing
      - a token is present more than once (except in correspondence)
      - a token lacks the `challenge:write` scope
      - a player account is closed
      - a player is paired more than once (except in correspondence)
      - a bulk is already scheduled to start at the same time with the same player
      - you have 20 scheduled bulks
      - you have 1000 scheduled games

    Partial bulks are never created. Either it all fails, or it all succeeds.
    When it fails, it does so with an error message explaining the issue.
    Failed bulks are not counted in the rate limiting, they are free.
    Fix the issues, manually or programmatically, then retry to schedule the bulk.
    A successful bulk creation returns a JSON bulk document. Its ID can be used for further operations.

    Args:
        body (BulkPairingCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: BulkPairingCreateBody,

) -> Optional[Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]]:
    """ Create a bulk pairing

     Schedule many games at once, up to 24h in advance.
    OAuth tokens are required for all paired players, with the `challenge:write` scope.
    You can schedule up to 500 games every 10 minutes. [Contact us](mailto:contact@lichess.org) if you
    need higher limits.
    If games have a real-time clock, each player must have only one pairing.
    For correspondence games, players can have multiple pairings within the same bulk.

    **The entire bulk is rejected if:**
      - a token is missing
      - a token is present more than once (except in correspondence)
      - a token lacks the `challenge:write` scope
      - a player account is closed
      - a player is paired more than once (except in correspondence)
      - a bulk is already scheduled to start at the same time with the same player
      - you have 20 scheduled bulks
      - you have 1000 scheduled games

    Partial bulks are never created. Either it all fails, or it all succeeds.
    When it fails, it does so with an error message explaining the issue.
    Failed bulks are not counted in the rate limiting, they are free.
    Fix the issues, manually or programmatically, then retry to schedule the bulk.
    A successful bulk creation returns a JSON bulk document. Its ID can be used for further operations.

    Args:
        body (BulkPairingCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkPairingCreateBody,

) -> Response[Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]]:
    """ Create a bulk pairing

     Schedule many games at once, up to 24h in advance.
    OAuth tokens are required for all paired players, with the `challenge:write` scope.
    You can schedule up to 500 games every 10 minutes. [Contact us](mailto:contact@lichess.org) if you
    need higher limits.
    If games have a real-time clock, each player must have only one pairing.
    For correspondence games, players can have multiple pairings within the same bulk.

    **The entire bulk is rejected if:**
      - a token is missing
      - a token is present more than once (except in correspondence)
      - a token lacks the `challenge:write` scope
      - a player account is closed
      - a player is paired more than once (except in correspondence)
      - a bulk is already scheduled to start at the same time with the same player
      - you have 20 scheduled bulks
      - you have 1000 scheduled games

    Partial bulks are never created. Either it all fails, or it all succeeds.
    When it fails, it does so with an error message explaining the issue.
    Failed bulks are not counted in the rate limiting, they are free.
    Fix the issues, manually or programmatically, then retry to schedule the bulk.
    A successful bulk creation returns a JSON bulk document. Its ID can be used for further operations.

    Args:
        body (BulkPairingCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkPairingCreateBody,

) -> Optional[Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]]:
    """ Create a bulk pairing

     Schedule many games at once, up to 24h in advance.
    OAuth tokens are required for all paired players, with the `challenge:write` scope.
    You can schedule up to 500 games every 10 minutes. [Contact us](mailto:contact@lichess.org) if you
    need higher limits.
    If games have a real-time clock, each player must have only one pairing.
    For correspondence games, players can have multiple pairings within the same bulk.

    **The entire bulk is rejected if:**
      - a token is missing
      - a token is present more than once (except in correspondence)
      - a token lacks the `challenge:write` scope
      - a player account is closed
      - a player is paired more than once (except in correspondence)
      - a bulk is already scheduled to start at the same time with the same player
      - you have 20 scheduled bulks
      - you have 1000 scheduled games

    Partial bulks are never created. Either it all fails, or it all succeeds.
    When it fails, it does so with an error message explaining the issue.
    Failed bulks are not counted in the rate limiting, they are free.
    Fix the issues, manually or programmatically, then retry to schedule the bulk.
    A successful bulk creation returns a JSON bulk document. Its ID can be used for further operations.

    Args:
        body (BulkPairingCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkPairingCreateResponse200, BulkPairingCreateResponse400]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
