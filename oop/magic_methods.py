class Employee :

    num_of_emps = 0
    raise_amount = 1.1
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def appy_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname()}, {self.email}"
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    
emp_1 = Employee('Behnam', 'Safari', 43000)
emp_2 = Employee('Bahar', 'Saberi', 23000)

print(emp_1) 

print(repr(emp_1))
print(str(emp_1))

# Same as to lines above
print(emp_2.__repr__())
print(emp_2.__str__())

print(emp_1 + emp_2)


print(len(emp_2))