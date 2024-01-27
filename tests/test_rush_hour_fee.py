from calculations import rush_hour_fee
"""
Test the rush_hour_fee function.
This function takes in a time string in ISO format and UTC timezone
and the current fee in cents.

Returns the rush hour fee in cents.
"""


def test_applied_fee():
    # Friday, 3pm, current fee is 710 cents
    assert rush_hour_fee("2024-01-19T15:00:00Z", 710) == 142
    # Friday, 4:59pm, current fee is 1000 cents
    assert rush_hour_fee("2024-01-26T16:59:12Z", 1000) == 200
    # Friday, 3:01pm, current fee is 500 cents
    assert rush_hour_fee("2024-01-19T15:01:00Z", 500) == 100
    # Friday, 6:59pm, current fee is 2000 cents
    assert rush_hour_fee("2024-01-12T18:59:00Z", 2000) == 400
    # Friday, 4:22pm, current fee is 450 cents
    assert rush_hour_fee("2024-01-05T16:22:59Z", 450) == 90


def test_no_fee():
    # Friday, 1pm, current fee is 710 cents
    assert rush_hour_fee("2024-01-15T13:00:00Z", 710) == 0
    # Friday, 7pm, current fee is 200 cents
    assert rush_hour_fee("2024-01-26T19:00:00Z", 200) == 0
    # Friday, 2:59pm, current fee is 10000 cents
    assert rush_hour_fee("2024-01-19T14:59:59Z", 10000) == 0
    # Friday, 7:01pm, current fee is 100 cents
    assert rush_hour_fee("2024-01-12T19:01:00Z", 100) == 0
    # Saturday, 4:59pm, current fee is 20 cents
    assert rush_hour_fee("2024-01-27T16:59:00Z", 20) == 0
    # Monday, 11:34am, current fee is 1000 cents
    assert rush_hour_fee("2024-01-22T11:34:04Z", 1000) == 0
    # Tuesday, 3:30pm, current fee is 500 cents
    assert rush_hour_fee("2024-01-23T15:30:00Z", 500) == 0
    # Thursday, 6:59pm, current fee is 2000 cents
    assert rush_hour_fee("2024-01-25T18:59:00Z", 2000) == 0
