import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from build_features import build_features

df = pd.read_csv("data/games_to_ml.csv", parse_dates=["game_date"])

X, y, full_df = build_features(df)

# Split temporal
split_date = "2024-02-01"

train_idx = full_df["game_date"] < split_date
test_idx  = full_df["game_date"] >= split_date

X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_proba))
