# Q1: open three file 1.txt ,2.txt,3.txt , if any of thee file is not present , a massage without exiting the
# program must be printed prompting the same.
'''
def openFile(filename):
    try:
        with open(filename, 'r') as f:
            a=f.read()
            print(a)

    except FileNotFoundError:
        print(f"File {filename} is not found")

openFile('1.txt')        
openFile('2.txt')  
openFile('3.txt')
'''

# Q2 - print third, fifth and seventh element from a list using enumerate function.
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for i , item in enumerate(l):
    if i==2 or i==4 or i==6:
        #print(i,item)
        print(f"The {i+1} Element is {item}")
'''
# Q3-  write a list comprehension to print a list which contains the multiplication table of a user enterd number.

'''
num = int(input("Enter you number: "))
table = [num*i for i in range(1,11)]   
print(table)
'''

# Q4- write a program to display a/b, where a and b are integers. If b = 0 , display infinity by handling
# the ZeroDivisionError
'''
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

try:
    c= a/b
    print(f"The value is {c}")
    
except ZeroDivisionError:
    print("Infinite")
'''

# Q5 - store a multplication table generated in Q3 in a file name Table.txt

num = int(input("Enter a no for Table: "))
Table = [num*i for i in range(1, 11)]
print(Table)

with open('Table.txt', 'a') as f:
    f.write(str(Table))
    f.write('\n')
