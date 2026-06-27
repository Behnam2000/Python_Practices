class Employee :
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"
 
emp_1 = Employee('Behnam', 'Safari', 43000)
emp_2 = Employee('Bahar', 'Saberi', 23000)

# print(emp_1)
# print(emp_2)


print(emp_1.email)
print(emp_2.email)