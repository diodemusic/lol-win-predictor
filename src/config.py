from dotenv import load_dotenv
import os
from sys import exit
from enum import Enum


class EnvVarNotFound(Exception):
    def __str__(self):
        return "Enviroment variable not found."


class Secret(Enum):
    # discord_token = "DISCORD_TOKEN"
    riot_api_key = "RIOT_API_KEY"


class Config:
    def __init__(self):
        load_dotenv()

    def _get_secret(self, secret: Secret):
        SECRET = os.getenv(secret.value)

        if not SECRET:
            raise EnvVarNotFound

        return SECRET

    # def get_discord_token(self):
    #     secret = _keys.discord_token.value

    #     try:
    #         return self._get_token(secret)
    #     except EnvVarNotFound as e:
    #         print(f"Error getting {secret}: {e}")
    #         exit(1)

    def get_riot_api_key(self):
        secret = Secret.riot_api_key

        try:
            return self._get_secret(secret)
        except EnvVarNotFound as e:
            print(f"Error getting {secret}: {e}")
            exit(1)
