from dotenv import load_dotenv
import os
import requests
import urllib
import datetime
import logging
from riotcrawler.config import get_api_key_env

logger = logging.getLogger(__name__)


x = get_api_key_env("RIOT_API_KEY")
print(x)
