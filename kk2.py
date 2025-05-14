class Worker:
    def set_daily_wage(self, amount):
        self.daily_wage = amount

    def set_work_days(self, number):
        self.work_days = number

    def show_daily_wage(self):
        return self.daily_wage

    def show_work_days(self):
        return self.work_days

    def compute_pay(self):
        total = self.daily_wage * self.work_days
        print(f"Payment: {total} rubles")
        return total


worker = Worker()

worker.set_daily_wage(1500)
worker.set_work_days(20)

print("Daily wage:", worker.show_daily_wage())
print("Work days:", worker.show_work_days())

worker.compute_pay()