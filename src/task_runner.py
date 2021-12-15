from DateHour import DateHour
import time
import datetime
import subprocess
import json

class Task:
    def __init__(self,command,date_and_hour):
        self.command = command
        self.date_and_hour = date_and_hour
    def get_time_to_task(self,from_hour):
        return self.date_and_hour.time_from(from_hour)
    def run(self):
        subprocess.call(self.command)

class TaskRunner:
    def __init__(self,filename):
        with open(filename) as ifile:
            ifile_data = json.load(ifile)
            self.tasks = [Task(task_data['command'],DateHour(task_data)) for task_data in ifile_data['tasks']]
    def await_next(self):
        if len(self.tasks) == 0:
            raise
        last_checked = None
        while True:
            now = datetime.datetime.now()
            now_datehour = DateHour.from_datetime(now)
            if now_datehour != last_checked:
                for task in self.tasks:
                    if task.matches(now_datehour):
                        task.run()
                last_checked = now_datehour
            time.sleep(60 - now.second)