# There are many types of error generate in python when something goes wrong.
try:
    a = int(input("Enter a no: "))
    c = 1/a
    print(c)

except TypeError as e:
    print("Make sure you have enterd a intger.")  
    print(e) 

except ZeroDivisionError as e:
    print("Can not divide by 0 ")  

except:
    print("Error")    

      

print("Thanks! Hope you understand this code")  










