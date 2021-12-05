import datetime

class DateHour:
    def __init__ (self,data):
        # YYYY MM DD hh mm path/to/file
        assert(all(k in data for k in ['year','month','day','hours','minutes']))
        self.data = data
    def __str__(self):
        return str(self.data)
    def __eq__(self,other):
        return self.data == other.data
    def __ne__(self,other):
        return not (self == other)
    def __gt__ (self,other):
        return self.time_from(other) > 0
    def __ge__ (self,other):
        return self.time_from(other) >= 0
    def __lt__ (self,other):
        return self.time_from(other) < 0
    def __le__ (self,other):
        return self.time_from(other) <= 0
    def time_from(self,time_to_compare):
        # Compare with other time
        # The time to compare must not have any wildcard.
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
        # data_string: string
        # Must be in the following format:
        # YYYY MM DD hh mm path/to/file
        if len(args) != 6:
            raise
        self.path = path
        self.date_and_hour = date_and_hour
        

class TaskRunner:
    def __init__(self,filename):
        self.tasks = [Task(task_data_string) for task_data_string in open(filename,'r').read().split('\n')]
    def await_next(self):
        pass

'''
task_runner = TaskRunner('example.txt')

while True:
    task_runner.await_next()
'''
date_hour_1 = DateHour({'year': '2021', 'month': '12', 'day': '5', 'hours': '18', 'minutes': '9'})
date_hour_2 = DateHour({'year': '*', 'month': '*', 'day': '*', 'hours': '19', 'minutes': '0'})
assert(date_hour_2 > date_hour_1)

print(date_hour_1.time_from(date_hour_2))
