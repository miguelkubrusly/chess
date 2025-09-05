from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_swiss_schedule_next_round_body import ApiSwissScheduleNextRoundBody
from ...models.api_swiss_schedule_next_round_response_400 import ApiSwissScheduleNextRoundResponse400
from ...models.api_swiss_schedule_next_round_response_401 import ApiSwissScheduleNextRoundResponse401
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: ApiSwissScheduleNextRoundBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/swiss/{id}/schedule-next-round".format(id=id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ApiSwissScheduleNextRoundResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ApiSwissScheduleNextRoundResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiSwissScheduleNextRoundBody,

) -> Response[Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]]:
    """ Manually schedule the next round

     Manually schedule the next round date and time of a Swiss tournament.
    This sets the `roundInterval` field to `99999999`, i.e. manual scheduling.
    All further rounds will need to be manually scheduled, unless the `roundInterval` field is changed
    back to automatic scheduling.

    Args:
        id (str):  Example: hL7vMrFQ.
        body (ApiSwissScheduleNextRoundBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiSwissScheduleNextRoundBody,

) -> Optional[Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]]:
    """ Manually schedule the next round

     Manually schedule the next round date and time of a Swiss tournament.
    This sets the `roundInterval` field to `99999999`, i.e. manual scheduling.
    All further rounds will need to be manually scheduled, unless the `roundInterval` field is changed
    back to automatic scheduling.

    Args:
        id (str):  Example: hL7vMrFQ.
        body (ApiSwissScheduleNextRoundBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiSwissScheduleNextRoundBody,

) -> Response[Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]]:
    """ Manually schedule the next round

     Manually schedule the next round date and time of a Swiss tournament.
    This sets the `roundInterval` field to `99999999`, i.e. manual scheduling.
    All further rounds will need to be manually scheduled, unless the `roundInterval` field is changed
    back to automatic scheduling.

    Args:
        id (str):  Example: hL7vMrFQ.
        body (ApiSwissScheduleNextRoundBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiSwissScheduleNextRoundBody,

) -> Optional[Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]]:
    """ Manually schedule the next round

     Manually schedule the next round date and time of a Swiss tournament.
    This sets the `roundInterval` field to `99999999`, i.e. manual scheduling.
    All further rounds will need to be manually scheduled, unless the `roundInterval` field is changed
    back to automatic scheduling.

    Args:
        id (str):  Example: hL7vMrFQ.
        body (ApiSwissScheduleNextRoundBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiSwissScheduleNextRoundResponse400, ApiSwissScheduleNextRoundResponse401]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
