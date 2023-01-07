import os
import pandas as pd
from dotenv import load_dotenv
from peewee import SqliteDatabase, Model, DateField, FloatField

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

INDEX = 18  # should be the rainfall

# database = PostgresqlDatabase(DATABASE_NAME, user=DATABASE_USER)
database = SqliteDatabase("rain.db")


class BaseModel(Model):
    class Meta:
        database = database  # This model uses the "people.db" database.


class RainData(BaseModel):
    date = DateField(null=False, index=True)
    value = FloatField(null=False)

# * This script is only run once to create the table and seed the db
# Todo: Ensure that if this is run multiple times duplicates are not entered.
def create_tables():
    with database:
        database.create_tables([RainData])
        rainDataRaw = pd.read_excel("./NYC_Rain_Example.xlsx")
        for index, row in rainDataRaw.iterrows():
            RainData.create(date=row["Date"], value=row["Col1"])


def payout(strike: float, exit_: float, notional: float):
    strikeIndex = max(INDEX - strike, 0)
    layer = min(exit_ - strike, strikeIndex)
    return layer * notional


def rainfall_index(start, end):
    pass


if __name__ == '__main__':
    pass
    # create_tables()
