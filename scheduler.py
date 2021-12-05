
class Scheduler:
    def __init__(self):
        pass
    def add(self,path,time):
        pass
    def delete(self,id):
        pass
    def process(self,command):
        pass


def main():
    scheduler = Scheduler()
    while True:
        command = input()
        scheduler.process(command)

if __name__ == '__main__':
    main()
