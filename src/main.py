from fetch_matches import fetch_matches
import riot_api

if __name__ == "__main__":
    fetch_matches(riot_api.Continent.americas, "McDonaldsManager", "mid")
