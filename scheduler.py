
class Task:
    def __init__(self,data_string):
        # data_string: string
        # Must be in the following format:
        # YYYY MM DD hh mm path/to/file
        data_string = data_string.split(' ')
        if len(data_string) != 6:
            raise
        self.data = {['year','month','day','hours','minutes','path'][i]:
                     data_string[i] for i in range(6)}
    def __str__(self):
        return str(self.data)
    def __eq__(self,other):
        return self.data == other.data
    def __gt__(self,other):
        

class TaskRunner:
    def __init__(self,filename):
        self.tasks = [Task(task_data_string) for task_data_string in open(filename,'r').read().split('\n')]
    def await_next(self):
        pass

task_runner = TaskRunner('example.txt')

while True:
    task_runner.await_next()
