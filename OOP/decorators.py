
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'
    
    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @full_name.deleter
    def full_name(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    
if __name__ == '__main__':
    emp_1 = Employee('Test1', 'User2', 50000)

    emp_1.full_name = 'Corey Schafer'

    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.full_name)

    del emp_1.full_name