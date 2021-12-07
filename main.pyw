from .task_runner import TaskRunner

def main():
    task_runner = TaskRunner('example.json')
    while True:
        task_runner.await_next()

if __name__ == '__main__':
    main()