import pytest
import datetime
from main import app, payout


""" @pytest.fixture()
def app():
    app = create_app() # ? Might consider moving to a factory when doing a full scale app
    app.config.update({
        "TESTING": True,
        "DEBUG": True
    })

    # other setup can go here

    yield app

    # clean up / reset resources here
"""

@pytest.fixture()
def client():
  with app.test_client() as client:
        yield client
    # return app.test_client()


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()


def test_payoutFormula():
    strike = 16
    ex = 24
    notional = 25000
    assert payout(strike, ex, notional) == 50000


# def test_request_example(client):
#     response = client.get("/posts")
#     assert b"<h2>Hello, World!</h2>" in response.data

def test_rainfall_index(client):
    asString = lambda _date: _date.strftime("%Y-%m-%d")
    start = asString(datetime.date(2022, 6, 1))
    end = asString(datetime.date(2022, 6, 2))
    # response = client.get(f"/rainfall/{start}/{end}")
    response = client.get('/rainfall/2022-06-01/2022-06-02')

    assert False

