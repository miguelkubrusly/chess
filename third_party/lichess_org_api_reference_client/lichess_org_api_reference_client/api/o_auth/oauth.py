from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Literal, cast
from typing import Union



def _get_kwargs(
    *,
    response_type: Literal['code'],
    client_id: str,
    redirect_uri: str,
    code_challenge_method: Literal['S256'],
    code_challenge: str,
    scope: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["response_type"] = response_type

    params["client_id"] = client_id

    params["redirect_uri"] = redirect_uri

    params["code_challenge_method"] = code_challenge_method

    params["code_challenge"] = code_challenge

    params["scope"] = scope

    params["username"] = username

    params["state"] = state


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/oauth",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    response_type: Literal['code'],
    client_id: str,
    redirect_uri: str,
    code_challenge_method: Literal['S256'],
    code_challenge: str,
    scope: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,

) -> Response[Any]:
    """ Request authorization code

     OAuth2 authorization endpoint.
    Start the OAuth2 Authorization Code Flow with PKCE by securely
    generating two random strings unique to each authorization
    request:

    * `code_verifier`
    * `state`

    Store these in session storage. Make sure not to reveal `code_verifier`
    to eavesdroppers. Do not show it in URLs, do not abuse `state` to store
    it, do not send it over insecure connections. However it is fine if
    the user themselves can extract `code_verifier`, which will always be
    possible for fully client-side apps.
    Then send the user to this endpoint. They will be prompted to grant
    authorization and then be redirected back to the given `redirect_uri`.
    If the authorization failed, the following query string parameters will
    be appended to the redirection:

    * `error`, in particular with value `access_denied` if the user
       cancelled authorization
    * `error_description` to aid debugging
    * `state`, exactly as passed in the `state` parameter

    If the authorization succeeded, the following query string parameters
    will be appended to the redirection:

    * `code`, containing a fresh short-lived authorization code
    * `state`, exactly as passed in the `state` parameter

    Next, to defend against cross site request forgery, check that the
    returned `state` matches the `state` you originally generated.

    Finally, continue by using the authorization code to
    [obtain an access token](#operation/apiToken).

    Args:
        response_type (Literal['code']):
        client_id (str):
        redirect_uri (str):
        code_challenge_method (Literal['S256']):
        code_challenge (str):
        scope (Union[Unset, str]):
        username (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        response_type=response_type,
client_id=client_id,
redirect_uri=redirect_uri,
code_challenge_method=code_challenge_method,
code_challenge=code_challenge,
scope=scope,
username=username,
state=state,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    response_type: Literal['code'],
    client_id: str,
    redirect_uri: str,
    code_challenge_method: Literal['S256'],
    code_challenge: str,
    scope: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,

) -> Response[Any]:
    """ Request authorization code

     OAuth2 authorization endpoint.
    Start the OAuth2 Authorization Code Flow with PKCE by securely
    generating two random strings unique to each authorization
    request:

    * `code_verifier`
    * `state`

    Store these in session storage. Make sure not to reveal `code_verifier`
    to eavesdroppers. Do not show it in URLs, do not abuse `state` to store
    it, do not send it over insecure connections. However it is fine if
    the user themselves can extract `code_verifier`, which will always be
    possible for fully client-side apps.
    Then send the user to this endpoint. They will be prompted to grant
    authorization and then be redirected back to the given `redirect_uri`.
    If the authorization failed, the following query string parameters will
    be appended to the redirection:

    * `error`, in particular with value `access_denied` if the user
       cancelled authorization
    * `error_description` to aid debugging
    * `state`, exactly as passed in the `state` parameter

    If the authorization succeeded, the following query string parameters
    will be appended to the redirection:

    * `code`, containing a fresh short-lived authorization code
    * `state`, exactly as passed in the `state` parameter

    Next, to defend against cross site request forgery, check that the
    returned `state` matches the `state` you originally generated.

    Finally, continue by using the authorization code to
    [obtain an access token](#operation/apiToken).

    Args:
        response_type (Literal['code']):
        client_id (str):
        redirect_uri (str):
        code_challenge_method (Literal['S256']):
        code_challenge (str):
        scope (Union[Unset, str]):
        username (Union[Unset, str]):
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        response_type=response_type,
client_id=client_id,
redirect_uri=redirect_uri,
code_challenge_method=code_challenge_method,
code_challenge=code_challenge,
scope=scope,
username=username,
state=state,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

