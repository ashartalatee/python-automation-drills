import pandas as pd
import logging
from datetime import datetime
import os

LOG_PATH = "output/logs.txt"

def setup_logger():
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def load_csv(path):
    setup_logger()
    logging.info(f"Loading CSV: {path}")
    return pd.read_csv(path)

def save_csv(df, path):
    df.to_csv(path, index=False)
    logging.info(f"Saved CSV: {path}")