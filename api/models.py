from main import database
from peewee import Model, DateField, FloatField


class BaseModel(Model):
    class Meta:
        database = database


class RainData(BaseModel):
    date = DateField(null=False, index=True)
    value = FloatField(null=False)


def create_tables():
    # * This script is only run once to create the table and seed the db
    # Todo: Ensure that if this is run multiple times duplicates are not entered.
    with database:
        database.create_tables([RainData])
        rainDataRaw = pd.read_excel("./NYC_Rain_Example.xlsx")
        for index, row in rainDataRaw.iterrows():
            RainData.create(date=row["Date"], value=row["Col1"])


if __name__ == '__main__':
    # create_tables()
    pass
