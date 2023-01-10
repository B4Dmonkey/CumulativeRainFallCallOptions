import datetime
import logging
from flask import Flask, request
from flask_cors import CORS
from models import RainData, database
from peewee import fn
import numpy as np


app = Flask(__name__)
log = app.logger
CORS(app, origins="*")


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


@app.route("/<option_type>/<startDate>/<endDate>/<strike>/<exit_>/<notional>", methods=['GET'])
def calculate(option_type: str, startDate: datetime, endDate: datetime, strike: float, exit_: float, notional: float):
    index = rainfall_index(startDate, endDate)
    data = [
        dict(
            year=i['year'],
            index=i['index'],
            payout=payout(float(strike), float(exit_),
                          float(notional), i['index'])
        )
        for i in index
    ]

    index_array = [i['index'] for i in data]
    payout_array = [p['payout'] for p in data]

    summary = dict(
        index=dict(
            min=min(index_array),
            max=max(index_array),
            average=np.mean(index_array),
            std=np.std(index_array)
        ),
        payout=dict(
            min=min(payout_array),
            max=max(payout_array),
            average=np.mean(payout_array),
            std=np.std(payout_array)
        )
    )

    return dict(summary=summary, results=data)


def payout(strike: float, exit_: float, notional: float, index: float) -> float:
    # todo need to account for call vs put
    strikeIndex = max(index - strike, 0)
    layer = min(exit_ - strike, strikeIndex)
    return layer * notional


@app.route('/rainfall/<startDate>/<endDate>', methods=['GET'])
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
    return [{'year': data.year, 'index': data.value} for data in query]
    # return [{'key': data.year, 'value':data.value} for data in query]
    # return {data.year: data.value for data in query}
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
