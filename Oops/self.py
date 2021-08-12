# self refres to instance of the class. Automatically passed with a function call from an object.

class Employee:
    company = 'Google'
    def getsalary(self):
        print(f"The company is {self.company} and the salary is {self.salary}")

Danish = Employee()
Danish.salary = 10000
Danish.getsalary()     #Employee.getsalary(Danish)   Both are same