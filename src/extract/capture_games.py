import pandas as pd
from pathlib import Path
from nba_api.stats.endpoints import leaguegamefinder
import time

OUTPUT_PATH = Path("data/games_2024_raw.csv")

#function to capture nba games of the 2023-24 season
def fetch_games_2024():
    print("Fetching NBA 2024 games from NBA Stats API...")

    gamefinder = leaguegamefinder.LeagueGameFinder(
        season_nullable="2023-24",
        league_id_nullable="00",
        season_type_nullable="Regular Season"
    )

    games = gamefinder.get_data_frames()[0]

    games.columns = games.columns.str.lower()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    games.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved raw data to {OUTPUT_PATH}")


if __name__ == "__main__":
    fetch_games_2024()
    time.sleep(2)
