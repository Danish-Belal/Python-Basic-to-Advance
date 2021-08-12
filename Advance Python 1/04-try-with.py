#  ***Try with else***

# Else condition will only execute if try condition will run. sometime we want to print something after try so we use else
'''
try:
    a = int(input("Enter a no: "))
    div = 1/a
    print(div)

except Exception as e:
    print(e)

else:   # else conditon is executing when try completly run
    a +=1 
    print("Try has successfully run.")
    print(a)        
'''

# *** Try with finally ***

# Python offers a finally clause to which ensure execution of a piece of code  irrespective of the execution.

try:
    a = int(input("Enter a no: "))
    div = 1/a
    print(div)

except Exception as e:
    print(e)
    exit()

# finally will execute eve after try will fail and exception excute. if we exit() form excption , Even then finally execute.
finally:   
    print("Finally! is printed")   

print("Thanks for using this program")  # this will not execute if try will fail. 






