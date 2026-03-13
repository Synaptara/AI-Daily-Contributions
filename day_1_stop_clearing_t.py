class TaskManager:
    def __init__(self):
        self.tasks = []
        self.clearing_task_id = None

    def add_task(self, task_id):
        self.tasks.append(task_id)

    def start_clearing(self, task_id):
        self.clearing_task_id = task_id
        self.tasks.remove(task_id)

    def stop_clearing(self):
        self.clearing_task_id = None

def main():
    manager = TaskManager()
    manager.add_task(1)
    manager.add_task(2)
    manager.start_clearing(1)
    print("Clearing task:", manager.clearing_task_id)
    manager.stop_clearing()
    print("Clearing task:", manager.clearing_task_id)

if __name__ == "__main__":
    main()