# self refres to instance of the class. Automatically passed with a function call from an object.

class Employee:
    company = 'Google'
    def getsalary(self):
        print(f"The company is {self.company} and the salary is {self.salary}")
    def getInfo(self):
        print(f"Your company name is {self.company}")

Danish = Employee()
Danish.salary = 10000
Danish.getsalary()     #Employee.getsalary(Danish)   Both are same
Danish.getInfo()