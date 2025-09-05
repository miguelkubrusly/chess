from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_simul_response_200 import ApiSimulResponse200
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/simul",
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiSimulResponse200]:
    if response.status_code == 200:
        response_200 = ApiSimulResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiSimulResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[ApiSimulResponse200]:
    """ Get current simuls

     Get recently created, started, finished, simuls.
    Created and finished simul lists are not exhaustives, only those with
    strong enough host will be listed, the same filter is used to display simuls on
    https://lichess.org/simul.
    When [authenticated with OAuth2](#section/Introduction/Authentication), the pending list will be
    populated with your created, but unstarted simuls.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSimulResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[ApiSimulResponse200]:
    """ Get current simuls

     Get recently created, started, finished, simuls.
    Created and finished simul lists are not exhaustives, only those with
    strong enough host will be listed, the same filter is used to display simuls on
    https://lichess.org/simul.
    When [authenticated with OAuth2](#section/Introduction/Authentication), the pending list will be
    populated with your created, but unstarted simuls.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSimulResponse200
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[ApiSimulResponse200]:
    """ Get current simuls

     Get recently created, started, finished, simuls.
    Created and finished simul lists are not exhaustives, only those with
    strong enough host will be listed, the same filter is used to display simuls on
    https://lichess.org/simul.
    When [authenticated with OAuth2](#section/Introduction/Authentication), the pending list will be
    populated with your created, but unstarted simuls.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSimulResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[ApiSimulResponse200]:
    """ Get current simuls

     Get recently created, started, finished, simuls.
    Created and finished simul lists are not exhaustives, only those with
    strong enough host will be listed, the same filter is used to display simuls on
    https://lichess.org/simul.
    When [authenticated with OAuth2](#section/Introduction/Authentication), the pending list will be
    populated with your created, but unstarted simuls.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSimulResponse200
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
