import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime


def get_api_key(env_path: str = "./.env") -> None | str:
    """Retrieve a generic 'api_key' from .env (used in some endpoints)."""
    load_dotenv(dotenv_path=env_path)
    api_key: str | None = os.getenv("api_key")
    if api_key is None:
        print("api_key não encontrada.")
    return api_key


def get_lichess_token(env_path: str = "./.env") -> None | str:
    """Retrieve 'LICHESS_API_TOKEN' from .env. Optional for public data."""
    load_dotenv(dotenv_path=env_path)
    token: str | None = os.getenv("LICHESS_API_TOKEN")
    if token is None:
        print("LICHESS_API_TOKEN não encontrado (opcional para jogos públicos).")
    return token


def ensure_directory_exists(path: str) -> None:
    Path(path).expanduser().resolve().mkdir(parents=True, exist_ok=True)


def get_timestamp(format: str = "%Y%m%d_%H%M") -> str:
    return datetime.now().strftime(format)

