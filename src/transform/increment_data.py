import pandas as pd
from pathlib import Path
import numpy as np

RAW_PATH = Path("data/games_2024_raw.csv")
PROCESSED_PATH = Path("data/games_2024_processed.csv")
ML_PATH = Path("data/games_to_ml.csv")


def clean_games():
    df = pd.read_csv(RAW_PATH)

    df = df[["team_abbreviation","game_date","wl","min","pts","fgm","fga","fg_pct","fg3m","fg3a","fg3_pct","ftm","fta","ft_pct"]]
    df["over_100"] = np.where(df["pts"] > 100,"S","N")
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    print(f"Saved processed data to {PROCESSED_PATH}")

def data_to_ml():
    df = pd.read_csv(RAW_PATH)
    df["home_team"] = np.where(df["matchup"].str.contains("@"), df["team_abbreviation"], np.nan)
    df["visitor_team"] = np.where(df["matchup"].str.contains("vs"), df["team_abbreviation"], np.nan)
    df["home_pts"] = np.where(df["matchup"].str.contains("@"), df["pts"], np.nan)
    df["visitor_pts"] = np.where(df["matchup"].str.contains("vs"), df["pts"], np.nan)
    df = df.groupby(["game_id","game_date"]).agg({
        "home_team":"first",
        "visitor_team":"first",
        "home_pts":"first",
        "visitor_pts":"first"
    }).reset_index()
    df = df[["game_date", "home_team", "visitor_team", "home_pts", "visitor_pts"]]
    
    ML_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(ML_PATH, index=False)

    print(f"Saved processed ML data to {ML_PATH}")

if __name__ == "__main__":
    clean_games()
    data_to_ml()