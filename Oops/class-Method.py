# class method --> Class method is bound to the class  and not the object of the class
# @classmethod decorator is used to create a class method

class Employee:
    company = 'Wipro'
    salary =200
    location = 'Kolkatta'

   # def changeSalary(self , sal):
    #    self.__class__.salary = sal   # tunder class to chng class method attribure.


    @classmethod                        # use class decorator to modifiy value of class. it is a function and its take attribute
    def changeSalary(cls , sal):
        cls.salary = sal

e = Employee()
print(Employee.salary)
e.changeSalary(500)     # here we are only changing salary value in instance attribute , not class attribute
print(e.salary) 
print(Employee.salary)   


