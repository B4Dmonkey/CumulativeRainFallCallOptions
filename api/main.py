import datetime
import logging
from flask import Flask, request
from flask_cors import CORS
from models import RainData, database
from peewee import fn


def create_app():
    app = Flask(__name__)
    return app


# app = Flask(__name__)
app = create_app()
log = app.logger
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.before_request
def before_request():
    database.connect()


@app.after_request
def after_request(response=None):
    database.close()
    return response


def payout(strike: float, exit_: float, notional: float) -> float:
    INDEX = 18  # should be the rainfall
    strikeIndex = max(INDEX - strike, 0)
    layer = min(exit_ - strike, strikeIndex)
    return layer * notional


@app.route('/rainfall/<startDate>/<endDate>', methods=['GET'])
# def rainfall_index():
def rainfall_index(startDate: datetime, endDate: datetime):
    start = datetime.datetime.strptime(startDate, "%Y-%m-%d").date()
    end = datetime.datetime.strptime(endDate, "%Y-%m-%d").date()
    # Select all dates between month and between days
    # database.create_tables([RainData], safe=True)

    queryStartMonth = fn.date_part('month', RainData.date) == start.month
    yearAsCol = fn.date_part('year', RainData.date).alias('year')
    dayAsCol = fn.date_part('day', RainData.date).alias('day')

    # # * Looking at one month only
    # # ? What if we have 2 months or more ?
    if (end.month - start.month == 0):
        query = (
            RainData
            .select(yearAsCol, fn.SUM(RainData.value))
            .where((queryStartMonth) & (RainData.date.day.between(start.day, end.day)))
            .group_by(yearAsCol)
        )
    return {data.year:data.value for data in query}
    # queryStartMonth = fn.date_part('month', RainData.date) == 6
    # queryEndMonth = fn.date_part('month', RainData.date) <= 6

    # yearAsCol = fn.date_part('year', RainData.date).alias('year')
    # monthAsCol = fn.date_part('month', RainData.date).alias('month')

    # mdASCol = fn.date_part('monthday', RainData.date).alias('md')
    # RainData.select(monthAsCol, dayAsCol, yearAsCol, RainData.value)

    # for data in query:
    #     log.info(f"Year: {data.year} Value: {data.value}")
        # print(data)
    # * Get the year
    # for data in RainData.select().where((RainData.date.month.between(start.month, end.month)) & (RainData.date.day.between(start.day, end.day))):
    #     print(f"Date: {data.date} Value: {data.value}")
    #     x = 1
    # months = RainData.select().where((RainData.date.month >= start.month)
        #  & (RainData.date.month <= end.month))
    # [r for r in RainData.select().where( (RainData.date.month >= 6) & (RainData.date.month <= 6) )]
    # query = []
    # query = RainData \
    #           .select() \
    #           .where(
    #             RainData.date.between(
    #               (fn.date_part('month', RainData.date) == 6),
    #               (fn.date_part('month', RainData.date) == 6)
    #             )
    #           )

    # RainData.select().where(fn.date_part('year', RainData.date) == 2022)
    # Todo: Return as dict to send back as a json
    # return "Hello, rainfall!"


if __name__ == '__main__':
    app.run(debug=True)
