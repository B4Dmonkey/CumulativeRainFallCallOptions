from models import RainData, database
from peewee import fn
import datetime
# @app.before_request


def before_request():
    database.connect()

# @app.after_request


def after_request(response=None):
    database.close()
    return response


def payout(strike: float, exit_: float, notional: float) -> float:
    INDEX = 18  # should be the rainfall
    strikeIndex = max(INDEX - strike, 0)
    layer = min(exit_ - strike, strikeIndex)
    return layer * notional


def rainfall_index(start: datetime, end: datetime):
    # Select all dates between month and between days
    before_request()  # !should be handled by flask
    database.create_tables([RainData], safe=True)

    queryStartMonth = fn.date_part('month', RainData.date) == start.month

    yearAsCol = fn.date_part('year', RainData.date).alias('year')
    dayAsCol = fn.date_part('day', RainData.date).alias('day')

    # * Looking at one month only
    # ? What if we have 2 months or more ?
    if (end.month - start.month == 0):
        query = (
            RainData
              .select(yearAsCol, fn.SUM(RainData.value))
              .where((queryStartMonth) & (RainData.date.day.between(start.day, end.day)))
              .group_by(yearAsCol)
        )

    # queryStartMonth = fn.date_part('month', RainData.date) == 6
    # queryEndMonth = fn.date_part('month', RainData.date) <= 6

    # yearAsCol = fn.date_part('year', RainData.date).alias('year')
    # monthAsCol = fn.date_part('month', RainData.date).alias('month')

    # mdASCol = fn.date_part('monthday', RainData.date).alias('md')
    # RainData.select(monthAsCol, dayAsCol, yearAsCol, RainData.value)

    for data in query:
        print(f"Year: {data.year} Value: {data.value}")
        # print(data)
    # * Get the year
    for data in RainData.select().where((RainData.date.month.between(start.month, end.month)) & (RainData.date.day.between(start.day, end.day))):
        print(f"Date: {data.date} Value: {data.value}")
        x = 1
    months = RainData.select().where((RainData.date.month >= start.month)
                                     & (RainData.date.month <= end.month))
    # [r for r in RainData.select().where( (RainData.date.month >= 6) & (RainData.date.month <= 6) )]
    query = []
    # query = RainData \
    #           .select() \
    #           .where(
    #             RainData.date.between(
    #               (fn.date_part('month', RainData.date) == 6),
    #               (fn.date_part('month', RainData.date) == 6)
    #             )
    #           )

    # RainData.select().where(fn.date_part('year', RainData.date) == 2022)
    for data in query:
        print(data)
        break
    after_request()  # ! should be handled by flask
    pass


if __name__ == '__main__':
    pass
    # create_tables()
