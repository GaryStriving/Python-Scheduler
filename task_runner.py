import time
import datetime
import subprocess
import json

class DateHour:
    def __init__ (self,data):
        assert(all(k in data for k in ['year','month','day','hours','minutes']))
        self.data = {k: str(v) if v != str else v for k,v in data.items() if k in ['year','month','day','hours','minutes']}
    def __str__(self):
        return str(self.data)
    def __eq__(self,other):
        return type(self) == type(other) and self.data == other.data
    def __ne__(self,other):
        return not (self == other)
    def time_from(self,time_to_compare):
        minutes = 0
        for criteria in ['year','month','day','hours','minutes']:
            if self.data[criteria] == time_to_compare.data[criteria]:
                continue
            if self.data[criteria] == '*' or time_to_compare.data[criteria] == '*':
                continue
            minutes += (int(time_to_compare.data[criteria]) - int(self.data[criteria])) * {'year': 525600, 'month': 43800, 'day': 1440, 'hours': 60, 'minutes': 1}[criteria]
        return -minutes

class Task:
    def __init__(self,path,date_and_hour):
        self.path = path
        self.date_and_hour = date_and_hour
    def get_time_to_task(self,from_hour):
        return self.date_and_hour.time_from(from_hour)
    def run(self):
        subprocess.call([self.path])

class TaskRunner:
    def __init__(self,filename):
        with open(filename) as ifile:
            ifile_data = json.load(ifile)
            self.tasks = [Task(task_data['path'],DateHour(task_data)) for task_data in ifile_data['tasks']]
    def await_next(self):
        if len(self.tasks) == 0:
            raise
        last_checked = None
        while True:
            now = datetime.datetime.now()
            now_datehour = DateHour({'year': str(now.year), 'month': str(now.month),'day': str(now.day), 'hours': str(now.hour), 'minutes': str(now.minute)})
            if now_datehour != last_checked:
                for task in self.tasks:
                    if task.get_time_to_task(now_datehour) == 0:
                        task.run()
                last_checked = now_datehour
            time.sleep(60 - now.second)