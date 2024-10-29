class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team.")

class Developer(Employee):
    def work(self):
        print("Developer is writing code.")

manager = Manager()
developer = Developer()

manager.work()
developer.work()