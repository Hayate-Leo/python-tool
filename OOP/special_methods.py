
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
    
    def __repr__(self) -> str:
        return f'Employee({self.first}, {self.last}, {self.pay})'
    
    def __str__(self) -> str:
        return f'{self.full_name()} - {self.email}'
    
    def __add__(self, other):
        return self.pay + other.pay


    
if __name__ == '__main__':
    emp_1 = Employee('Test1', 'User2', 50000)
    emp_2 = Employee('Test2', 'User2', 60000)

    print(emp_1 + emp_2)

    print(emp_1.__repr__())
    print(emp_1.__str__())
