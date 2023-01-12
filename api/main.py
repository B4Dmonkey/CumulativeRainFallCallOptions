import datetime
from flask import Flask
from flask_cors import CORS
from models import RainData, database
from peewee import fn
import numpy as np
import functools


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
            payout=payout(option_type, float(strike), float(exit_),
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
            avg=np.mean(index_array),
            std=np.std(index_array)
        ),
        payout=dict(
            min=min(payout_array),
            max=max(payout_array),
            avg=np.mean(payout_array),
            std=np.std(payout_array)
        )
    )

    return dict(summary=summary, results=data)


CALL = 'call'
PUT = 'PUT'


def payout(option_type: str, strike: float, exit_: float, notional: float, index: float) -> float:
    # ? Need some kind of defensive coding here just incase we get bad inputs
    if option_type == CALL:
        strikeIndex = max(index - strike, 0)
    elif option_type == PUT:
        strikeIndex = max(strike - index, 0)
    layer = min(exit_ - strike, strikeIndex)
    return layer * notional


def validDates(res, start, end):
    return datetime.date(res.date.year, start.month, start.day) <= res.date <= datetime.date(res.date.year, end.month, end.day)


@app.route('/rainfall/<startDate>/<endDate>', methods=['GET'])
def rainfall_index(startDate: datetime, endDate: datetime):
    start = datetime.datetime.strptime(startDate, "%Y-%m-%d").date()
    end = datetime.datetime.strptime(endDate, "%Y-%m-%d").date()

    # # * Looking at one month only
    # # ? What if we have 2 months or more ?
    if (end.month - start.month == 0):
        queryStartMonth = fn.date_part('month', RainData.date) == start.month
        yearAsCol = fn.date_part('year', RainData.date).alias('year')
        query = (
            RainData
            .select(yearAsCol, fn.SUM(RainData.value))
            .where((queryStartMonth) & (RainData.date.day.between(start.day, end.day)))
            .group_by(yearAsCol)
        )
        return [{'year': data.year, 'index': data.value} for data in query]

    # ToDo: Need to figure out how to do this in an sql statement
    query = RainData.select()
    validDatesPartial = functools.partial(validDates, start=start, end=end)
    filtered_dates = filter(validDatesPartial, query)
    results = {}
    for data in filtered_dates:
        year_exists = results.get(data.date.year)
        if year_exists:
            results.update({data.date.year: year_exists + data.value})
        results.update({data.date.year: data.value})

    return [{'year': data[0], 'index': data[1]} for data in results.items()]


if __name__ == '__main__':
    app.run(debug=True)
