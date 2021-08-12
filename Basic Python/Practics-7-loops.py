# Q1 Program to print table of a given no.
'''
n = int(input("Enter a no for table\n"))

for i in range(1, 11):
    # print(n, " X ", i, " = ", n*i)
    #can chang all in string and the intiger inside {} is using f string
    print(f"{n} X {i} = {n*i}")

'''

# send greet all person whose name start with s on the list.
'''
l = ['Danish', 'Shahzeb ', 'Arbaz  ', 'Sotasim']
greet = 'Hello You are great '

for name in l:
    # if(name[0]=="S"):
    if name.startswith('S'):
        print(name, "!",  greet)
'''

# Question 2 by using while loop
'''
l = ['Danish', 'Shahzeb ', 'Arbaz  ', 'Motasim']
greet = 'Hello You are great '

i = 1
while i<len(l):
    print( l[i] , greet)
    i+=1

'''

# Find a given no is prime or not.
'''
n = int(input("Enter a no\n"))
prime = True
for i in range(2,n):
    if (n%i==0):
       prime = False
       break
if(prime):
    print("No is Prime")
else:
    print("No is not prime")

'''

# Q5 sum of first n natural no using loop.
'''
i = 1
sum=0
n = int(input("Enter a no for sum\n"))
while i<n:
    sum+=i
    i+=1
print("The sum is ",sum)
'''

# Q6 Factorial of a number.
'''
n = int(input("Enter a number for Factorial\n"))
factorial =1
for i in range(1,n+1):
    if n==0 or n==1:
        factorial = 1
    else:
        factorial= factorial*i
print(f"The factorial is {factorial}")
  '''


# Q7 print pyramid star
#n = int(input("Enter n\n"))
'''
n=3
for i in range(3):
    print(" "*(n-i-1), end = "")
    print("*"*(2*i+1), end="")
    print(" "*(n-i-1))
'''

# Q8 - print star pattern
'''
n=4
for i in range(n+1):
    print(" * "*i)
'''

# Table in reverse order.
'''
n= int(input("Enter a no for Table\n"))
for i in reversed(range(1,11)):
    print(f"{n} X {i} = {n*i} ")
'''


  
