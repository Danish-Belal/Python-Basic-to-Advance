# Map applies a function to all the in an input list.

# suppose we want a square of a list.


def square(num):
    return num*num


l = [1,2,4] 
# First Method
squareList = []  # create a empty list
for i in l:
    squareList.append(square(i))
print(squareList)    

# Method 2 using map

print(list(map(square,l)))  # map take a function(can be lamda) and input list as argument. list function change output of map in list











