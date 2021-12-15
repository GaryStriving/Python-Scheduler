from src.DateHour import DateHour
import json
import datetime
import os

class Scheduler:
    def __init__(self,filename):
        self.data = []
        if filename and os.path.isfile(filename):
            with open(filename) as ifile:
                settings = json.load(ifile)
                self.data = settings["tasks"]
    def register(self,command,time):
        if isinstance(time,datetime.datetime):
            time = DateHour.from_datetime(time)
        new_task = {"command": command}.update(time.to_dict())
        self.data.append(new_task)
    def unregister(self,func):
        self.data = [task for task in self.data if not func(task)]
    def save(self,filename):
        settings = {}
        if filename and os.path.isfile(filename):
            with open(filename,'r') as ifile:
                settings = json.load(ifile)
        settings["tasks"] = self.data
        with open(filename,'w') as ofile:
            json.dump(settings,ofile)