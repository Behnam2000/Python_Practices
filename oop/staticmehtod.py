class Employee:

    num_of_emps = 0
    raise_amount = 1.1

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self, amount):
        return self.pay + amount

        
emp_1 = Employee("Bardia", "Saheri", 45000)

print(emp_1.apply_raise(6000))



