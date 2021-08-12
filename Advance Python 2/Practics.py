# Q1: input name , number , marks , and print it using formate
'''
name = input("Enter you Name: ")
Marks = int(input("Enter your Mrks: "))
Pno = int(input("Enter your Phone no: "))

val = "The name of the student is {} , his Marks are {} and Phone number is {}.".format(name , Marks , Pno)
#val = "The name of the student is {0} , his Marks are {1} and Phone number is {2}".format(name , Marks , Pno)  # can use index also
print(val)
'''

# Q2: print a table in verticle using list comprehension.
'''
l = [(i*7) for i in range(1,11)]
print(l)

l = [str(i*7) for i in range(1,11)]    # for using join we need to change int into string
verticleTable = '\n'.join(l)
print(verticleTable)

'''

# Q3: filter a list which is divisable by 5

'''
#Divby5 = lambda num: (num % 5 == 0)


l = [5, 60, 15, 10, 30, 45, 54, 34, 12]

#val = list(filter(Divby5,l))
val = filter(lambda num:( num % 5 == 0) , l)   # can write function as filter first argument
print(list(val))   # changing in list is compulsory

'''

#Q4:  Find maximum of the number in a list using reduce function. 
'''
from functools import reduce    # to use reduce we need to reduce

l = [4,6,8,9,7,5,3,52,19]

#Maxno = lambda num1 , num2 : max(num1,num2)
#result = reduce(Maxno , l)

result = reduce(max , l)
print(result)

'''















