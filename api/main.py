import os
import pandas as pd
from dotenv import load_dotenv
from peewee import SqliteDatabase, Model, DateField, FloatField

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

INDEX = 18  # should be the rainfall

database = SqliteDatabase("rain.db")


def payout(strike: float, exit_: float, notional: float) -> float:
    strikeIndex = max(INDEX - strike, 0)
    layer = min(exit_ - strike, strikeIndex)
    return layer * notional


def rainfall_index(start, end):
    pass


if __name__ == '__main__':
    pass
    # create_tables()
