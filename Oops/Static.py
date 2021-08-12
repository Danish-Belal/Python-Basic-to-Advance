# we need a function that does not use the self parameter then we define static method.
# Static method is a decorator to mark grade as a static method.

class Employee:
    company = 'Google'

    def getsalary(self , signature):           # we can pass multiple argument with self Argument.
        print(f"The company is {self.company} and the salary is {self.salary}\n Signature is {signature}")

    # If we dont want to use self in a function then we use static method.
    @staticmethod
    def greet():
        print("Hello There")

    @staticmethod               # We can create multiple static method.
    def time():
        print("The time is 9.00 PM" ) 


Danish = Employee()
Danish.salary = 10000 
Danish.getsalary('danishbelal..')     #Employee.getsalary(Danish)   Both are same
Danish.greet()  # Employee.greet()
Danish.time()
