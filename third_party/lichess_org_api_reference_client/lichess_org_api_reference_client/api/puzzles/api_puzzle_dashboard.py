from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_puzzle_dashboard_response_200 import ApiPuzzleDashboardResponse200
from typing import cast



def _get_kwargs(
    days: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/puzzle/dashboard/{days}".format(days=days,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiPuzzleDashboardResponse200]:
    if response.status_code == 200:
        response_200 = ApiPuzzleDashboardResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiPuzzleDashboardResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    days: int,
    *,
    client: AuthenticatedClient,

) -> Response[ApiPuzzleDashboardResponse200]:
    """ Get your puzzle dashboard

     Download your [puzzle dashboard](https://lichess.org/training/dashboard/30/dashboard) as JSON.
    Also includes all puzzle themes played, with aggregated results.
    Allows re-creating the
    [improvement/strengths](https://lichess.org/training/dashboard/30/improvementAreas) interfaces.

    Args:
        days (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPuzzleDashboardResponse200]
     """


    kwargs = _get_kwargs(
        days=days,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    days: int,
    *,
    client: AuthenticatedClient,

) -> Optional[ApiPuzzleDashboardResponse200]:
    """ Get your puzzle dashboard

     Download your [puzzle dashboard](https://lichess.org/training/dashboard/30/dashboard) as JSON.
    Also includes all puzzle themes played, with aggregated results.
    Allows re-creating the
    [improvement/strengths](https://lichess.org/training/dashboard/30/improvementAreas) interfaces.

    Args:
        days (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPuzzleDashboardResponse200
     """


    return sync_detailed(
        days=days,
client=client,

    ).parsed

async def asyncio_detailed(
    days: int,
    *,
    client: AuthenticatedClient,

) -> Response[ApiPuzzleDashboardResponse200]:
    """ Get your puzzle dashboard

     Download your [puzzle dashboard](https://lichess.org/training/dashboard/30/dashboard) as JSON.
    Also includes all puzzle themes played, with aggregated results.
    Allows re-creating the
    [improvement/strengths](https://lichess.org/training/dashboard/30/improvementAreas) interfaces.

    Args:
        days (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPuzzleDashboardResponse200]
     """


    kwargs = _get_kwargs(
        days=days,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    days: int,
    *,
    client: AuthenticatedClient,

) -> Optional[ApiPuzzleDashboardResponse200]:
    """ Get your puzzle dashboard

     Download your [puzzle dashboard](https://lichess.org/training/dashboard/30/dashboard) as JSON.
    Also includes all puzzle themes played, with aggregated results.
    Allows re-creating the
    [improvement/strengths](https://lichess.org/training/dashboard/30/improvementAreas) interfaces.

    Args:
        days (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPuzzleDashboardResponse200
     """


    return (await asyncio_detailed(
        days=days,
client=client,

    )).parsed
