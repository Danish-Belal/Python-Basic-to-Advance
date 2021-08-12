# Two types of Variable . 1: Local Variable. 2: Loacal Variable
'''
a = 50  # Global variabal 
def fun1():
    global a # using Global Veriable in Function
    print(a)
    a= 10    # Local Variable
    print(a)

fun1()    
print(a)  
'''

# if local variable is not given inside a function then it use global keyword.

name = "Danish"
def greet():

    global name    # by writing global we say to compiler to use global value
    name = "Shahzeb"
    print(f"Hello {name}")


greet()
print(name)
