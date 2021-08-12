def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

# fibonacci Series
def feb(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return (n-1) + (n-2)    
        
print(feb(6))        




















