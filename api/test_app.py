import pytest
import datetime
from main import app, payout


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_payoutFormula():
    strike = 16
    ex = 24
    notional = 25000
    index = 18
    assert payout(strike, ex, notional, index) == 50000


def test_rainfall_index(client):
    def asString(_date): return _date.strftime("%Y-%m-%d")
    start = asString(datetime.date(2023, 6, 1))
    end = asString(datetime.date(2023, 6, 2))
    response = client.get(f"/rainfall/{start}/{end}")
    assert len(response.json) == 73

def test_calculate_same_month(client):
    def asString(_date): return _date.strftime("%Y-%m-%d")
    start = asString(datetime.date(2023, 6, 1))
    end = asString(datetime.date(2023, 6, 30))

    # these numbers don't make sense
    strike = 16
    exit_ = 24
    notional = 25000
    index = 18

    response = client.get(f"/{start}/{end}/{strike}/{exit_}/{notional}")
    assert type(response.json) == list

def test_calculate_multiple_months(client):
    def asString(_date): return _date.strftime("%Y-%m-%d")
    start = asString(datetime.date(2023, 6, 30))
    end = asString(datetime.date(2023, 7, 1))

    res = client.get(f"/rainfall/{start}/{end}")

    assert False
