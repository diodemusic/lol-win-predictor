import riot_api

import json

riot = riot_api.Riot()


def fetch_matches(
    continent: riot_api.Continent,
    game_name: str,
    tag_line: str,
    count: int = 100,
    path: str = "../data/raw",
):
    puuid = riot.get_puuid(continent, game_name, tag_line)
    match_ids = riot.get_match_ids(continent, puuid, count=count)

    for match_id in match_ids:
        match = riot.get_match(continent, match_id)

        with open(f"{path}/{match_id}.json", "w", encoding="utf-8") as f:
            json.dump(match, f)
