import os
import logging
import pandas as pd
from peewee import SqliteDatabase, Model, DateField, FloatField

log = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAIN_DATA_FILE = os.path.join(BASE_DIR, "NYC_Rain_Example.xlsx")
database = SqliteDatabase(os.path.join(BASE_DIR, "rain.db"))


class BaseModel(Model):
    class Meta:
        database = database


class RainData(BaseModel):
    date = DateField(null=False, index=True)
    value = FloatField(null=False)


def create_tables():
    # * This script is only run once to create the table and seed the db
    # Todo: Ensure that if this is run multiple times duplicates are not entered.
    try:
        with database:
            database.create_tables([RainData], safe=True)
    except Exception as error:
        log.error(f"An unexpected error occurred during execution:\n{error}")


def seed_tables():
    # * This script is only run once to create the table and seed the db
    # Todo: Ensure that if this is run multiple times duplicates are not entered.
    try:
        create_tables()
        rainDataRaw = pd.read_excel(RAIN_DATA_FILE)
        for index, row in rainDataRaw.iterrows():
            RainData.create(date=row["Date"], value=row["Col1"])
    except FileNotFoundError as file_error:
        log.error(f"Unable to read file: {RAIN_DATA_FILE}")
    except Exception as error:
        log.error(f"An unexpected error occurred during execution:\n{error}")


if __name__ == '__main__':
    create_tables()
    # seed_tables()
    pass
