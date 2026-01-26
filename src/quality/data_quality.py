import pandera as pa
from pandera import Column, DataFrameSchema, Check
import great_expectations as gx
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config import config

# Configurar logging
logger = logging.getLogger(__name__)


def valid_schema_ml():
    schema = DataFrameSchema({
        "game_date": Column(pa.DateTime),
        "home_team": Column(str),
        "visitor_team": Column(str),
        "home_pts": Column(int, Check.ge(0)),
        "visitor_pts": Column(int, Check.ge(0))
    })
    return schema

def valid_data_ml(df):
    df_ge = gx.from_pandas(df)

    df_ge.expect_column_values_to_not_be_null("game_date")
    df_ge.expect_column_values_to_be_between("home_pts", 0, 200)
    df_ge.expect_column_values_to_be_between("visitor_pts", 0, 200)
    return df_ge
