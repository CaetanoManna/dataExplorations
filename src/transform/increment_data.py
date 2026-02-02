import pandas as pd
from pathlib import Path
import numpy as np
import sys
import logging

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config import config

# Configurar logging
logger = logging.getLogger(__name__)

RAW_PATH = Path(config.get("paths.data.raw"))
RAW_PATH_PLAYERS = Path(config.get("paths.players.raw"))
PROCESSED_PATH = Path(config.get("paths.data.processed"))
PROCESSED_PATH_PLAYERS = Path(config.get("paths.players.processed"))
ML_PATH = Path(config.get("paths.data.ml"))
ML_PATH_PLAYERS = Path(config.get("paths.players.ml"))


def clean_games():
    df = pd.read_csv(RAW_PATH)

    df = df[["team_abbreviation",
            "game_date",
            "wl",
            "min",
            "pts",
            "fgm",
            "fga",
            "fg_pct",
            "fg3m",
            "fg3a",
            "fg3_pct",
            "ftm",
            "fta",
            "ft_pct"]]

    df["over_100"] = np.where(df["pts"].astype(int) > 100,"S","N")

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    logger.info(f"Saved processed data to {PROCESSED_PATH}")

def data_to_ml():
    df = pd.read_csv(RAW_PATH)

    df["visitor_team"] = np.where(df["matchup"].str.contains("@"), df["team_abbreviation"], np.nan)
    df["home_team"] = np.where(df["matchup"].str.contains("vs"), df["team_abbreviation"], np.nan)
    df["visitor_pts"] = np.where(df["matchup"].str.contains("@"), df["pts"], np.nan)
    df["home_pts"] = np.where(df["matchup"].str.contains("vs"), df["pts"], np.nan)

    df = df.groupby(["game_id","game_date"]).agg({
        "home_team":"first",
        "visitor_team":"first",
        "home_pts":"first",
        "visitor_pts":"first"
    }).reset_index()

    df = df[["game_date", "home_team", "visitor_team", "home_pts", "visitor_pts"]]
    
    ML_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(ML_PATH, index=False)

    logger.info(f"Saved processed ML data to {ML_PATH}")


def clean_player_stats():
    df = pd.read_csv(RAW_PATH_PLAYERS)

    
    df["trat_var"] = np.where(
        df["matchup"].str.contains("@"),
        df["matchup"].str.split("@"),
        df["matchup"].str.split("vs.")
    )
    df["opponent_team"] = df["trat_var"].str.get(1).str.strip()

    df = df[["player_name",
            "fgm",
            "fga",
            "fg_pct",
            "fg3m",
            "fg3a",
            "fg3_pct",
            "ftm",
            "fta",
            "ft_pct",
            "oreb",
            "dreb",
            "reb",
            "ast",
            "stl",
            "blk",
            "tov",
            "pf",
            "pts",
            "opponent_team"]]
    
    PROCESSED_PATH_PLAYERS.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH_PLAYERS, index=False)

    logger.info(f"Saved processed player data to {PROCESSED_PATH_PLAYERS}")

def data_to_ml_players():
    df = pd.read_csv(PROCESSED_PATH_PLAYERS)

    df = df.groupby(["player_name","opponent_team"]).agg({
        "pts":"mean",
        "ast":"mean",
        "reb":"mean",
        "stl":"mean",
        "blk":"mean"
    }).reset_index()
    
    df["best_vs"] = df.groupby("player_name")["pts"].rank(ascending=False, method="first")
    df["worst_vs"] = df.groupby("player_name")["pts"].rank(ascending=True, method="first")
    ML_PATH_PLAYERS.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(ML_PATH_PLAYERS, index=False)
    
    
    logger.info(f"Saved processed ML player data to {ML_PATH_PLAYERS}")