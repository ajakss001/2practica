class Worker:
    def __init__(self, pay_per_day, days_worked):
        self.pay_per_day = pay_per_day
        self.days_worked = days_worked

    def calculate_salary(self):
        salary = self.pay_per_day * self.days_worked
        print(f"Salary: {salary} rub")
        return salary


employee1 = Worker(1500, 20)
employee1.calculate_salary()

employee2 = Worker(2000, 15)
employee2.calculate_salary()    