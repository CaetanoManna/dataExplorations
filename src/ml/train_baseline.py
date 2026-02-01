import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from pathlib import Path
import sys
import logging

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from build_features import build_features
from config import config

# Configurar logging
logger = logging.getLogger(__name__)

def  main():
    df = pd.read_csv(config.get("paths.data.ml"), parse_dates=["game_date"])

    X, y, full_df = build_features(df)

    # Split temporal
    split_date = config.get("model.split_date")

    train_idx = full_df["game_date"] < split_date
    test_idx  = full_df["game_date"] >= split_date

    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    max_iterations = config.get("model.max_iterations")
    random_state = config.get("model.random_state")

    model = LogisticRegression(max_iter=max_iterations, random_state=random_state)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_proba)

    logger.info(f"Accuracy: {accuracy:.4f}")
    logger.info(f"ROC AUC: {roc_auc:.4f}")

    print(f"Accuracy: {accuracy:.4f}")
    print(f"ROC AUC: {roc_auc:.4f}")
