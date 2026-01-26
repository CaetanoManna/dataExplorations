assert (df["away_points"] >= 0).all()
assert (df["home_points"] >= 0).all()
assert (df["away_points"] != df["home_points"]).all()
assert df["game_id"].is_unique
