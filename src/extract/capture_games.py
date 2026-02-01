import pandas as pd
from pathlib import Path
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import LeagueGameLog
import time
import sys
import logging

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config import config

# Configurar logging
logger = logging.getLogger(__name__)

OUTPUT_PATH = Path(config.get("paths.data.raw"))
OUTPUT_PATH_PLAYERS = Path(config.get("paths.players.raw"))

#function to capture nba games of the 2023-24 season
def fetch_games_2024():
    logger.info("Fetching NBA 2024 games from NBA Stats API...")

    season = config.get("nba_api.season")
    league_id = config.get("nba_api.league_id")
    season_type = config.get("nba_api.season_type")

    gamefinder = leaguegamefinder.LeagueGameFinder(
        season_nullable=season,
        league_id_nullable=league_id,
        season_type_nullable=season_type
    )

    games = gamefinder.get_data_frames()[0]

    games.columns = games.columns.str.lower()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    games.to_csv(OUTPUT_PATH, index=False)

    logger.info(f"Saved raw data to {OUTPUT_PATH}")

def capture_players():
    from nba_api.stats.endpoints import LeagueGameLog

    gamelog = LeagueGameLog(
        season="2023-24",
        season_type_all_star="Regular Season",
        player_or_team_abbreviation="P"
    )

    df = gamelog.get_data_frames()[0]

    df.columns = df.columns.str.lower()

    OUTPUT_PATH_PLAYERS.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH_PLAYERS, index=False)

    logger.info(f"Saved raw players to {OUTPUT_PATH_PLAYERS}")

