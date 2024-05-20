import logging
from pathlib import Path
import os
from riotcrawler.exceptions import ConfigDoesNotExistException
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def get_api_key_env(config_path: Path | str):
    if not os.path.exists(config_path):
        raise ConfigDoesNotExistException(f"Config file {config_path} does not exist.")

    load_dotenv()
    API_KEY = os.getenv(config_path)
    return API_KEY
