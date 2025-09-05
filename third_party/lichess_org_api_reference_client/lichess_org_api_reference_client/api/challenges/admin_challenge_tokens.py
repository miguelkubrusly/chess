from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.admin_challenge_tokens_body import AdminChallengeTokensBody
from ...models.admin_challenge_tokens_response_200 import AdminChallengeTokensResponse200
from ...models.admin_challenge_tokens_response_400 import AdminChallengeTokensResponse400
from typing import cast



def _get_kwargs(
    *,
    body: AdminChallengeTokensBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/token/admin-challenge",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]]:
    if response.status_code == 200:
        response_200 = AdminChallengeTokensResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = AdminChallengeTokensResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AdminChallengeTokensBody,

) -> Response[Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]]:
    """ Admin challenge tokens

     **This endpoint can only be used by Lichess administrators. It will not work if you do not have the
    appropriate permissions.** Tournament organizers should instead use [OAuth](#tag/OAuth) to obtain
    `challenge:write` tokens from users in order to perform bulk pairing.*
    Create and obtain `challenge:write` tokens for multiple users.
    If a similar token already exists for a user, it is reused. This endpoint is idempotent.

    Args:
        body (AdminChallengeTokensBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]]
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
    body: AdminChallengeTokensBody,

) -> Optional[Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]]:
    """ Admin challenge tokens

     **This endpoint can only be used by Lichess administrators. It will not work if you do not have the
    appropriate permissions.** Tournament organizers should instead use [OAuth](#tag/OAuth) to obtain
    `challenge:write` tokens from users in order to perform bulk pairing.*
    Create and obtain `challenge:write` tokens for multiple users.
    If a similar token already exists for a user, it is reused. This endpoint is idempotent.

    Args:
        body (AdminChallengeTokensBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AdminChallengeTokensBody,

) -> Response[Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]]:
    """ Admin challenge tokens

     **This endpoint can only be used by Lichess administrators. It will not work if you do not have the
    appropriate permissions.** Tournament organizers should instead use [OAuth](#tag/OAuth) to obtain
    `challenge:write` tokens from users in order to perform bulk pairing.*
    Create and obtain `challenge:write` tokens for multiple users.
    If a similar token already exists for a user, it is reused. This endpoint is idempotent.

    Args:
        body (AdminChallengeTokensBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]]
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
    body: AdminChallengeTokensBody,

) -> Optional[Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]]:
    """ Admin challenge tokens

     **This endpoint can only be used by Lichess administrators. It will not work if you do not have the
    appropriate permissions.** Tournament organizers should instead use [OAuth](#tag/OAuth) to obtain
    `challenge:write` tokens from users in order to perform bulk pairing.*
    Create and obtain `challenge:write` tokens for multiple users.
    If a similar token already exists for a user, it is reused. This endpoint is idempotent.

    Args:
        body (AdminChallengeTokensBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AdminChallengeTokensResponse200, AdminChallengeTokensResponse400]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
