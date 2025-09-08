import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime


def get_lichess_token(env_path: str = "./.env") -> str | None:
    """Retrieve 'LICHESS_API_TOKEN' from .env. Optional for public data."""
    load_dotenv(dotenv_path=env_path)
    return os.getenv("LICHESS_API_TOKEN")


def ensure_directory_exists(path: str) -> None:
    Path(path).expanduser().resolve().mkdir(parents=True, exist_ok=True)


def get_timestamp(format: str = "%Y%m%d_%H%M") -> str:
    return datetime.now().strftime(format)
