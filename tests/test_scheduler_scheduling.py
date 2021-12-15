from src.scheduler import Scheduler
from src.DateHour import DateHour

def test_empty_constructor():
    scheduler = Scheduler()
    assert(scheduler.data == [])

def test_constructor():
    scheduler = Scheduler('example.json')
    example_json = [{"year": "*", "month": "*", "day": "*", "hours": "17", "minutes": "0", "command": ["C:/Users/Administrator/Desktop/Exercise-Reminder/build/Release/Exercise-Reminder.exe"]}]
    assert(scheduler.data == example_json)

def test_register_task():
    scheduler = Scheduler()
    task_time = DateHour({'year': '*', 'month': '*', 'day': '*', 'hours': '*', 'minutes': '*'})
    scheduler.register(['py','hi'],task_time)
    generated_json = [{"year": "*", "month": "*", "day": "*", "hours": "*", "minutes": "*", "command": ["py","hi"]}]
    assert(scheduler.data == generated_json)