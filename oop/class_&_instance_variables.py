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

emp_1 = Employee('Behnam', 'Safari', 43000)
emp_2 = Employee('Bahar', 'Saberi', 23000)

emp_1.raise_amount = 1.15

# print(emp_1.__dict__)    # using the instance 
# print(Employee.__dict__) # using the class

print(Employee.raise_amount) # using the class
print(emp_1.raise_amount)    # using an instance
print(emp_2.raise_amount)    # Using an instance


print(Employee.num_of_emps)