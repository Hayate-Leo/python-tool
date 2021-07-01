
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
    
    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp: str):
        first, last, pay = emp.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

if __name__ == '__main__':
    print(Employee.num_of_emps)
    emp_1 = Employee('Test1', 'User2', 50000)
    emp_2 = Employee('Test2', 'User2', 60000)

    emp_str_1 = 'John-Doe-70000'
    emp_str_2 = 'Steve-Smith-80000'
    emp_str_3 = 'Jane-Doe-90000'

    new_emp_1 = Employee.from_string(emp_str_1)

    print(new_emp_1.email)
    print(type(new_emp_1.pay))

    Employee.set_raise_amt(1.05)

    print(emp_1.raise_amt)
    print(emp_2.raise_amt)

    print(Employee.num_of_emps)

    import datetime
    my_date = datetime.date(2021, 7, 1)
    print(Employee.is_working(my_date))
