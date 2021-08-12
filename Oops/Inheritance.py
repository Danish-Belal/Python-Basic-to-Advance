# Inheritance is a way to creating a new class from an existing class.

class Employee:                     # base class / parent class
    company = 'Google'
    def detail(self):
        print("This is an Employee")


class Programmer(Employee):  # we can use all attribute and method of Employee calss in Programer class. #Drive class/child class.
    def getDetail(self):
        print("This is a Programmer")
    #company = 'Youtube'   # if value of company will not present in instance/drive class then it will use parent class value.

e = Employee()
print(e.company)
e.detail()
p= Programmer()    
p.getDetail()
p.detail()    
print(p.company)

