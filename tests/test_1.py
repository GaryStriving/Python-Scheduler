from task_runner import DateHour, Task, TaskRunner

def test_date_hour_comparison():
    date_hour_1 = DateHour({'year': '2021', 'month': '12', 'day': '5', 'hours': '17', 'minutes': '9'})
    date_hour_2 = DateHour({'year': '*', 'month': '*', 'day': '*', 'hours': '19', 'minutes': '0'})
    assert(date_hour_2 > date_hour_1)



