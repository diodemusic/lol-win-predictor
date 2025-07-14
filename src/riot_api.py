from config import Config

from typing import Any
import requests
from urllib.parse import urlencode
from enum import Enum

cfg = Config()
RIOT_API_KEY = cfg.get_riot_api_key()


class Region(Enum):
    # TODO
    pass


class Riot:
    def _construct_continent_url(self, endpoint: str) -> str:
        return f"https://europe.api.riotgames.com/riot/{endpoint}"

    def _construct_region_url(self, endpoint: str, region: Region) -> str:
        return f"https://{region}.api.riotgames.com/riot/{endpoint}"

    def _call_url(self, url: str) -> Any:
        params = {"api_key": RIOT_API_KEY}
        r = requests.get(url, params=urlencode(params))

        if r.status_code == 200:
            return r.json()

    def get_puuid(self, game_name: str, tag_line: str) -> str:
        url = self._construct_continent_url(
            endpoint=f"account/v1/accounts/by-riot-id/{game_name}/{tag_line}",
        )

        puuid = self._call_url(url)["puuid"]
        return puuid
