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
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Behnam', 'Safari', 43000)
emp_2 = Employee('Bahar', 'Saberi', 23000)

Employee.set_raise_amt(1.4)

print(Employee.raise_amount) # using the class
print(emp_1.raise_amount)    # using an instance
print(emp_2.raise_amount)    # Using an instance


emp_str_1 = "Sara-Doe-70000"
emp_str_2 = "Nima-Nazari-20000"
emp_str_3 = "Hamid-Shafiei-60000"

new_emp_1 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_1.pay)