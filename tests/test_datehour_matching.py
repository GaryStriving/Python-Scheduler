from src.task_runner import DateHour

def test_classical_matching_matches():
    date_hour_1 = DateHour({'year': '2021', 'month': '12', 'day': '25', 'hours': '0', 'minutes': '0'})
    date_hour_2 = DateHour({'year': '2021', 'month': '12', 'day': '25', 'hours': '0', 'minutes': '0'})
    assert(date_hour_2.matches(date_hour_1))

def test_classical_not_matches():
    date_hour_1 = DateHour({'year': '2021', 'month': '12', 'day': '25', 'hours': '0', 'minutes': '1'})
    date_hour_2 = DateHour({'year': '2021', 'month': '12', 'day': '25', 'hours': '0', 'minutes': '0'})
    assert(not date_hour_2.matches(date_hour_1))

def test_wildcard_matching_matches():
    date_hour_1 = DateHour({'year': '2021', 'month': '12', 'day': '*', 'hours': '12', 'minutes': '*'})
    date_hour_2 = DateHour({'year': '*', 'month': '*', 'day': '24', 'hours': '12', 'minutes': '0'})
    assert(date_hour_2.matches(date_hour_1))

def test_wildcard_matching_not_matches():
    date_hour_1 = DateHour({'year': '2021', 'month': '12', 'day': '5', 'hours': '17', 'minutes': '9'})
    date_hour_2 = DateHour({'year': '*', 'month': '*', 'day': '*', 'hours': '19', 'minutes': '0'})
    assert(not date_hour_2.matches(date_hour_1))


