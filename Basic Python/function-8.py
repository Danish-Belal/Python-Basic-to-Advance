# Function with Argument
'''
def percent(marks):
    return((marks[0]+marks[1]+marks[2]+marks[3])/40)*100


marks1 = [7, 5, 8, 7]
percent1 = percent(marks1)

marks2 = [8, 9, 5, 3]
percent2 = percent(marks2)

print(percent1, percent2)


def greet(name):
    print ("Good Morning "+ name)

greet("danish")


def sum(a , b):
    return a+b

a=10
b=60
print(sum(a,b)) 
'''  

# Default Parameter Values
 
def Greet(name="Shahzeb"):          # Shahzeb is default parameter , this value will used when no argument is passed
    return "Hello  " + name

print(Greet("Danish "))
print(Greet())


