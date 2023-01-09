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
    assert payout(strike, ex, notional) == 50000


def test_rainfall_index(client):
    def asString(_date): return _date.strftime("%Y-%m-%d")
    start = asString(datetime.date(2023, 6, 1))
    end = asString(datetime.date(2023, 6, 2))
    response = client.get(f"/rainfall/{start}/{end}")
    assert len(response.json) == 73
