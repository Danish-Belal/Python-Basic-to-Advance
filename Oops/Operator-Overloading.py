# Operators in python can be overloaded using Dunder Metohd.
# These Method are called when a given operator is used on the objects

class Calculator:

    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print('Add')
        return self.num + num2.num

    
    def __sub__(self, num2):
        print("Substraction")
        return self.num-num2.num    

    def __mul__(self, num2):
        print("Multiplication")
        return self.num * num2.num

    
    def __truediv__(self, num2):
        print("Division")
        return self.num/num2.num

    
    def __floordiv__(self, num2):
        print("Remander")
        return self.num//num2.num
    # Other Dunder Method
    def __str__(self):
        return f"Decimal no is {self.num}"

    def __len__(self):
        return 1

n1 = Calculator(50)
#n2 = Calculator(3)
'''
sum = n1+n2
print(sum)

Subtraction= n1-n2
print(Subtraction)

Multplication = n1*n2
print(Multplication)

TrueDivision = n1/n2
print(TrueDivision)

Division = n1//n2
print(Division)
'''
print(n1)
print(len(n1))