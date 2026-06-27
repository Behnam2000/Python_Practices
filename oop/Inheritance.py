class Employee :

    raise_amount = 1.1
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def appy_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.15

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev_1 = Developer("Behnam", "Safari", 65000, "Python")
dev_2 = Developer("Ali", "Azghandi", 80000, "JavaScript")
dev_3 = Developer("Sara", "Banani", 40000, "PHP")

mgr_1 = Manager('Bahar', 'Saberi', 100000, [dev_1, dev_3])

print(mgr_1.email)

mgr_1.add_emp(dev_2)

mgr_1.remove_emp(dev_3)

mgr_1.print_emps()

print(isinstance(mgr_1, Employee)) # True

print(isinstance(mgr_1, Manager)) # True

print(isinstance(mgr_1, Developer)) # False

print(issubclass(Developer, Employee)) # True

print(issubclass(Manager, Developer)) # False


# print(dev_1.email)
# print(dev_1.prog_lang)


# print(dev_1.pay)
# dev_1.appy_raise()
# print(dev_1.pay)