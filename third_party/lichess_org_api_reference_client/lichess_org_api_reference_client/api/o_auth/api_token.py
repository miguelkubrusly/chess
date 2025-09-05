from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_token_body import ApiTokenBody
from ...models.api_token_response_200 import ApiTokenResponse200
from ...models.api_token_response_400 import ApiTokenResponse400
from typing import cast



def _get_kwargs(
    *,
    body: ApiTokenBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/token",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ApiTokenResponse200, ApiTokenResponse400]]:
    if response.status_code == 200:
        response_200 = ApiTokenResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ApiTokenResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ApiTokenResponse200, ApiTokenResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiTokenBody,

) -> Response[Union[ApiTokenResponse200, ApiTokenResponse400]]:
    """ Obtain access token

     OAuth2 token endpoint. Exchanges an authorization code for an access token.

    Args:
        body (ApiTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTokenResponse200, ApiTokenResponse400]]
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
    client: Union[AuthenticatedClient, Client],
    body: ApiTokenBody,

) -> Optional[Union[ApiTokenResponse200, ApiTokenResponse400]]:
    """ Obtain access token

     OAuth2 token endpoint. Exchanges an authorization code for an access token.

    Args:
        body (ApiTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTokenResponse200, ApiTokenResponse400]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiTokenBody,

) -> Response[Union[ApiTokenResponse200, ApiTokenResponse400]]:
    """ Obtain access token

     OAuth2 token endpoint. Exchanges an authorization code for an access token.

    Args:
        body (ApiTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTokenResponse200, ApiTokenResponse400]]
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
    client: Union[AuthenticatedClient, Client],
    body: ApiTokenBody,

) -> Optional[Union[ApiTokenResponse200, ApiTokenResponse400]]:
    """ Obtain access token

     OAuth2 token endpoint. Exchanges an authorization code for an access token.

    Args:
        body (ApiTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTokenResponse200, ApiTokenResponse400]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
