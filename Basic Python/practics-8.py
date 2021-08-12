# Q1 -To find greatest among Three number
'''
def greatest( num1 , num2 , num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3      

print(greatest(55,617,789))   
'''


# Q2- Convert Celsius to Fahrenheit
'''
def Fahrenheit(celcius):
    return (celcius *(9/5))+32

c = 0
print("The temprature in fahrenheit is " , Fahrenheit(c))    
'''

# sum of first natural number.
'''
def natural(n):
    if n==0 :
        return 0
    else:    
        return n+ natural(n-1)

print(natural(3))   
'''

this = "   This    is Danish    Belal   o"
print(this)
print(this.strip())







