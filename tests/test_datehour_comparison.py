from task_runner import DateHour

def test_classical_comparison_equal_datehours():
    date_hour_1 = DateHour({'year': '2021', 'month': '12', 'day': '25', 'hours': '0', 'minutes': '0'})
    date_hour_2 = DateHour({'year': '2021', 'month': '12', 'day': '25', 'hours': '0', 'minutes': '0'})
    assert(date_hour_2.time_from(date_hour_1) == 0)

def test_classical_comparison_on_year_change():
    date_hour_1 = DateHour({'year': '2022', 'month': '1', 'day': '1', 'hours': '0', 'minutes': '1'})
    date_hour_2 = DateHour({'year': '2021', 'month': '12', 'day': '31', 'hours': '23', 'minutes': '59'})
    assert(date_hour_2.time_from(date_hour_1) > 0)

def test_classical_comparison_on_month_change():
    date_hour_1 = DateHour({'year': '2020', 'month': '4', 'day': '31', 'hours': '23', 'minutes': '59'})
    date_hour_2 = DateHour({'year': '2020', 'month': '5', 'day': '1', 'hours': '0', 'minutes': '1'})
    assert(date_hour_2.time_from(date_hour_1) > 0)

def test_wildcard_comparison():
    date_hour_1 = DateHour({'year': '2021', 'month': '12', 'day': '5', 'hours': '17', 'minutes': '9'})
    date_hour_2 = DateHour({'year': '*', 'month': '*', 'day': '*', 'hours': '19', 'minutes': '0'})
    assert(date_hour_2.time_from(date_hour_1) > 0)
