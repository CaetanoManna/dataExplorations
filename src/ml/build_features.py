import pandas as pd

def build_features(df):
    df = df.sort_values("game_date").copy()

    # Target
    df["home_win"] = (df["home_pts"] > df["visitor_pts"]).astype(int)
    df["point_diff"] = df["home_pts"] - df["visitor_pts"]

    # Estatísticas históricas por time
    stats = []

    for _, row in df.iterrows():
        date = row["game_date"]

        home = row["home_team"]
        visitor = row["visitor_team"]

        past_games = df[df["game_date"] < date]

        def team_stats(team):
            games = past_games[
                (past_games["home_team"] == team) |
                (past_games["visitor_team"] == team)
            ]

            if games.empty:
                return 0.0, 0.5  # média pts, win rate

            pts_scored = (
                games.loc[games["home_team"] == team, "home_pts"].sum() +
                games.loc[games["visitor_team"] == team, "visitor_pts"].sum()
            ) / len(games)

            wins = (
                (games["home_team"] == team) & (games["home_pts"] > games["visitor_pts"]) |
                (games["visitor_team"] == team) & (games["visitor_pts"] > games["home_pts"])
            ).sum()

            return pts_scored, wins / len(games)

        home_pts_avg, home_winrate = team_stats(home)
        vis_pts_avg, vis_winrate = team_stats(visitor)

        stats.append({
            "home_pts_avg": home_pts_avg,
            "visitor_pts_avg": vis_pts_avg,
            "home_winrate": home_winrate,
            "visitor_winrate": vis_winrate
        })

    stats_df = pd.DataFrame(stats)
    df = pd.concat([df.reset_index(drop=True), stats_df], axis=1)

    # Features finais
    df["pts_avg_diff"] = df["home_pts_avg"] - df["visitor_pts_avg"]
    df["winrate_diff"] = df["home_winrate"] - df["visitor_winrate"]

    features = df[[
        "pts_avg_diff",
        "winrate_diff"
    ]]

    target = df["home_win"]

    return features, target, df
