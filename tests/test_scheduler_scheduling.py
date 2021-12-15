from src.scheduler import Scheduler

def test_constructor():
    scheduler = Scheduler('example.json')
    example_json = [{"year": "*", "month": "*", "day": "*", "hours": "17", "minutes": "0", "command": ["C:/Users/Administrator/Desktop/Exercise-Reminder/build/Release/Exercise-Reminder.exe"]}]
    assert(scheduler.data == example_json)
    