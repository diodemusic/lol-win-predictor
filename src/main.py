import riot_api

if __name__ == "__main__":
    riot = riot_api.Riot()
    puuid = riot.get_puuid(riot_api.Continent.americas, "McDonaldsManager", "mid")
    match_ids = riot.get_match_ids(riot_api.Continent.americas, puuid)

    for m in match_ids:
        print(m)
