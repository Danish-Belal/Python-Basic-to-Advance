
'''
def square(num):
    return num*num

a = square(10)
print(a)    
'''


# Lamda function --> Function creating using an expression using lamda keyword
square = lambda num: num*num  # creating a square lamda function which takes num as input and multiply num*num and return to square
num = 10
a=square(num)
print(a)

sum = lambda a,b,c: a+b+c
s= sum(num,4,6)  # return 20 , take first value num =10
print(s)

