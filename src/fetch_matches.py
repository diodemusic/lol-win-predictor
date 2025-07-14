import riot_api

riot = riot_api.Riot()

puuid = riot.get_puuid(riot_api.Continent.americas, "McDonaldsManager", "mid")
match_ids = riot.get_match_ids(riot_api.Continent.americas, puuid)
match = riot.get_match(riot_api.Continent.americas, match_ids[0])

print(match)
