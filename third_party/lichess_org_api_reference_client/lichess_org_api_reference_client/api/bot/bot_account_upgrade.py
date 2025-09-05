from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bot_account_upgrade_response_200 import BotAccountUpgradeResponse200
from ...models.bot_account_upgrade_response_400 import BotAccountUpgradeResponse400
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/bot/account/upgrade",
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]]:
    if response.status_code == 200:
        response_200 = BotAccountUpgradeResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BotAccountUpgradeResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]]:
    r""" Upgrade to Bot account

     Upgrade a lichess player account into a Bot account. Only Bot accounts can use the Bot API.
    The account **cannot have played any game** before becoming a Bot account. The upgrade is
    **irreversible**. The account will only be able to play as a Bot.
    To upgrade an account to Bot, use the [official lichess-bot client](https://github.com/lichess-bot-
    devs/lichess-bot), or follow these steps:
    - Create an [API access token](https://lichess.org/account/oauth/token/create?scopes[]=bot:play)
    with \"Play bot moves\" permission.
    - `curl -d '' https://lichess.org/api/bot/account/upgrade -H \"Authorization: Bearer
    <yourTokenHere>\"`
    To know if an account has already been upgraded, use the [Get my profile API](#operation/accountMe):
    the `title` field should be set to `BOT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Optional[Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]]:
    r""" Upgrade to Bot account

     Upgrade a lichess player account into a Bot account. Only Bot accounts can use the Bot API.
    The account **cannot have played any game** before becoming a Bot account. The upgrade is
    **irreversible**. The account will only be able to play as a Bot.
    To upgrade an account to Bot, use the [official lichess-bot client](https://github.com/lichess-bot-
    devs/lichess-bot), or follow these steps:
    - Create an [API access token](https://lichess.org/account/oauth/token/create?scopes[]=bot:play)
    with \"Play bot moves\" permission.
    - `curl -d '' https://lichess.org/api/bot/account/upgrade -H \"Authorization: Bearer
    <yourTokenHere>\"`
    To know if an account has already been upgraded, use the [Get my profile API](#operation/accountMe):
    the `title` field should be set to `BOT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]]:
    r""" Upgrade to Bot account

     Upgrade a lichess player account into a Bot account. Only Bot accounts can use the Bot API.
    The account **cannot have played any game** before becoming a Bot account. The upgrade is
    **irreversible**. The account will only be able to play as a Bot.
    To upgrade an account to Bot, use the [official lichess-bot client](https://github.com/lichess-bot-
    devs/lichess-bot), or follow these steps:
    - Create an [API access token](https://lichess.org/account/oauth/token/create?scopes[]=bot:play)
    with \"Play bot moves\" permission.
    - `curl -d '' https://lichess.org/api/bot/account/upgrade -H \"Authorization: Bearer
    <yourTokenHere>\"`
    To know if an account has already been upgraded, use the [Get my profile API](#operation/accountMe):
    the `title` field should be set to `BOT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Optional[Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]]:
    r""" Upgrade to Bot account

     Upgrade a lichess player account into a Bot account. Only Bot accounts can use the Bot API.
    The account **cannot have played any game** before becoming a Bot account. The upgrade is
    **irreversible**. The account will only be able to play as a Bot.
    To upgrade an account to Bot, use the [official lichess-bot client](https://github.com/lichess-bot-
    devs/lichess-bot), or follow these steps:
    - Create an [API access token](https://lichess.org/account/oauth/token/create?scopes[]=bot:play)
    with \"Play bot moves\" permission.
    - `curl -d '' https://lichess.org/api/bot/account/upgrade -H \"Authorization: Bearer
    <yourTokenHere>\"`
    To know if an account has already been upgraded, use the [Get my profile API](#operation/accountMe):
    the `title` field should be set to `BOT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BotAccountUpgradeResponse200, BotAccountUpgradeResponse400]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
