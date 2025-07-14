from config import Config

from typing import Any
import requests
from urllib.parse import urlencode
from enum import Enum

cfg = Config()
RIOT_API_KEY = cfg.get_riot_api_key()


class Continent(Enum):
    americas = "americas"


class Riot:
    def _construct_url(self, endpoint: str, continent: Continent) -> str:
        url = f"https://{continent.value}.api.riotgames.com/{endpoint}"
        print(url)
        return url

    def _call_url(self, url: str) -> Any:
        params = {"api_key": RIOT_API_KEY}
        r = requests.get(url, params=urlencode(params))

        if r.status_code == 200:
            return r.json()

    def get_puuid(self, continent: Continent, game_name: str, tag_line: str) -> str:
        url = self._construct_url(
            endpoint=f"riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}",
            continent=continent,
        )

        puuid = self._call_url(url)["puuid"]

        return puuid

    def get_match_ids(self, continent: Continent, puuid: str) -> list[str]:
        url = self._construct_url(
            endpoint=f"lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=100",
            continent=continent,
        )

        match_ids = self._call_url(url)

        return match_ids
