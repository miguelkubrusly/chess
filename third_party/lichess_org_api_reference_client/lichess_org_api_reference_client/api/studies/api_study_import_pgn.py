from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_study_import_pgn_body import ApiStudyImportPGNBody
from ...models.api_study_import_pgn_response_200 import ApiStudyImportPGNResponse200
from ...models.api_study_import_pgn_response_400 import ApiStudyImportPGNResponse400
from typing import cast



def _get_kwargs(
    study_id: str,
    *,
    body: ApiStudyImportPGNBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/study/{study_id}/import-pgn".format(study_id=study_id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]]:
    if response.status_code == 200:
        response_200 = ApiStudyImportPGNResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ApiStudyImportPGNResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    study_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiStudyImportPGNBody,

) -> Response[Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]]:
    """ Import PGN into a study

     Imports arbitrary PGN into an existing [study](https://lichess.org/study). Creates a new chapter in
    the study.
    If the PGN contains multiple games (separated by 2 or more newlines)
    then multiple chapters will be created within the study.
    Note that a study can contain at most 64 chapters.

    Args:
        study_id (str):
        body (ApiStudyImportPGNBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]]
     """


    kwargs = _get_kwargs(
        study_id=study_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    study_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiStudyImportPGNBody,

) -> Optional[Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]]:
    """ Import PGN into a study

     Imports arbitrary PGN into an existing [study](https://lichess.org/study). Creates a new chapter in
    the study.
    If the PGN contains multiple games (separated by 2 or more newlines)
    then multiple chapters will be created within the study.
    Note that a study can contain at most 64 chapters.

    Args:
        study_id (str):
        body (ApiStudyImportPGNBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]
     """


    return sync_detailed(
        study_id=study_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    study_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiStudyImportPGNBody,

) -> Response[Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]]:
    """ Import PGN into a study

     Imports arbitrary PGN into an existing [study](https://lichess.org/study). Creates a new chapter in
    the study.
    If the PGN contains multiple games (separated by 2 or more newlines)
    then multiple chapters will be created within the study.
    Note that a study can contain at most 64 chapters.

    Args:
        study_id (str):
        body (ApiStudyImportPGNBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]]
     """


    kwargs = _get_kwargs(
        study_id=study_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    study_id: str,
    *,
    client: AuthenticatedClient,
    body: ApiStudyImportPGNBody,

) -> Optional[Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]]:
    """ Import PGN into a study

     Imports arbitrary PGN into an existing [study](https://lichess.org/study). Creates a new chapter in
    the study.
    If the PGN contains multiple games (separated by 2 or more newlines)
    then multiple chapters will be created within the study.
    Note that a study can contain at most 64 chapters.

    Args:
        study_id (str):
        body (ApiStudyImportPGNBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiStudyImportPGNResponse200, ApiStudyImportPGNResponse400]
     """


    return (await asyncio_detailed(
        study_id=study_id,
client=client,
body=body,

    )).parsed
